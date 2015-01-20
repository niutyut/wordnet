Chinese Wordnet 的 SQLite 資料庫
======
資料檔位於 http://lope.linguistics.ntu.edu.tw/cwnvis/data/cwn_dirty.sqlite

主要有三個資料表：
<ol>
<li>cwn_lemma: 記錄 6 碼的 lemma_id 以及 lemma_type
<li>cwn_sense: 在原 lemmaid 擴增 2 碼成為 8 碼的 sense_id，以及 sense_def
<li>cwn_goodSynset: 記錄 synset member 的 sense_id
</ol>

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
