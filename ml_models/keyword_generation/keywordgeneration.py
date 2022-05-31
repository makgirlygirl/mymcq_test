import pprint
import itertools
import re
import pke
import string
from nltk.corpus import stopwords
class KeywordGenerataion():
    def __init__(self):
        self.extractor = pke.unsupervised.MultipartiteRank()
        self.pos = {'PROPN'}
        self.stoplist = list(string.punctuation)
        self.stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
        self.stoplist += self.stopwords.words('english')
    def generate(self, full_txt):
        keyword=[]
        self.extractor.load_document(input=full_txt, stoplist=self.stoplist)
        self.extractor.candidate_selection(pos=self.pos)
        self.extractor.candidate_weighting(alpha=1.1,
                                    threshold=0.75,
                                    method='average')
        keyphrases = self.extractor.get_n_best(n=20)

        for key in keyphrases:
            keyword.append(key[0])

        return keyword