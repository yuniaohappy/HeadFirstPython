import os

#过滤sql文件中的表名
def table_name(table_string):
    if "--" in table_string:
        pass
    elif "<!" in table_string:
        pass
    elif "ODS_" in table_string or "ods_" in table_string:
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




