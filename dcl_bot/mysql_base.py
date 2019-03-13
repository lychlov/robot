import pymysql.cursors


class SQLExecutor:
    def __init__(self):
        self.connection = pymysql.connect(host='10.87.164.115',
                                          user='zhdd',
                                          password='1234',
                                          db='mysql')

    def executor(self, para):
        self.connection.connect()
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT ptnw.ptn,yw.yw,yw.AAA FROM ptnw LEFT JOIN yw ON ptnw.ptn = yw.prime WHERE ptnw.ptn LIKE '%%s%'"
                cursor.execute(sql, (para,))
                result = cursor.fetchone()
                print(result)
        finally:
            self.connection.close()
