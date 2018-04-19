
from mysql_lib import MysqlHelper
import  pygame
class Service(object):
    def __init__(self):
        self.helper = MysqlHelper()
        pygame.mixer.init()



    def login(self,username,password):
        user = self.helper.getOne('select id,username,password from t_user WHERE username =%s AND password = %s',username,password)
        if user:
            print('%s 登陆成功'%user[1])
            self.username = user[1]
            self.uid = user[0]
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
                self.helper.executeDML('insert into t_mp3 (mp3_name,mp3_file) VALUES (%s,%s)',mp3_name,f)
                mp3_id = self.helper.getOne('select id from t_mp3 where mp3_name=%s',mp3_name)
                self.helper.executeDML('insert into t_play_list (mid,uid) VALUES (%s,%s)',mp3_id[0],self.uid)
        else:
            print('用户没有选择文件')

    #根据用户登录之后的ID，从数据库中查到该用户播放列表
    def find_play_list_by_user(self):
        sql='select t2.mp3_name from t_play_list as t1 join t_mp3 as t2 on t1.mid=t2.id where t1.uid = %s'
        return  self.helper.getList(sql,self.uid)

    def play_mp3(self,mp3_name):
        file_path = self.helper.getOne('select mp3_file from t_mp3 where mp3_name=%s',mp3_name) #tuple
        if file_path and file_path[0]: #数据库中找到了mp3的路径
            file = r'%s'%file_path[0]
            file = file.encode('utf-8')
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()

    def delete_play_list(self,mp3_name):
        mp3_id = self.helper.getOne('select id from t_mp3 where mp3_name = %s',mp3_name)
        if mp3_id:
            self.helper.executeDML('delete from t_play_list WHERE mid = %s AND uid=%s',mp3_id[0],self.uid)


