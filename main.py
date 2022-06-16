#!/usr/bin/env python
# -*- coding: utf-8 -*-

#命令分流器

#import time
import pyperclip
import os
import yaml
from selfmode import Clipboard
from selfmode import sys

# 将路径中的\替换为/                
def change(Clipboard_text):
        input_data1 = Clipboard_text.replace('\\','/')
        print('\n')
        print(input_data1)
        print('\n')
        return input_data1

#os.chdir('D:/1share/1item/Git_repository/qilin')
path = os.getcwd()

current_path = change(path)
print('当前路径为'+current_path)
# os.chdir(sys.argv[0][:-14]) #打包成exe需要这句
# os.chdir(sys.argv[0][:-14])
#print(os.getcwd())
#sys.path.append(r'../py') #添加py文件夹路径，用于执行额外的py脚本

def welcome():
    welcome_doc = open(current_path+'/doc/welcome.txt','r',encoding="utf-8")
    custome_doc = open(current_path+'/doc/custome.txt','r',encoding="utf-8")
    for i in welcome_doc.readlines():
        print(i)
    welcome_doc.close()
    for i in custome_doc.readlines():
        print(i)
    custome_doc.close()

#重新加载配置文件
conmand = {}
methonds = {}
custome = {}
def reload():
    global conmand
    global methonds
    global custome
    print('正在读取配置文件\n')
    with open(current_path + '/conmand.yml',encoding="utf-8") as file:
        conmand = yaml.full_load(file) ##命令字典
    with open(current_path+'/methond.yaml',encoding="utf-8") as file:
        methonds = yaml.full_load(file) ##方法字典
    with open(current_path+'/custome.yml',encoding="utf-8") as file:
        custome = yaml.full_load(file) ##方法字典 
    print('配置文件读取成功\n')
    welcome()



def help():
    help_doc = open(current_path+'/doc/help.txt','r',encoding="utf-8")
    for i in help_doc.readlines():
        print(i)
    help_doc.close()

# 定义一个退出命令
def quite():
    exit()
 
# 定义复合指令解析
def combind_conmand(input):
    for i in input[1:]:
        conmand_analys(i)

#判断命令的来源，及执行方法
def select_methond(input_conmand):
    if input_conmand in custome:
        c = custome[input_conmand]
        print('\n{}命令来自用户自定义\n 开始执行\n'.format(input_conmand))
    else:
        c = conmand[input_conmand]
        print('正在执行系统命令{}'.format(input_conmand))
    return c

#Clipboard方法命令解析器
def cipboard_parser(c):
    input = pyperclip.paste()
    out = eval('Clipboard.'+c[0]+'(input)') #调用剪切板方法，引入text_option.py模块
    if out == None:
        out = out
    else:
        pyperclip.copy(str(out))
        print(out)

#sys方法命令解析器
def sys_parser(c):
    try:
        print("正在执行cmd命令")
        eval('sys.'+c[0]+'(c)')
    except:
        print("执行cmd命令失败")


#定义命令分流装置
def conmand_analys(input_conmand):
    #conmand
    c = select_methond(input_conmand)
    #methonds
    m = methonds[c[0]]
    if m in ('Clipboard'):
        cipboard_parser(c)
    elif m in ("sys"): #
        sys_parser(c)
    elif m in ('combind_conmand'):
        combind_conmand(c)
    else:
        print('暂时没有此功能，可向开发者反馈')

#定义初始化函数
def initial():
    try:
        reload()
        print('初始化完成')
    except:
        print('文件路径为{}'.format(current_path))
        print('初始化失败')
        print('请检查后输入：reload进行重新载入')

#定义一个循环，可以一直读取用户输入
def main():
    initial()
    meta_conmand = ['reload','help','q', 'welcome']
    while True:
        input_conmand = input('请输入你想要进行的操作：')
        if input_conmand in (meta_conmand):
            eval(input_conmand+'()')
        else:
            #执行预先定义的快捷命令
            if (input_conmand in conmand) or (input_conmand in custome):
                print('开始执行快捷命令\n')
                try:
                    conmand_analys(input_conmand)
                except:
                    print("解析快捷命令出错")
            else:
                #解析用户输入的命令
                print('没有找到快捷命令\n 开始解析用户输入的命令(等待开发)\n')


main()