from nltk.corpus import wordnet
noun=wordnet.all_synsets(pos='n').next()
print noun.name,noun.definition
verb=wordnet.all_synsets(pos='v').next()
print verb.name,verb.definition
adj=wordnet.all_synsets(pos='a').next()
print adj.name,adj.definition
adv=wordnet.all_synsets(pos='r').next()
print adv.name,adv.definition
