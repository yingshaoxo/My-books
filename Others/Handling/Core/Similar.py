from difflib import SequenceMatcher 
from difflib import get_close_matches


def similar(a, b): 
    return SequenceMatcher(None, a, b).ratio()
    #.quick_ratio()
    #.real_quick_ratio()
    
def match(word, a_list):
    result = get_close_matches(word, a_list, 1)
    if len(result) == 0:
        return ''
    else:
        return result

           
def max_close(word, a_list):
    max = [0,0.0]
    min = [0,0.0]

    for num, text in enumerate(a_list, start=0):
        similarity = similar(word, a_list[num])
        #print(similarity,'\n')
        if similarity > 0:
            if similarity > max[1]:
                max[1] = similarity
                max[0] = num
            elif similarity < min[1]:
                min[1] = similarity
                min[0] = num
    
    print('max: {}\n'.format(max[1]))
    #print(max[0])
    print(a_list[max[0]])
    return a_list[max[0]]
    
    if min[1] > 0:
        print('\n\n', '-'*10, '\n\n')
        print('min: {}\n\n'.format(min[1]))
        #print(min[0])
        print(a_list[min[0]])


def split_txt(dirname):
    import re
    try:
        with open(dirname, 'r',  encoding='utf-8', errors='replace') as f:
            text = f.read()
    except Exception as e:
        print(e)
        print('We only support UTF_8!')
                
    result = text.split('\n\n' + '——————————————' + '\n\n')	
    if result == [text]:
        result = text.split('\n')
    result = [i for i in result if re.match(r'^\s*$', i) == None]

    return result


a_list = split_txt('/sdcard/历史.txt')
#a_list = ['我爱','我想','我做']
word = '重在坚持'
max_close(word, a_list)

#print(match(word, a_list))
