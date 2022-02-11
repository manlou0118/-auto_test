#auther: Manlou
#date: 2020/10/10

import logging
import time
import os.path


class loggingUtil:
    """
    日志工具类，记录接口调用详情
    """
    def __init__(self):
        pass

    def logWrite(self):
        # 设置日志级别和格式
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #print(rq)

        # 获取日志文件目录和名称
        log_path = os.path.dirname(os.getcwd())+'/Logs/'
        log_file = log_path + rq + '.log'
        global fh
        fh = logging.FileHandler(log_file, mode='a')

        # 输出到文件的等级配置
        fh.setLevel(logging.DEBUG)

        # 配置log文件格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def logError(self, data):
        pass

    def logInfo(self, data):
        logger = self.logWrite()
        logger.info(data)
        logger.removeHandler(fh)









if __name__ == '__main__':
    log1 = loggingUtil()
    log1.logWrite("111")