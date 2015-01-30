i=0
lines=open('manual_evaluate_popping_asbc_with_100_original_rich.csv').readlines()
current=lines[1].strip()
print current,',',current
while i<len(lines):
    s1=lines[i].strip()
    s2=lines[i+1].strip()
    if s2==current:print s1
    else:
        current=s2
        print current,',',current
    i+=2
