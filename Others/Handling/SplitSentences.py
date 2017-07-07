import re


def list_to_text(_list, num_of_line):
    text = ''
    for num, i in enumerate(_list, start=1):
        if num % num_of_line != 0:
            text += i + '\n'
        else:
            text += i + '\n\n'
    return text

def OT(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　'):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　'):#right
        text = text[:-1]
    return text

def handle(obj):
    text = obj.group(0)
    text = OT(text)
    return text + '\n'*2
    
def split_sentence(text):
    text = re.sub(r'((.*?)(?<!B|A)([!?.] ) ?)', handle, text)
    a_list = text.split('\n')
    a_list = [OT(i) for i in a_list if re.match(r'^\s*$', i) == None] 
    text = list_to_text(a_list, 1)
    return text


text = '''
A
Music
Opera at Music Hall: 1243 Elm Street. The season runs June through August, with additional performances in March and September. The Opera honors Enjoy the Arts membership discounts. Phone: 241-2742. http://www.cityopera.com.
Chamber Orchestra: The Orchestra plays at Memorial Hall at 1406 Elm Street, which offers several concerts from March through June. Call 723-1182 for more information. http://www.chamberorch.com.
Symphony Orchestra: At Music Hall and Riverbend. For ticket sales, call 381-3300. Regular season runs September through May at Music Hall in summer at Riverbend. http://www.symphony.org/home.asp.
College Conservatory of Music(CCM): Performances are on the main campus(校园) of the university, usually at Patricia Cobbett Theater. CCM organizes a variety of events, including performances by the well-known LaSalle Quartet, CCM's Philharmonic Orchestra, and various groups of musicians presenting Baroque through modern music. Students with I.D. cards can attend the events for free. A free schedule of events for each term is available by calling the box office at 556-4183. http://www.ccm.uc.edu/events/calendar.
Riverbend Music Theater: 6295 Kellogg Ave. Large outdoor theater with the closest seats under cover (price difference).Big name shows all summer long! Phone: 232-6220. http://www.riverbendmusic.com.
'''
print(split_sentence(text))