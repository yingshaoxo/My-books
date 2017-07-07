import requests
import re


def _get(text):
    _list = re.findall('[^"。！？…]{5,}[。！？…]', text, re.L)
    end_list = []
    for num, i in enumerate(_list, start=1):
        if num/2 == int(num/2):
            end_list.append(i)
    return end_list

def translate(text):
    r = requests.post('https://translate.google.cn/translate_a/single?client=at&sl=en&tl=zh-CN&hl=zh-CN&dt=at&ie=UTF-8&oe=UTF-8&q='\
                              + text)
    result = _get(r.text)
    return result

#https://translate.google.cn/translate_a/single?client=at&sl=en&tl=zh-CN&hl=zh-CN&dt=at&ie=UTF-8&oe=UTF-8&q=sure
text = '''Right now your dad and I have been married for about two years, living on Ellis Avenue; when we move out you'll still be too young to remember the house
'''
print(translate(text))
