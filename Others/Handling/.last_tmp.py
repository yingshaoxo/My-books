import re

virsion = str(0)
if virsion == '0':
    virsion = ''
book = '/sdcard/王者文件夹/My-books/Others/Handling/American Situational Conversations.txt'
book2 = book.replace('.txt', virsion+'.txt')
with open(book2, 'r', encoding='utf-8') as f:
    text = f.read()


line = '\n\n' + '——————————————' + '\n\n'
#do something in here
all_list = text.split(line)
new_l = []
for i in all_list:
    t = i.split('\n')
    t[1] += '\n'
    new_l.append('\n'.join(t))
all_list = new_l
text = line.join(all_list)
#text = text.replace('', '')
#text = text[:-len(line)]
#text = text.strip('  　\n ')
print(text)
#do something in here


if virsion == '':
    virsion = '0'
book2 = book.replace('.txt', str(int(virsion)+1)+'.txt')
with open(book2, 'w', encoding='utf-8') as f:
    f.write(text)