#%%
import textwrap
import warnings
warnings.filterwarnings(action='ignore')

from mcq_gen import MCQGenerator
#%%
MCQ_Generator = MCQGenerator(True)
## 지문번호와 문제유형을 받는다...
## 근데 이렇게 한두줄이면 그냥 딴거랑 합칠가 ㅇㅅㅇ
mcq_dict=MCQ_Generator.generate_mcq_questions(1, 10)