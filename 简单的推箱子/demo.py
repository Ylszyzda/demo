from ast import FloorDiv
from multiprocessing.connection import wait
from turtle import Screen
import pygame
import random
import time
import sys
import tkinter
from data import coin
from pygame.locals import *
from tkinter import ttk
pygame.init()#初始化pygame

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("推箱子")#窗口标题
path = open("data.py","w+")
f = pygame.font.Font('ttf/MBF Pexo.ttf',50)#字体路径
x = 100
y = 100#定义初始坐标
fx = random.randint(3,18)
fy = random.randint(3,10)
dx = random.randint(3,18)
dy = random.randint(3,10)
#变量从data.py中引入

def out():
    print("游戏结束,分数已保存")
    print("coin = "+str(coin),file=path)
    path.close
    pygame.quit()
    sys.exit()#退出函数

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            out()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 25
            if event.key == pygame.K_DOWN:
                y += 25
            if event.key == pygame.K_RIGHT:     #屎山,勿动
                x += 25
            if event.key == pygame.K_LEFT:
                x -= 25
    if x > 925:
        x=925
    if x < 25:
        x=25
    if y > 525:
        y= 525
    if y < 25:
        y= 25
#游戏失败检测
    if 50*fx > 925:#出界检测
        fx=18
        out()
    if 50*fx < 25:
        fx=1
        out()
    if 50*fy > 525:
        fy= 10
        out()
    if 50*fy < 25:
        fy= 1
        out()

    screen.fill(color='white')#窗口颜色
    image1 = pygame.Surface((50,50),flags=pygame.HWSURFACE)#创建一个矩形
    image1.fill(color='pink')
    food = pygame.Surface((50,50),flags=pygame.HWSURFACE)
    food.fill(color='lightgreen')#箱子
    door = pygame.Surface((50,50),flags=pygame.HWSURFACE)#门
    door.fill(color='darkred')
    text = f.render ("coin: "+str(coin),True,(0,0,0),(255,255,255))
    bg = pygame.Surface((25,600),flags=pygame.HWSURFACE)
    bg2 = pygame.Surface((25,600),flags=pygame.HWSURFACE)#边框
    bg3 = pygame.Surface((950,25),flags=pygame.HWSURFACE)
    bg4 = pygame.Surface((950,25),flags=pygame.HWSURFACE)
    bg.fill(color='lightblue')
    bg2.fill(color='lightblue')
    bg3.fill(color='lightblue')
    bg4.fill(color='lightblue')
#---------------move---------------------
    if x == 50*fx-25 and y == 50*fy:
        fx += 0.5
    if x == 50*fx+25 and y == 50*fy:
        fx -= 0.5
    if y == 50*fy-25 and x == 50*fx:
        fy += 0.5
    if y == 50*fy+25 and x == 50*fx:#绿色方块不能上移      #已解决，变量名错误
        fy -= 0.5
#----------------------------------------
    screen.blit(image1,(x,y))
    screen.blit(bg,(0,0))
    screen.blit(bg2,(975,0))
    screen.blit(bg3,(25,0))
    screen.blit(bg4,(25,575))
    screen.blit(food,(50*fx,50*fy))
    screen.blit(door,(50*dx,50*dy))
    screen.blit(text,(25,25))
#----------------------------------------
    if dx == fx and dy == fy:
        fx = random.randint(3,18)
        fy = random.randint(3,10)
        dx = random.randint(3,18)
        dy = random.randint(3,10)
        coin += 1
    pygame.display.flip()