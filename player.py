#coding:utf-8
import pygame
import time
file = r'd:/1278.主，我邀请你.mp3'
file = file.encode('utf-8') #支持中文名字
pygame.mixer.init()
#pygame.mixer.music.load(file)
load = pygame.mixer.music.load(file)
pygame.mixer.music.play()
#time.sleep(10)
while True:
    pass