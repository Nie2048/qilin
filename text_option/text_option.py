#定义各种剪切板文本操作方法

import pyperclip
import string

input = pyperclip.paste()

#判断剪贴板的内容是否和上一次不相同，是则返回TRUE，否则返回FALSE
def copy_notsame(input_data,old_input):
    if input_data != old_input:
        return True
    else:
        return False

#统计剪切板字数
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

#统计剪切板字符数
def count_characters(Clipboard_text):
    count = len(Clipboard_text)
    print("剪切板字符数为{}".format(count))

#定义一个删除指定字符串的函数
def del_ttr(Clipboard_text,str):
    input_data1 = Clipboard_text.replace(str,'')
    print('\n')
    print(input_data1)
    print('\n')
    return input_data1

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

# 将路径中的\替换为/                
def change(Clipboard_text):
        input_data1 = Clipboard_text.replace('\\','/')
        print('\n')
        print(input_data1)
        print('\n')
        return input_data1