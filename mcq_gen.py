#%%
from typing import List
from unittest import result

import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
import time

import toolz

from function import *
from ml_models.distractor_generation.distractor_generator import \
    DistractorGenerator
from ml_models.keyword_generation.keyword_generator import KeywordGenerataior
from ml_models.question_generation.question_generator import QuestionGenerator
from ml_models.sense2vec_distractor_generation.sense2vec_generator import \
    Sense2VecDistractorGenerator
from ml_models.summerizer_generation.summerizer_generator import \
    SummerizerGenerator
from question import Question
#%%
class MCQGenerator():
    def __init__(self,is_verbose=False):
        start_time = time.perf_counter()
        print('Loading ML Models...')

        # self.question_generator = QuestionGenerator()
        # print('Loaded QuestionGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.distractor_generator = DistractorGenerator()
        print('Loaded DistractorGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.sense2vec_distractor_generator = Sense2VecDistractorGenerator()
        print('Loaded Sense2VecDistractorGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.keyword_generator = KeywordGenerataior()
        print('Loaded KeywordGenerataior in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.distractor_generator = SummerizerGenerator()
        print('Loaded SummerizerGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

    def final(self, full_txt, question_type):
        ## 지문 받아서 문제 만들고
        ## 맨 마지막 딕셔너리 리턴
        ## 문제번호는 언제 정하지 ??
        ## 문제타입은?? init에서정하는건에바고 음 여기서 매번 QuestionGenerator 다시 로딩해야하나
        ## 몇 개 만드는지는?? 아모르겠눙 ㅇㅅㅇ

        ## question_table: sql에 들어갈것
        question_table=['full txt',# 지문번호로 바뀔예정
                         'question type',
                         'question', 
                         'answer',
                         'distractors']## distractors list?? 아니면 d1, d2, d3, d4??
        cleaned_txt=clean_text(full_txt)

        ###### 이부분 모델 완성하면 코딩 ~~~~~

        q='asdfasdfasdfasdfasdf'
        a='aa'
        d=['zz', 'xx', 'bb', 'cc']##일단 리스트로 한다고 치자

        '''
        ## 함수 만들면 요로코롬 한다는 뜻
        q=question(full_txt, question_type)
        a=ans(full_txt)
        d=distractors(full_txt, q)
        '''

        result=[full_txt, question_type, q, a, d]
        MCQ={ x:y for x,y in zip(question_table,result)}
        
        return MCQ

    ''' # 문제 답 오답 무엇을 먼저 만들지에 따라 매개변수 변할 듯
    ## 일단은 question_type에 따라 따로 돌려야 하나 아무튼 ..
    def question(self, full_txt, question_type):
    def ans(self, full_txt):
    def distractors(self, context, question):'''