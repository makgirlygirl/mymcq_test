#%%
from typing import List

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

        self.question_generator = QuestionGenerator()
        print('Loaded QuestionGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.distractor_generator = DistractorGenerator()
        print('Loaded DistractorGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.sense2vec_distractor_generator = Sense2VecDistractorGenerator()
        print('Loaded Sense2VecDistractorGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.keyword_generator = KeywordGenerataior()
        print('Loaded KeywordGenerataior in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

        self.distractor_generator = SummerizerGenerator()
        print('Loaded SummerizerGenerator in', round(time.perf_counter() - start_time, 2), 'seconds.') if is_verbose else ''

    def question():
    def ans()
    def distractors():