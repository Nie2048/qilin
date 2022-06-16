#定义win系统交互操作
import os
#打开exe文件,路径需要先经过/处理
#conmand = 'F:/1.software/Tencent/QQ/Bin/QQScLauncher.exe'
def OpenExe(conmand):
    for i in conmand[1:]:
        try:
            print('正在打开软件')
            i = str(i).replace('\\','/')
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
def cmd(conmand):
    for i in conmand[1:]:
        try:
            print('正在执行命令'+ i)
            os.system('chcp 65001')
            os.system(i)
        except:
            print('执行出现错误')

#定义自定义脚本的运行方法

# 读取py文件夹的python脚本并执行
def script(conmand):
    path = os.getcwd()
    current_path = path.replace("\\","/")
    for i in conmand[1:]:
        file_path =  current_path + '/py/'+ i 
        python_path = current_path + '/python_env/python.exe'
        conm = python_path +' ' + file_path
        try:
            print('正在打开'+ file_path)
            #exec(open(file_path,encoding='utf-8').read())
            os.system('chcp 65001')
            os.system(conm)
        except:
            print('执行文件{}\n 出现错误'.format(file_path))