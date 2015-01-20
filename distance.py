#-*-coding:utf8-*-
from Levenshtein import distance

cwn_dict={}
for line in open('cwn_dirty.csv').readlines():
    lemma_type,sense_def=line.split(',')
    lemma_type,sense_def=lemma_type.strip(),sense_def.strip()
    if lemma_type not in cwn_dict:cwn_dict[lemma_type]=[sense_def]
    else:cwn_dict[lemma_type].append(sense_def)

moe_dict={}
for line in open('dict-revised.csv').readlines():
    title,definition=line.split(',')
    title,definition=title.strip(),definition.strip()
    if title not in moe_dict:moe_dict[title]=[definition]
    else:moe_dict[title].append(definition)

sense_list=[]
for word in cwn_dict:
    if word in moe_dict:
        print 'cwn:'
        for cwn_sense in cwn_dict[word]:
            sense_list.append(cwn_sense)
            print cwn_sense
        print 'moe:'
        for moe_sense in moe_dict[word]:
      #          if distance(cwn_sense,moe_sense)<12: #,'cwn:',cwn_sense,'moe:',moe_sense
            print moe_sense
        break
