top100=list()
for line in open('sorted_popped_debug_CWNMOE_asbc_lemmas.csv').readlines()[:100]:
    lemma=line.split()[0][1:-1]
    top100.append(lemma)

i=0
lines=open('popping_debug_CWNMOE_asbc.csv').readlines()
while i<len(lines)-1:
    s1,s2=lines[i],lines[i+1]
    if s1.split()[0] in top100:
        print s1.strip()
        print s2.strip()
    i+=2
