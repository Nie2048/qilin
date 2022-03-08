#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个文本处理小程序
#import time
import pyperclip
import os
import yaml
import sys
import string

# 将路径中的\替换为/                
def change(Clipboard_text):
        input_data1 = Clipboard_text.replace('\\','/')
        print('\n')
        print(input_data1)
        print('\n')
        return input_data1

# current_path = "D:/1share/1item/Python/text_option"
path = os.getcwd()


current_path = change(path)
print('当前路径为'+current_path)
# os.chdir(sys.argv[0][:-14]) #打包成exe需要这句
# os.chdir(sys.argv[0][:-14])
#print(os.getcwd())
#sys.path.append(r'../py') #添加py文件夹路径，用于执行额外的py脚本

# os.chdir('D:/1share/1item/Python/text_option/')




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

#判断剪贴板的内容是否和上一次不相同，是则返回TRUE，否则返回FALSE
def copy_notsame(input_data,old_input):
    if input_data != old_input:
        return True
    else:
        return False

def count_words(Clipboard_text):
    count = 0
    for i in range(0,len(Clipboard_text)):
        if Clipboard_text[i] in string.ascii_letters:
            if i == (len(Clipboard_text)-1):
                count = count +1
            elif not Clipboard_text[i+1] in string.ascii_letters:
                count = count +1
            else:
                continue
        elif Clipboard_text[i].isalpha():
            count = count +1
        else:
            continue
    print("剪切板字数为{}".format(count))

def count_characters(Clipboard_text):
    count = len(Clipboard_text)
    print("剪切板字符数为{}".format(count))

#将内容中的大写替换为小写
def Up2Low(Clipboard_text):
    print('\n')
    print(Clipboard_text.lower())
    print('\n')
    return Clipboard_text.lower()

#将内容中的小写替换为大写
def Low2Up(Clipboard_text):
    print('\n')
    print(Clipboard_text.upper())
    print('\n')
    return Clipboard_text.upper()

#打开exe文件,路径需要先经过/处理
#input = 'F:/1.software/Tencent/QQ/Bin/QQScLauncher.exe'
def OpenExe(input):
    for i in input[1:]:
        try:
            print('正在打开软件')
            i = str(change(i))
            for b in range(1,len(i)):
                a = eval(str(-b))
                if i[a] == '/':
                    locate = a+1
                    break
                else:
                    continue
            software = i[locate:-4]
            conmand = 'start '+ '"{1}" "{0}"'.format(i,software)
            print(conmand)
            os.system('chcp 65001')
            os.system('@echo off')
            os.system(conmand)
        except:
            print('打开软件错误')

# 定义一个执行cmd脚本的命令
def cmd(input):
    for i in input[1:]:
        try:
            print('正在执行命令'+ i)
            os.system('chcp 65001')
            os.system(i)
        except:
            print('执行出现错误')

# 定义一个退出命令
def quite():
    exit()
 

# 读取py文件夹的python脚本并执行
def script(conmand):
    for i in conmand[1:]:
        file_path = current_path + '/py/'+ i 
        python_path = current_path + '/python_env/python.exe'
        conm = python_path +' ' + file_path
        try:
            print('正在打开'+ file_path)
            #exec(open(file_path,encoding='utf-8').read())
            os.system('chcp 65001')
            os.system(conm)
        except:
            print('执行文件{}\n 出现错误'.format(file_path))

# 定义复合指令解析
def combind_conmand(input):
    for i in input[1:]:
        conmand_analys(i)

#定义命令分流装置
def conmand_analys(input_conmand):
    if input_conmand in custome:
        c = custome[input_conmand]
        print('\n{}命令来自用户自定义\n 开始执行\n'.format(input_conmand))
    else:
        c = conmand[input_conmand]
        print('正在执行系统命令{}'.format(input_conmand))
    c0 = c[0]
    m = methonds[c0]
    if m in ('Clipboard'):
        input = pyperclip.paste()
        out = eval(c0+'(input)') #调用剪切板方法
        if out == None:
            out = out
        else:
            pyperclip.copy(str(out))
            print(out)
    elif m in ('cmd'):
        eval(c0+'(c)')
    elif m in ('without_input'):
        eval(c0+'()')  
    elif m in ('combind_conmand'):
        combind_conmand(c)
    else:
        print('暂时没有此功能，可向开发者反馈')

#定义一个循环，可以一直读取剪切板内容
def main():
    try:
        reload()
    except:
        print('文件路径为{}'.format(current_path))
        print('初始化失败')
        print('请检查后输入：reload进行重新载入')
    while True:
        input_conmand = input('请输入你想要进行的操作：')
        if input_conmand in ('reload','help','q'):
            eval(input_conmand+'()')
        else:
            if input_conmand in conmand:
                print('开始执行\n')
                conmand_analys(input_conmand)
            elif input_conmand in custome:
                print('开始执行\n')
                conmand_analys(input_conmand)
            else:
                print('\n暂时没有此功能，可向开发者反馈,或者检查配置文件。\n')

main()


