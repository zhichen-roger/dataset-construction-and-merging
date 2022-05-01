import re
import xlwt
from stanfordcorenlp import StanfordCoreNLP
import os
osfile = []
dir = r"F:\pythonbert\demo\untitled1\extract\extracttxt"
for root, dirs, files in os.walk(dir):
    for file in files:
        if file != 'extract.py' and file != '__init__.py' and file !='split.py' and file !='Label.py' and file !='CSV.py':
            osfile.append(file)
for index in range(len(osfile)):
    nlp = StanfordCoreNLP('E:\stanford\stanford-corenlp-latest\stanford-corenlp-full-2021-01-09', lang='en')
    sentence = []
    key = []
    substance = []
    time = []
    location =[]
    Dict = []
    k = 0
    num = 0
    # 分字典存储
    with open(osfile[index], "r", encoding="utf-8") as f:
        lines = f.readlines()
        # 去除换行符
        result = ([x.strip() for x in lines if x.strip() != ''])
        # 将整理好字典提取成为全局字典
        for x in result:
            Dict.append(x)
    for k in range(len(Dict)-int(len(Dict) % 5)):
        if num == 1:
           key.append(Dict[k][11:])
        elif num == 2:
           substance.append(Dict[k][11:])
        elif num == 3:
           time.append(Dict[k][6:])
        elif num == 4:
           location.append(Dict[k][10:])
        else:
            num = 0
            sentence.append(Dict[k])
        num += 1
    # print("sentence:", sentence)
    # print("substance", substance)
    # print("time:", time)
    # print("location:", location)
    # 将每句话切成单个单词并写入excel
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('test','w+r')
    sentencesub = []
    substancesub = []
    timesub = []
    locationsub = []
    nlpsub = []
    for i in range(len(sentence)):
        for j in range(0,len(nlp.pos_tag(sentence[i]))):
            nlpsub.append(nlp.pos_tag(sentence[i])[j][1])
        nlpsub.append('.')
        #sentencesub.append(sentence[i].replace(","," ,").replace("-"," - ").split(" "))
        sentencesub.append(nlp.word_tokenize(sentence[i]))
        substancesub.append(substance[i].replace(",","").split(" "))
        timesub.append(time[i].replace(",","").split(" "))
        locationsub.append(location[i].replace(",","").split(" "))
    nlp.close()
    for i in range(len(nlpsub)):
        worksheet.write(i,2,nlpsub[i])
    flag = 0
    sentencelabel = []
    sublabel = []
    for j in range(len(sentencesub)):
        worksheet.write(flag,0,"Sentence")
        for i in range(len(sentencesub[j])):
            sentencelabel.append(sentencesub[j][i])
            worksheet.write(flag,1,sentencesub[j][i])
            sublabel.append("O")
            worksheet.write(flag, 3, "O")
            flag+=1
        sentencelabel.append('.')
        worksheet.write(flag,1,'.')
        sublabel.append('O')
        worksheet.write(flag, 3, 'O')
        flag += 1

    flagsub = 0
    flagtim = 0
    flagloc = 0
    lensentence = 0
    for j in range(len(sentencesub)):
        for i in range(len(sentencesub[j])):
            for sub in range(len(substancesub[j])):
                if sentencesub[j][i]==substancesub[j][sub]:
                    flagsub = i + lensentence
                    sublabel[flagsub] = 'B-nat'
                    if sublabel[flagsub-1]=='B-nat':
                        sublabel[flagsub] = 'I-nat'
                    worksheet.write(flagsub , 3 , sublabel[flagsub])
            for tim in range(len(timesub[j])):
                if sentencesub[j][i]== timesub[j][tim]:
                    flagtim = i + lensentence
                    sublabel[flagtim] = 'B-tim'
                    if sublabel[flagtim-1]=='B-tim':
                        sublabel[flagtim] = 'I-tim'
                    worksheet.write(flagtim , 3 , sublabel[flagtim])
            for loc in range(len(locationsub[j])):
                if sentencesub[j][i]== locationsub[j][loc]:
                    flagloc = i + lensentence
                    sublabel[flagloc] = 'B-geo'
                    if sublabel[flagloc-1]=='B-geo':
                        sublabel[flagloc] = 'I-geo'
                    worksheet.write(flagloc , 3 , sublabel[flagloc])
        lensentence +=len(sentencesub[j])+1
    workbook.save(osfile[index].split('.')[0]+'.xls')
    print("work done")


