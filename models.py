#%%
from keybert import KeyBERT  # # 키워드
from summarizer import Summarizer  # # 요약문장
from transformers import pipeline  # # 중심문장
from nltk.corpus import wordnet as wn ## 유의어 반의어

#%% test
f = open("/home/mymcq/testset/1.txt","r")
full_text = f.read()
#%% 중심문장
class KeysentenceGenerator():
    def __init__(self):
        self.model=pipeline("summarization", model="facebook/bart-large-cnn")
    def generate(self, full_text, max_length=20, min_length=0, do_sample=False):
        key_text=self.model(full_text, max_length=max_length, min_length=min_length,do_sample=do_sample)
        # list->dict->str
        return key_text[0]['summary_text']

#%% 요약문장
class SummerizerGenerator():
    def __init__(self):
        self.model = Summarizer()
    def generate(self, full_text, min_length=0, max_length=20, num_sentence=1):
        result = self.model(full_text, 
                            min_length=min_length, max_length = max_length ,
                            num_sentences = num_sentence)

        summarized_text = ''.join(result)
        return summarized_text
#%%
# text2text_generator = pipeline("text2text-generation")
# a=text2text_generator("question: What is 42 ? context: 42 is the answer to life, the universe and everything")
# print(a)
#%% 키워드
class KeywordGenerator():
    def __init__(self):
        self.model=KeyBERT()
    def generate(self, full_text):
        keyword=self.model.extract_keywords(full_text)
        ## list
        return keyword
#%%
'''
유의어 반의어 어떤걸로할지 정하기 !!'''
#%% 유의어
class SynonymsGenerator():
    def __init__(self):
        pass
    def generate(self, word):
        s_list=[]
        ## wn.synsets(sord: 단어.품사.그룹인덱스)
        for synsets in wn.synsets(word):
            s_list.extend(synsets.lemma_names())
        s_list=list(dict.fromkeys(s_list))## 중복 제거
        return s_list
# %% 반의어
class AntonymsGenerator():
    def __init__(self):
        pass
    def generate(self, word):
        a_list=[]
        ## wn.synsets(sord: 단어.품사.그룹인덱스)
        for synsets in wn.synsets(word):
            synsets=str(synsets).split('\'')[1]
            synsets=synsets+'.'+synsets.split('.')[0]
            print(synsets)
            a_list.append(wn.lemma(synsets).antonyms())
        # a_list=list(dict.fromkeys(a_list))## 중복 제거
        print(a_list)
        return a_list

a=AntonymsGenerator()
a.generate('king')

# %%
# print(wn.lemma('king.n.01.king').antonyms())
# %%
