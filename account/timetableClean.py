# -*- coding: utf-8 -*-

timetable=["","","","",""]


#whole_str="1교시 매체 미술 (우영주) 분반:1/강의실:미술실	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정	프로그래밍 (정윤희) 분반:1/강의실:멀티미디어실	에너지환경과학 (박찬규) 분반:2/강의실:A304 2교시 매체 미술 (우영주) 분반:1/강의실:미술실	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정	프로그래밍 (정윤희) 분반:1/강의실:멀티미디어실	에너지환경과학 (박찬규) 분반:2/강의실:A304 3교시 수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	심리학 (홍순율) 분반:2/강의실:B404	통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	고전역학 (정형식/유상미) 분반:2/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정 4교시 수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	심리학 (홍순율) 분반:2/강의실:B404	통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	고전역학 (정형식/유상미) 분반:2/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정 5교시 고전역학 (정형식/유상미) 분반:2/강의실:B401	에너지환경과학 (박찬규) 분반:2/강의실:A304	수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401	스포츠 생활(남) (황진령/김현진) 분반:7/강의실:3층대강의실 6교시 통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	에너지환경과학 (박찬규) 분반:2/강의실:A304	수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	매체 미술 (우영주) 분반:1/강의실:미술실	스포츠 생활(남) (황진령/김현진) 분반:7/강의실:3층대강의실 7교시 통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	고전역학 (정형식/유상미) 분반:2/강의실:B401		매체 미술 (우영주) 분반:1/강의실:미술실	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401"
whole_str = "1교시 매체 미술 (우영주) 분반:1/강의실:미술실	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정	프로그래밍 (정윤희) 분반:1/강의실:멀티미디어실	에너지환경과학 (박찬규) 분반:2/강의실:A304 2교시 매체 미술 (우영주) 분반:1/강의실:미술실	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정	프로그래밍 (정윤희) 분반:1/강의실:멀티미디어실	에너지환경과학 (박찬규) 분반:2/강의실:A304 3교시 수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	심리학 (홍순율) 분반:2/강의실:B404	통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	고전역학 (정형식/유상미) 분반:2/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정 4교시 수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	심리학 (홍순율) 분반:2/강의실:B404	통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	고전역학 (정형식/유상미) 분반:2/강의실:B401	공강(4단위)1 () 분반:6/강의실:미정 5교시 고전역학 (정형식/유상미) 분반:2/강의실:B401	에너지환경과학 (박찬규) 분반:2/강의실:A304	수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401	스포츠 생활(남) (황진령/김현진) 분반:7/강의실:3층대강의실 6교시 통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	에너지환경과학 (박찬규) 분반:2/강의실:A304	수학세미나Ⅰ (박성훈) 분반:1/강의실:A303	매체 미술 (우영주) 분반:1/강의실:미술실	스포츠 생활(남) (황진령/김현진) 분반:7/강의실:3층대강의실 7교시 통합수학Ⅰ (이문호/허보람) 분반:1/강의실:B403	고전역학 (정형식/유상미) 분반:2/강의실:B401		매체 미술 (우영주) 분반:1/강의실:미술실	응용물리학탐구 (정형식/유상미) 분반:1/강의실:B401"
time_cnt = 0

subline=[[],[],[],[],[],[],[]]

t_split = whole_str.split("\t")

t_split.remove('')

subs_whole = []
push=""
for i, el in enumerate(t_split):
    if i%3==1:
        continue

    if i%3==0:
        push=el
    
    elif i%3==2:
        push+="  "+el.split(":")[2]
        subs_whole.append(push)
        push=""

DB_class =[[0,1,2,3,4],[0,1,3,4]]

for i, el in enumerate(subs_whole):
    p=(i//5)//6

    timetable[DB_class[p][i%5]]+="/"+el

DB_date={"월":0,"화":0,"수":0,"목":0,"금":0}
date = input()
date_num = DB_date[date]

print(timetable[date_num][1:])
print(timetable)
#return timetable