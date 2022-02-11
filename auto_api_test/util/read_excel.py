#auther: Manlou
#date: 2020/10/15

import xlrd
from util.db_util import MysqlDb


class ReadExcel():
    """
    从excel导入接口测试数据到数据库
    """
    def __init__(self, file_path):
        self.file = file_path
        self.rows = self.get_rows()
        self.cols = self.get_cols()

    def readExcel(self, sheet_index=0):
        """
        读取excel数据并转为数组返回
        :return: list
        """
        data = xlrd.open_workbook(self.file)
        # 获取sheet列表1
        sheet = data.sheet_by_index(sheet_index)
        return sheet

    def get_values(self, rows=0):
        row_data = self.readExcel().row_values(rows)
        row_data[11] = int(row_data[11])
        return tuple(row_data)

    def get_rows(self):
        """
        获取文件行数
        :return: 行数
        """
        rows = self.readExcel().nrows
        return rows

    def get_cols(self):
        """
        获取文件列数
        :return: 列数
        """
        cols = self.readExcel().ncols
        return cols

    def updateDB(self, table):
        conn = MysqlDb()
        for rows in range(1, self.rows):
            sql = 'insert into `{0}` values {1}'.format(table, self.get_values(rows=rows))
            print(sql)
            conn.execute(sql)


if __name__ == '__main__':
    exc = ReadExcel(r"D:\Project\auto_api_test\test.xlsx")
    print(exc.rows, exc.cols)
    exc.updateDB("case")






# 可根据名称获取表
# sheet = data.sheet_by_name(sheet_name)

# 获取所有表，返回列表
# sheet_1 = data.sheet_names()

# 获取行数
# print(sheet.nrows)
# 获取列数
# print(sheet.ncols)
# 获取某行数据，返回列表
# print(sheet.row_values(1))
# 获取某个位置数据
# print(sheet.cell(0, 0).value)