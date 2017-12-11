text = ''' 义和团运动失败的根本原因是农民阶级的局限性，具体
表现为提不出正确的指导思想，缺乏统一的领导，没有
科学的革命纲领，斗争方式落后。

对义和团运动既不能一味的肯定，也不能一味的否定，

要辩证地看待。义和团运动一方面阻止了列强瓜分中
国阴谋的实现，另一方面也带有盲目的排外性质。

义和团运动从革命史角度看，是一场反帝爱国运动，阻
止了列强瓜分中国阴谋的实现；从近代化角度看，它盲
目排外，具有落后性。
'''

import re


def handle(obj):
    text = obj.group(0)
    if re.match(r'^\s+$', text)==None:
        return re.sub(r'\s*', '', text)
    else:
        return text
    
def fix(text):
    text = re.sub(r'[^。！？…；：”"）》】]\s+', handle, text)
    return text
    

path = '/storage/emulated/0/王者文件夹/我的文档/学习探索/全球通史pdf.txt'
with open(path, 'r',  encoding='utf-8', errors='replace') as f:
    text = f.read()
    
#print(text, '\n'*3)
text = #fix(text)

with open(path.replace('.txt', '1.txt'), 'w',  encoding='utf-8', errors='replace') as f:
    f.write(text)    