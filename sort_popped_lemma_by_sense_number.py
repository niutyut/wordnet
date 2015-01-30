i=0
for line in open('popped_debug_CWNMOE_asbc_100.csv'):
    
lines=open('popping_debug_CWNMOE_asbc.csv').readlines()
while i<len(lines)-1:
    s1,s2=lines[i],lines[i+1]
    i+=2
