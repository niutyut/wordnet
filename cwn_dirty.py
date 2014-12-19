from sqlite3 import connect
conn=connect('cwn_dirty.sqlite')
c=conn.cursor()

def lookup_pos(lemma_id):
    c.execute('select * from cwn_pos where cwn_id like "%'+lemma_id+'%"')
    cwn_pos=c.fetchone()
    pos=cwn_pos[2]
    return pos

def lookup_lemma(lemma_id):
    c.execute('select * from cwn_lemma where lemma_id="'+lemma_id+'"')
    cwn_lemma=c.fetchone()
    lemma_type=cwn_lemma[4].encode('utf-8')
    return lemma_type

def lookup_sense(lemma_id):
    c.execute('select * from cwn_sense where lemma_id="'+lemma_id+'"')
    cwn_sense=c.fetchone()
    sense_def=cwn_sense[2].encode('utf-8')
    return sense_def

print lookup_pos('080601')
print lookup_lemma('080601')
print lookup_sense('080601')
c.execute('select * from cwn_pos')
for cwn_pos in c.fetchall():
    pos=cwn_pos[2]
    print pos
