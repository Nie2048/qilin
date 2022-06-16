#定义各种剪切板文本操作方法

import pyperclip
import string
import text_option
from hello import h
import hello
hello.h.h()
text_option.count_words.count_words()
count_words.count_words()
input = pyperclip.paste()

text_option.count_characters()

hello.h

#判断剪贴板的内容是否和上一次不相同，是则返回TRUE，否则返回FALSE
def copy_notsame(input_data,old_input):
    if input_data != old_input:
        return True
    else:
        return False
