from mysql_lib import MysqlHelper

class Service(object):
    def __init__(self):
        self.helper = MysqlHelper()





    def login(self,username,password):
        user = self.helper.getOne('select username,password from t_user WHERE username =%s AND password = %s',username,password)
        if user:
            print('%s 登陆成功'%user[0])
            self.username = username[0]
            return True
        else:
            print('你输入的用户名和密码错误')
            return False

    def load_mp3(self,files):#files是用户选择的音乐文件列表
        if files:
            for f in files:
                end = f.rfind('.mp3')
                start = f.rfind('/')
                mp3_name = f[start+1:end]
                print(mp3_name)
                print(f)
