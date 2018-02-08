"""
    1、系统名称               system_name
    2、子系统代码             sub_system_code
    3、接口名                 interface_name
    4、中文表名               table_name_cn
    5、作业名                 job_name
    6、数据周期（日、月）     data_cycle
    7、是否有下游作业         downstream_job
    8、SQL脚本                sql_script
    9、ODS表名                ods_table_name
    10、表类型                table_type
    11、主键（主要是历史拉链）primary_key
    12、业务日期              business_date
    13、数据开始日期          data_start_date
    14、数据结束日期          data_end_date
    15、负责人                leader_name
    16、备注                  remark

"""


# 定义接口类用于存放属性信息
class InterfaceInfo:
    # 初始化类实例
    def __init__(self, i_system_name, i_sub_system_code, i_interface_name, i_table_name_cn,
                 i_job_name, i_data_cycle, i_downstream_job, i_sql_script, i_ods_table_name,
                 i_table_type, i_primary_key, i_business_date, i_data_start_date, i_data_end_date,
                 i_leader_name, i_remark):
        self.system_name = i_system_name
        self.sub_system_code = i_sub_system_code
        self.interface_name = i_interface_name
        self.table_name_cn = i_table_name_cn
        self.job_name = i_job_name
        self.data_cycle = i_data_cycle
        self.downstream_job = i_downstream_job
        self.sql_script = i_sql_script
        self.ods_table_name = i_ods_table_name
        self.table_type = i_table_type
        self.primary_key = i_primary_key
        self.business_date = i_business_date
        self.data_start_date = i_data_start_date
        self.data_end_date = i_data_end_date
        self.leader_name = i_leader_name
        self.remark = i_remark

    # 将数据写入文件
    def write_info(self):
        try:
            with open("interface_res.csv", "wa+") as wf:
                wf.write(self.system_name + "," +
                         self.sub_system_code + "," +
                         self.interface_name + "," +
                         self.table_name_cn + "," +
                         self.job_name + "," +
                         self.data_cycle + "," +
                         self.downstream_job + "," +
                         self.sql_script + "," +
                         self.ods_table_name + "," +
                         self.table_type + "," +
                         self.primary_key + "," +
                         self.business_date + "," +
                         self.data_start_date + "," +
                         self.data_end_date + "," +
                         self.leader_name + "," +
                         self.remark)
        except IOError as ioe:
            print("File is write: " + str(ioe))
