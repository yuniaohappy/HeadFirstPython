#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import os

from __builtin__ import raw_input

from interfaceinfo import InterfaceInfo
#过滤sql文件中的表名
def table_name(table_string,str01 = "ODS_",str02 = "ods_"):
    if "--" in table_string:
        pass
    elif "<!" in table_string:
        pass
    elif str01 in table_string or str02 in table_string:
        pass
#过滤元素中的空格、tab、空字符
def get_list_string(list_string):
    return(list_string.replace("\n","").replace(" ","").replace("\t","").strip())

#过滤Hive库中含有date的字段
def get_date_string(col_string):
    if "|" in col_string and "date" in col_string or "dt" in col_string:
        col_res_date = str(col_string.replace(" ","").replace("\t","").strip)
        col_date = col_res_date.strip().split("|")[1]
        return col_date
    else:
        return None

#执行脚本获取数据库中日期字段
def get_date(table_name):
    beeline = "beeline -u jdbc:hive2://22.224.72.3:10000 -n hdfs -e "
    comm = beeline + "\"" + "desc " + table_name + "\""
    lis = os.popen(comm).readlines()
    lis02 = [get_date_string(s) for s in lis]
    lis03 = ""
    for li in lis02:
        if li != None and lis03 == "":
            lis03 = li
        elif li != None and lis03 != None:
            lis03 += "," + li
    if len(lis03) == 1:
        return lis03[0]
    elif len(lis03) == 0:
        return None
    elif len(lis03) > 1:
        select_date = os.popen(beeline + "\"select " + lis03 +
                               " from " + table_name + " limit 10\"").readlines()
        #显示查询结果
        for i in select_date:
            print(i)
        table_input = raw_input("请选择一个列的名称，输入字段全名称（输入0为空）：")
        if table_input != "0":
            while table_input not in lis03:
                table_input = raw_input("输入错误，请重新输入：")
            return (str(table_input))
        else:
            return ""
        return (str(table_input))

#查询数据库中的开始日期和结束日期
def get_start_end_date(table_name,col_name):
    sql = "select min(" +col_name + ") as min,max(" + col_name + ") as max from " + table_name + \
          "where " + col_name + "is not null and " + col_name + " != '' and " + col_name  + "!= ' '"
    max_min = os.popen("beeline -u jdbc:hive2://22.224.72.3:10000 -n hdfs -e \"" + sql + "\"").readlines()
    m = max_min[3].split("|")
    dic = {}
    dic['mi'] = m[1]
    dic['ma'] = m[2]
    return dic

#获取ods和表名
def ods_name(path):
    lis = []
    s = str("cat " + path)
    lis = os.popen(s).readlines()
    lis01 = [table_name(s) for s in lis]
    lis02 = [t for t in lis01 if t != None]
    return(lis02[0])
def get_table_type(table_name):
    sql = "desc " + table_name
    table_type = os.popen("beeline -u jdbc:hive2://22.224.72.3:10000 -n hdfs -e \"" + sql +"\"").readlines()
    tab_str = [ts.replace("\n","").replace(" ","").replace("\t","")
               .strip().splite("|")[1] for ts in table_type[3:len(table_type)-1]]
    if "start_dt" in tab_str and "end_dt" in tab_str:
        return str("历史拉链表")
    elif "etl_load_date" in tab_str or "ETL_LOAD_DATE" in tab_str:
        return("流水表")
    else:
        return ""
#处理sql文件中的业务主键
def get_primary_key(path):
    lis = []
    comm = str("cat " + path)
    lis = os.popen(comm).readlines()
    lis02 = [table_name(s,"ON","on") for s in lis]
    lis03 = []
    for li in lis02:
        if type(li) is list:
            lis03 += li

    if len(lis03) == 0:
        return ""
    elif len(lis03) > 0:
        if 'ON' in lis03 or 'on' in lis03:
            return(str(lis03[lis03.index('=')-1].replace(" ","").split(".")[1]))
        else:
            return ""
    else:
        return ""
# 读取csv文件并将文件进行切分
def read_csv_file(csv_path):
    try:
        with open("interface.csv", "r") as rf:
            rows = rf.readlines()
            for row in rows:
                csv = row.readline().strip().split(",")
                o_name = ods_name(csv[7])
                i_ods_table_name = o_name[len(o_name)-1]
                print("ODS表名称：" + i_ods_table_name)
                i_business_date = get_date(i_ods_table_name)
                print("业务日期：" + i_business_date)
                if i_business_date != "":
                    i_start_end_date = get_start_end_date(i_ods_table_name,i_business_date)
                    print("数据开始、结束日期：" + i_start_end_date['mi'] + "\t" + i_start_end_date['ma'])
                else:
                    i_start_end_date['mi'] = ""
                    i_start_end_date['ma'] = ''
                    print("数据开始、结束日期为空！！！")
                i_table_type = get_table_type(i_ods_table_name)
                print("表类型：" + str(i_table_type))
                i_primary_key = get_primary_key(csv[7])
                print("主键（主要是历史拉链）：" + i_primary_key)
                info = InterfaceInfo(csv[0],csv[1],csv[2],csv[3],csv[4],csv[5],csv[6],csv[7],
                                     i_ods_table_name,str(i_table_type),i_primary_key,i_business_date,
                                     i_start_end_date['mi'],i_start_end_date['ma'],csv[14],csv[15])
                info.write_info()
    except IOError as ioe:
        print("File is read error: " + str(ioe))

def test():
    t_info = read_csv_file("interface_info_lp.csv")

test()
