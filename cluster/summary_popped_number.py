i=count=0
lines=open('asbc_sense_clustering_hsieh.tsv').readlines()
while i<len(lines):
    line=lines[i].split()
    if line[0]<'a':
        print count
        count=1
    else:count+=1
    i+=1
