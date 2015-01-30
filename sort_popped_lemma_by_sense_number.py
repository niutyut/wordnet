i=0
lines=open('popping.csv').readlines()
while i<len(lines)-1:
    s1,s2=lines[i],lines[i+1]
    print s1.split()[0]
    print s2.split()[0]
    i+=2
