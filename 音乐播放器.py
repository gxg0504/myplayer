
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilenames

import pygame
from playservice import Service

#<Button-1>:鼠标左击事件
#<Button-2>:鼠标中击事件
#<Button-3>:鼠标左击事件
#<Button-Release-x>:鼠标左击事件,x=[1,2,3],分别表示鼠标的左、中、右键操作
#<Double-Button-1>:双击事件

class MainWindow:
    def play(self,event):
        # track = pygame.mixer.music.load(r'd:/11.mp3')
        # print(track,type(track))
        # pygame.mixer.music.play()
        num = self.t1.curselection() #返回用户选择歌曲的下标
        mp3_name = self.t1.get(num)  #根据下标返回mp3名字
        self.service.play_mp3(mp3_name)

    def buttonListener2(self,event):
        tkinter.messagebox.showinfo('messagebox','this is button 2 dialog')

    def buttonListener3(self,event):
        tkinter.messagebox.showinfo('messagebox','this is button 3 dialog')

    #点击导入歌曲调用的函数
    def loadMp3(self,event):
        #tkinter.messagebox.showinfo('messagebox','this is button 4 dialog')
        files = askopenfilenames(filetypes = (('Mp3 file','*.mp3*'),)) #弹出一个文件选择框
        self.service.load_mp3(files) #插入到数据库中
        list = self.service.find_play_list_by_user() #查出播放列表
        #print(list)
        self.t1.delete(0, END)
        for i in list:
            self.t1.insert(END,i[0])

    def select_text(self,event):
        # tkinter.messagebox.showinfo('messagebox','this is')
        # item = self.t1.curselection()
        # print(self.t1.get(item))
        pass

    def __init__(self,service):
        self.service = service
        self.frame=Tk()
        self.frame.title('')
        self.button1 = Button(self.frame,text = '播放')
        self.button2 = Button(self.frame,text = '暂停')
        self.button3 = Button(self.frame,text = '停止')
        self.button4 = Button(self.frame,text = '导入歌曲')
        self.button5 = Button(self.frame,text = '删除歌曲')
        self.button6 = Button(self.frame,text = '增加音量')
        self.button7 = Button(self.frame,text = '减小音量')

        self.t1 = Listbox(self.frame,{'selectmode':SINGLE}) #播放列表play list
        self.button1.grid(row=0,column=0,padx=5,pady=5)
        self.button2.grid(row=0,column=1,padx=5,pady=5)
        self.button3.grid(row=0,column=2,padx=5,pady=5)
        self.button4.grid(row=0,column=3,padx=5,pady=5)
        self.button5.grid(row=0,column=4,padx=5,pady=5)
        self.button6.grid(row=0,column=5,padx=5,pady=5)
        self.button7.grid(row=0,column=6,padx=5,pady=5)

        self.t1.grid(row=1,column=0,padx=5,pady=5,columnspan=6)

        #返回登录用户的播放列表
        list = self.service.find_play_list_by_user()
        #print(list)
        self.t1.delete(0, END) #清空list
        for i in list:
            self.t1.insert(END,i[0])

        self.t1.bind('<ButtonRelease-1>',self.select_text)

        self.button1.bind('<ButtonRelease-1>',self.play)
        self.button2.bind('<ButtonRelease-1>',self.buttonListener2)
        self.button3.bind('<ButtonRelease-1>',self.buttonListener3)
        self.button4.bind('<ButtonRelease-1>',self.loadMp3)

        self.frame.mainloop()

if __name__ =='__main__':
    un=input('请输入登录的账号：')
    pwd = input('请输入登录的密码：')
    service = Service()
    if service.login(un,pwd):
        pygame.mixer.init()
        window = MainWindow(service)
