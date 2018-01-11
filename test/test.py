# -*- coding: utf-8 -*-
__author__ = 'wenyunlong'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from gensim.models import Word2Vec


#模型的加载
model = Word2Vec.load('../data/zh.bin')
print(model.most_similar(u'老师'))