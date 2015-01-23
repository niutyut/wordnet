from __future__ import division
from Jseg import jieba

def lesk(example,kwic):
    return len([w for w in example if w in kwic])/min(len(example),len(kwic))

kwics=[]
stopwords=[w for w in open('stopwords.csv').read().split()]
for line in open('lemma_definition_example.csv').readlines():
#    print '\n'.join(line.split(','))
#    print line
    if len(line.split(','))==3:
        lemma,definition,example=line.split(',')
        print lemma,',',definition,',',#example.strip()
        segmented=jieba.seg(example.strip()).nopos().split()
        for w in segmented:
            if w.encode('utf-8') not in stopwords:print w.encode('utf-8'),
        print
'''
    for kwic in kwics:
        if lesk(example,kwic)>.5:
            print lemma,definition,''.join(kwic)
'''
