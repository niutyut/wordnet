for line in open('CWNMOE-def-ex.csv').readlines():
    lemma,definition,example=line.split(',')
    print lemma.strip('"'),
    print definition.strip('"').strip(),
    print example.strip().strip('"').strip()
