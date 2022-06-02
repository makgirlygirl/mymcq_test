from summarizer import Summarizer


class SummerizerGenerator():
    def __init__(self):
        self.model = Summarizer()
    def generate(self, full_txt, min_len=-50, max_len=200, num_sentence=1):
        result = self.model(full_txt, 
                            min_length=min_len, max_length = max_len ,
                            num_sentences = num_sentence)

        summarized_text = ''.join(result)
        return summarized_text
