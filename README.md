Chinese Wordnet 的 Python NLTK 模組
======
先安裝 NLTK WordNet 模組 (http://nltk.org)

請 clone 本資料夾後覆蓋到 nltk_data/corpora 即可使用

取得第一個詞意：
from nltk.corpus import wordnet

wordnet.all_synsets()[0].definition   #nltk 2.0

wordnet.all_synsets()[0].definition() #nltk 3.0

CKIP 中研院斷詞服務
======
請自行申請帳號 (http://ckipsvr.iis.sinica.edu.tw) 並寫入 ckip.py

from ckip import seg

username='your username'

password='your password'

詞意相似度計算
======
from test import similar

similar(seg(def1),seg(def2))
