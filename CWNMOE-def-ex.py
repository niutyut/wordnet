for line in open('CWNMOE-def-ex.csv').readlines():
    lemma,definition,example=line.split(',')
    print lemma.strip('"'),definition.strip('"').strip(),example.strip().strip('"').strip()
