from __future__ import division
from numpy import dot
from math import sqrt

def lesk(example,kwic):
    return len([w for w in example if w in kwic])/min(len(example),len(kwic))

def cos_similar(v1,v2):
    len1=sum([i**2 for i in v1])
    len2=sum([i**2 for i in v2])
    d=dot(v1,v2)
    if d>0:return d/sqrt(len1)/sqrt(len2)
    return 0

plurks=[plurk.strip() for plurk in open('asbc.txt')]

d=dict() # {lemma:{definition:[lesk]}}
for line in open('CWNMOE-def-ex.csv').readlines():
#for line in open('CWNMOE-def-ex.csv').readlines()[2989:2993]:
    lemma,definition,example=line.split(',')
    lemma,definition,example=lemma.strip('"'),definition.strip('"').strip(),example.strip().strip('"').strip()
    example_words=example.split()
    flag=1
    vector=[]
    for plurk in plurks:
        plurk_words=plurk.split()
        if lemma in plurk_words:
            vector.append(lesk(example_words,plurk_words))
            if lemma not in d:d[lemma]={definition:[lesk(example_words,plurk_words)]}
            elif definition not in d[lemma]:d[lemma][definition]=[lesk(example_words,plurk_words)]
            else:d[lemma][definition].append(lesk(example_words,plurk_words))
            flag=0
#    if flag:d[lemma]={definition:[0]}

eval_matrix={} # {lemma:[[def1,history,...],[def2,history,...]]}
for lemma in d:
    for definition in lemma:
        if lemma not in eval_matrix:eval_matrix[lemma]=[[definition]]
        else:eval_matrix[lemma].append([definition])

#for lemma in eval_matrix:
 #   for definition in eval_matrix[lemma]:print lemma,definition

for lemma in d:
    i=0
    while i<len(d[lemma].keys()):
        defi=d[lemma].keys()[i]
#        print lemma,defi

#        if lemma not in eval_matrix:eval_matrix[lemma]=[[defi]]
 #       else:eval_matrix[lemma].append([defi])

        j=0
        while j<i and j<len(d[lemma].keys()) and i<len(d[lemma].keys()):
            def1,def2=d[lemma].keys()[i],d[lemma].keys()[j]
            v1,v2=d[lemma][def1],d[lemma][def2]
            if len(v1)==len(v2):
                if cos_similar(v1,v2)>.5:
#                    print lemma,def1
 #                   print lemma,def2
                    k=0
                    for k in range(len(eval_matrix[lemma])):
                        if eval_matrix[lemma][k][0]==def1:
                            eval_matrix[lemma][k].append(def2)
                        elif eval_matrix[lemma][k][0]==def2:
                            eval_matrix[lemma].pop(k)

                    eval_matrix[lemma]
                    d[lemma].pop(def1)
                    if i<len(d[lemma].keys()):continue
                else:j+=1
            else:j+=1
        i+=1

#for lemma in d:
 #   for definition in d[lemma]:print lemma,definition

for lemma in eval_matrix: # {lemma:[[def1,history,...],[def2,history,...]]}
    for defis in eval_matrix[lemma]:
        if len(defis)>1:
            print defis[0],',',defis[0]
            for defi in defis[1:]:print defi

