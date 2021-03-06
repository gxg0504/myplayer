import pymysql

class MysqlHelper(object):
    config={
        'host' : 'zled.top',
        'user' : 'root',
        'password': 'Fguan9001.',
        'db' : 'db_mp3',
        'charset':'utf8'
    }

    def __init__(self):
        self.connection = None
        self.cursor = None
        connection = pymysql.connect(**MysqlHelper.config)

    def getOne(self,sql,*args):
        try:
            self.connection = pymysql.connect(**MysqlHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql,args)
            return self.cursor.fetchone()
        except Exception as ex:
            print(ex,ex)
        finally:
            self.close()


    def getList(self,sql,*args):
        try:
            self.connection = pymysql.connect(**MysqlHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql,args)
            return self.cursor.fetchall()
        except Exception as ex:
            print(ex,ex)
        finally:
            self.close()

    def executeDML(self,sql,*args):
        try:
            self.connection = pymysql.connect(**MysqlHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql,args)
            new_id = self.connection.insert_id() #返回系统自增生成的新id
            self.connection.commit()
            return new_id
        except Exception as ex:
            self.connection.rollback()
            print(ex,ex)
        finally:
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

if __name__ == '__main__':
    helper = MysqlHelper()
    print('init ok')
    helper.executeDML('insert into t_money(money) VALUES (%s)',1000)
    print(helper.executeDML('DELETE FROM t_money WHERE money =%s',1000))