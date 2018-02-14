#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import os
from interfaceinfo import InterfaceInfo as info
#过滤sql文件中的表名
def table_name(table_string,str01 = "ODS_",str02 = "ods_"):
    if "--" in table_string:
        pass
    elif "<!" in table_string:
        pass
    elif str01 in table_string or str02 in table_string:
        pass
#过滤Hive库中含有date的字段
def get_date_string(colu_string):
    if "date" in colu_string:
        return colu_string

#执行脚本获取数据库中日期字段
def get_date(table_name):
    comm = "desc " + table_name
    lis = os.popen(comm).readlines()[1:len()-1]
    lis02 = str([get_date_string(s) for s in lis]).index(1,len()-1)
    os.popen("beeline -u jdbc:hive2://localhost:10000 -n hdfs -f \"select " + lis + " from " + table_name + "limit 10")

#查询数据库中的开始日期和结束日期
def get_start_end_date(table_name,col_name):
    sql = "select min(" +col_name + ") as min,max(" + col_name + ") as max from " + table_name + \
          "where " + col_name + "is not null and " + col_name + " != '' and " + col_name  + "!= ' ' limit 10"
    max_min = str(os.popen("beeline -u jdbc:hive2://localhost:10000 -n hdfs -e \"" + sql + "\"").readlines()[1])
    (max,min) = str(max_min.index(1,len()-1)).split("|")

#获取ods和表名
def ods_name(path):
    lis = []
    s = str("cat " + path)
    lis = os.popen(s).readlines()

#处理sql文件中的业务主键

# 读取csv文件并将文件进行切分
def read_csv_file(csv_path):
    try:
        with open("interface.csv", "r") as rf:
            csv = rf.readline().strip().split(",")
            info.system_name = csv[0]
            info.sub_system_code = csv[1]
            info.interface_name = csv[2]
            info.table_name_cn = csv[3]
            info.job_name = csv[4]
            info.data_cycle = csv[5]
            info.downstream_job = csv[6]
            info.sql_script = csv[7]
            info.ods_table_name = csv[8]
            info.table_type = csv[9]
            info.primary_key = csv[10]
            info.business_date = csv[11]
            info.data_start_date = csv[12]
            info.data_end_date = csv[13]
            info.leader_name = csv[14]
            info.remark = csv[15]
    except IOError as ioe:
        print("File is read error: " + str(ioe))
