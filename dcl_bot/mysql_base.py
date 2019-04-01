import pymysql.cursors
from .sqls import sqls


class SQLExecutor:
    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1',
                                          user='root',
                                          password='czk10101',
                                          db='zhdd')

    def executor(self, query_type,para):
        self.connection.connect()
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                # sql = "SELECT ptnw.ptn,yw.yw,yw.AAA FROM ptnw LEFT JOIN yw ON ptnw.ptn = yw.prime WHERE ptnw.ptn LIKE '%para%'"
                sql = sqls[query_type]
                sql=sql.replace('para',para)
                cursor.execute(sql)
                # cursor.execute(sql)
                result = cursor.fetchall()
                return result[:5]
        finally:
            self.connection.close()
