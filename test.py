#-*-coding:utf8-*-
from nltk.corpus import wordnet
from ckip import seg

def similar(seg_def1,seg_def2):
    sum=0
    for w in seg_def1:
        if w in seg_def2:sum+=1
    return sum

if __name__=='__main__':
#    synsets=list(wordnet.all_synsets())
 #   def1=seg(synsets[0].definition)
  #  def2=seg(synsets[1].definition)
   # print ' '.join(def1),' '.join(def2),similar(def1,def2)
    moedict=['皮肉破損的地方。','姓。如春秋時宋國有傷省。','受傷、使受傷。','耗損、毀壞。','妨礙。','毀謗。','悲痛，使憂心悲痛。']
    moedict=[seg(moe)[:-1] for moe in moedict]
    cwndict=[seg(synset.definition)[:-1] for synset in wordnet.synsets('傷')]
    for moe in moedict:
        print ' '.join(moe)
        for cwn in cwndict:
            print ' '.join(cwn),
            print similar(moe,cwn)
        print
