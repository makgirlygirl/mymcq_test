#%%
from platform import dist
from typing import List
import string
import re
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
#%% duplicate_removal.py in leaf

def remove_duplicates(items: List[str]) -> List[str]:
    unique_items = []
    normalized_unique_items = []

    for item in items:
        normalized_item = _normalize_item(item)

        if normalized_item not in normalized_unique_items:
            unique_items.append(item)
            normalized_unique_items.append(normalized_item)

    return unique_items

def remove_distractors_duplicate_with_correct_answer(correct: str, distractors: List[str]) -> List[str]:
    for distractor in distractors:
        if _normalize_item(correct) == _normalize_item(distractor):
            distractors.remove(distractor)
    
    return distractors

'''
Code from: https://github.com/allenai/bi-att-flow/blob/master/squad/evaluate-v1.1.py
'''
def _normalize_item(item) -> str:
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(item))))

def _calculate_nltk_bleu(references: List[str], hypothesis: str, bleu_n: int = 1):
    if hypothesis == '': 
        return 0, 0, 0, 0 

    # Word tokenize
    refs_tokenized = list(map(lambda x: word_tokenize(x), references))
    hyp_tokenized = word_tokenize(hypothesis)

    # Smoothing function to avoid the cases where it resuts 1.0 in the cases when // Corpus/Sentence contains 0 counts of 2-gram overlaps. BLEU scores might be undesirable; use SmoothingFunction() //
    chencherry = SmoothingFunction()
    bleu = 0

    if bleu_n == 1:
        bleu = sentence_bleu(refs_tokenized, hyp_tokenized, weights=(1, 0, 0, 0), smoothing_function=chencherry.method2)
    elif bleu_n == 2:
        bleu = sentence_bleu(refs_tokenized, hyp_tokenized, weights=(0.5, 0.5, 0, 0), smoothing_function=chencherry.method2)
    elif bleu_n == 3: 
        bleu = sentence_bleu(refs_tokenized, hyp_tokenized, weights=(0.33, 0.33, 0.33, 0), smoothing_function=chencherry.method2)
    elif bleu_n == 4:
        bleu = sentence_bleu(refs_tokenized, hyp_tokenized, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=chencherry.method2)

    return bleu
#%% text_cleaning.py in leaf

def clean_text(text: str) -> str:
    """Clean the text from symbols and additional information.
    
    Args:
        text (str): The text.
    
    Returns:
        str: CLeaned text.
    """
    cleaned_text = _remove_brackets(text)
    cleaned_text = _remove_square_brackets(cleaned_text)
    cleaned_text = _remove_multiple_spaces(cleaned_text)
    cleaned_text = _replace_weird_hyphen(cleaned_text)
    
    return cleaned_text
    

def _remove_brackets(text: str) -> str:
    """ Remove brackets '(', ')' and the information between them. 

    e.g. "The koala has a body length of 60–85 cm (24–33 in)."
    
    Args:
        text (str): The text.
    
    Returns:
        str: CLeaned text.
    """
    return re.sub(r'\((.*?)\)', lambda L: '', text)


def _remove_square_brackets(text: str) -> str:
    """ Remove square brackets '[', ']' and the information between them. 

    e.g. The koala[1] is cool."
    
    Args:
        text (str): The text.
    
    Returns:
        str: CLeaned text.
    """

    return re.sub(r'\[(.*?)\]', lambda L: '', text)


def _remove_multiple_spaces(text: str) -> str:
    """Remove multiple white spaces. 

    e.g. "The koala         is     angry  !"
    
    Args:
        text (str): The text.
    
    Returns:
        str: CLeaned text.
    """

    return re.sub(' +', ' ', text)


def _replace_weird_hyphen(text: str) -> str:
    """ Replace weird '–' hyphen that's not recognized as a delimeter by spacy. 

    e.g. '4–15 kg' -> '4-15 kg' 
    (You may not see a difference, but there fucking is. This motherfucker '–' is not recognized by spacy as a delimeter.)
    
    Args:
        text (str): The text.
    
    Returns:
        str: CLeaned text.
    """
    return text.replace('–', '-')