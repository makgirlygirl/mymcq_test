#%%
from typing import List
from unittest import result

import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
import time

import toolz

### 여기 나중에 수정을 ㅎ보자
from function import *
from models import *
from question import Question

#%%
'''
from mymcq.ml_models.distractor_generator import \
    DistractorGenerator
from ml_models.keyword_generation.keyword_generator import KeywordGenerataior
from ml_models.question_generation.question_generator import QuestionGenerator
from ml_models.sense2vec_distractor_generation.sense2vec_generator import \
    Sense2VecDistractorGenerator
from ml_models.summerizer_generation.summerizer_generator import \
    SummerizerGenerator'''
#%%
'''
내용일치
어휘
목적 요지 주제 주장 제목
빈칸추론
문장순서
문장삽입 
요약문
장문, 문법, 도표 는 나중에
'''
#%%
class MCQGenerator():
    def __init__(self,is_verbose=False):
        start_time = time.perf_counter()
        print('Loading ML Models...')

        # self.question_generator = QuestionGenerator()
        # self.distractor_generator = DistractorGenerator()
        # self.sense2vec_distractor_generator = Sense2VecDistractorGenerator()
        # self.keyword_generator = KeywordGenerataior()
        # self.distractor_generator = SummerizerGenerator()

        self.summerizerGenerator=SummerizerGenerator() # 요약문
        self.keysentenceGenerator=KeysentenceGenerator() # 중심문장
        self.keywordGenerator=KeywordGenerator() # 키워드
        # 오답
        
        print('Finish Loading ML Models...', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

    def final(self, paragraph_num, question_type):
        ## 지문 받아서 문제 만들고
        ## 맨 마지막 딕셔너리 리턴
        ## 문제번호는 언제 정하지 ??
        ## 문제타입은?? init에서정하는건에바고 음 여기서 매번 QuestionGenerator 다시 로딩해야하나
        ## 몇 개 만드는지는?? 아모르겠눙 ㅇㅅㅇ

        ## question_table: sql에 들어갈것
        question_table=['paragraph_num',
                         'question type',
                         'question', 
                         'answer',
                         'distractors']## distractors list?? 아니면 d1, d2, d3, d4??
        
        '''
        full_txt=  ##sql에서 paragrapgh num 에 맞게 읽어오기
        cleaned_txt=clean_text(full_txt)
        
        q=question(full_txt, question_type)
        a=ans(full_txt)
        d=distractors(full_txt, q)
        '''
        q='asdfasdfasdfasdfasdf'
        a='aa'
        d=['zz', 'xx', 'bb', 'cc']##일단 리스트로 한다고 치자

        result=[paragraph_num, question_type, q, a, d]
        MCQ={ x:y for x,y in zip(question_table,result)}
        
        return MCQ

    ## 문제 답 오답 무엇을 먼저 만들지에 따라 매개변수 변할 듯
    ## 일단은 question_type에 따라 따로 돌려야 하나 아무튼 ..
    def question(self, full_txt, question_type):
        
    def ans(self, full_txt):
    def distractors(self, context, question):
