"""
    1、系统名称
    2、子系统代码
    3、接口名
    4、中文表名
    5、作业名
    6、数据周期（日、月）
    7、是否有下游作业
    8、SQL脚本
    9、ODS表名
    10、表类型
    11、主键（主要是历史拉链）
    12、业务日期
    13、数据开始日期
    14、数据结束日期
    15、负责人
    16、备注
"""
#定义接口类用于存放属性信息
class InterfaceInfo():
    #初始化类实例
    def __init__(self,):
        pass
    #将数据写入文件
    def write_info(self):
        try:
            with open("interface_res.csv","w") as wf:
                wf.write("")
        except:
            pass