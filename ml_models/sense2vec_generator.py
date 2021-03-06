from collections import OrderedDict
from typing import List

from sense2vec import Sense2Vec


class Sense2VecDistractorGenerator():
    def __init__(self):
        self.model = Sense2Vec().from_disk('/home/Leaf-Question-Generation/app/ml_models/sense2vec_distractor_generation/data/s2v_old')

    def generate(self, answer: str, desired_count: int) -> List[str]:
        distractors = []
        answer = answer.lower()
        answer = answer.replace(" ", "_")

        sense = self.model.get_best_sense(answer)

        if not sense:
            return []

        most_similar = self.model.most_similar(sense, n=desired_count)

        for phrase in most_similar:
            normalized_phrase = phrase[0].split("|")[0].replace("_", " ").lower()

            if normalized_phrase.lower() != answer: #TODO: compare the stem of the words (e.g. wrote, writing)
                distractors.append(normalized_phrase.capitalize())

        return list(OrderedDict.fromkeys(distractors))
