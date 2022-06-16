import pyperclip

def hello():
    print("调用外部模块成功\n hello world!\n")

def sortA_Z():
    import pyperclip
    input = pyperclip.paste()
    output = sorted(input.split())
    print(output)
    pyperclip.copy(str(output)[2:-2])

def hello2():
    print("调用外部脚本成功\n ！！！！！！！!\n")