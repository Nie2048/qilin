#定义自定义脚本的运行方法

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