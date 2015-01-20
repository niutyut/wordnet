cwn_dict={}
for line in open('cwn_dirty.tsv').readlines():
    lemma_type,sense_def=line.split()
    if lemma_type not in cwn_dict:cwn_dict[lemma_type]=[sense_def]
    else:cwn_dict[lemma_type].append(sense_def)

moe_dict={}
for line in open('dict-revised.tsv').readlines():
    if len(line.split())<>2:print line
#    title,definition=line.split()
#    if lemma_type not in moe_dict:moe_dict[lemma_type]=[sense_def]
 #   else:moe_dict[lemma_type].append(sense_def)

