#定义一个删除指定字符串的函数
Clipboard_text = "你好，\n 我是 \n 谁？ "

print(Clipboard_text)

def del_ttr(Clipboard_text,str):
    input_data1 = Clipboard_text.replace(str,'')
    print('\n')
    print(input_data1)
    print('\n')
    return input_data1

del_ttr(Clipboard_text,'\n')