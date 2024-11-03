#!/usr/bin/env python
# coding: utf-8


# In[0]:

from makeChasuFile import chasuMan

# chasuMan()

meet = chasuMan()
meetNo = meet.iloc[0,0]
meetDate = meet.iloc[0,1]
meetNum = meet.iloc[0,2]
meetPW = meet.iloc[0,3]
meetURL = meet.iloc[0,4]


print(meetNo)
print(meetDate)
print(meetNum)
print(meetPW)
print(meetURL)

# In[1]:


import re
def find_tag(file_path):
    file = open(file_path, encoding='euckr')
    text_ori = file.read()
    menu = '1'
    while (menu!='Q')&(menu!='q'):
        menu = input('''***************************************************************************
메뉴를 입력해주세요
1. 태그 수정
2. 저장 후 종료
q. 종료\n***************************************************************************\n''').strip()
        if menu=='1':
            tag_names = ['p','span','p','p','p']
            tag_ids = ['kyocha','kyoill','meetid','meetpw','meeturl']
            modified_tags = [f'''- 교육명  : [DT] 코딩 실습 입문 과정 : SW트랙 {meetNo}차수''',
                             f'''{meetDate}, 08:00~17:00''',
                             f'''<p style="margin: 13px 0;">2. 회의ID : {meetNum}</p>''',
                             f'''<p style="margin: 13px 0;">3. 회의PW : {meetPW}</p>''',
                             f'''<p style="margin: 13px 0;">4. 회의URL : {meetURL}</p>''']
            for tag_index in range(5):
                tag_name = tag_names[tag_index]
                tag_id = tag_ids[tag_index]
                modified_tag = modified_tags[tag_index]
                index_start = [m.start() for m in re.finditer(f'<{tag_name.lower()}[>\s]|<{tag_name.upper()}[>\s]', text_ori)]
                if len(index_start):
                    for i in index_start:
                        pattern = re.compile(f'</{tag_name.lower()}[\s]*>|</{tag_name.upper()}[\s]*>')
                        res = pattern.search(text_ori[i:])
                        pattern2 = re.compile(f'id[\s]*=[\s]*[\'"]{tag_id}[\'"]')
                        res2 = pattern2.search(text_ori[i:i+res.end()])
                        if res2:
                            text_ori = text_ori[:i]+modified_tag+text_ori[i+res.end():]
                            break
                else:
                    print('찾으시는 태그가 존재하지 않습니다.')
        if menu=='2':
            temp_name = input('***************************************************************************\n새로 저장할 파일의 이름을 정해주세요\n')

            if temp_name.endswith('.html'):
                modified_path = temp_name
                modi = str(os.path.abspath("./forMail"))
            else:
                modified_path = temp_name+'.html'
                modi = str(os.path.abspath("./forMail"))
            with open(f"{modi}/{modified_path}", "w", encoding='euckr') as file:
                file.write(text_ori)
                print(f'***************************************************************************\n"{modified_path}" 파일이 생성되었습니다.\n')
                menu='q'
    print('작업을 종료합니다.')
    return
find_tag('입과안내메일양식_ver4.html')



# %%
