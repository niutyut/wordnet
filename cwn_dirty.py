from sqlite3 import connect
conn=connect('../cwn_dirty.sqlite')
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
pos='V' # N,V,A,D
wn_pos='v' # n,v,a,r
# begin with one sense (cwn_id) of a particular POS from cwn_pos table
#c.execute('select * from cwn_pos where pos = "'+pos+'"')
#c.execute('select * from cwn_pos where pos like "%'+pos+'%"')
c.execute('select * from cwn_pos')
processed_sense_ids=set()
for cwn_id,pos_sno,p in c.fetchall():
    sense_id=cwn_id[:8]
    lemma_id=cwn_id[:6]
    # fetch the lemma_type of this sense id from cwn_lemma table
    c.execute('select * from cwn_lemma where lemma_id="'+lemma_id+'"')
    cwn_lemma=c.fetchone()
    if cwn_lemma and sense_id not in processed_sense_ids:
        # omit meaning facets of this sense
        processed_sense_ids.add(sense_id)
        lemma_type=cwn_lemma[4].encode('utf-8')
        # fetch sense_def of this sense id from cwn_sense table
        c.execute('select * from cwn_sense where sense_id="'+sense_id+'"')
        cwn_sense=c.fetchone()
        if cwn_sense:
            sense_def=cwn_sense[2].encode('utf-8')
#            print wn_pos,
#            print p,
            print lemma_type,',',''.join(sense_def.split())
