#定义win系统交互操作
import sys
import os
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
