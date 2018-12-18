import os

with open('Super Student.txt', 'r', encoding='gbk') as f:
    t = f.read()

with open('fuck.txt', 'w', encoding='utf-8') as f:
    f.write(t)

