#auther: Manlou
#date: 2020/10/15


import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from util.class_api_test import ClassTestCase



if __name__ == '__main__':

    # 命令行启动
    app = ClassTestCase()
    app_name = sys.argv[1]
    app.runAllCase(app_name)
    # app = ClassTestCase()
    # app.runAllCase('test')

