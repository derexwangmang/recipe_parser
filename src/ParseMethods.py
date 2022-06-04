import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import spacy


primary = ['fry', 'saute', 'bake', 'roast', 'boil', 'steam', 'broil', 'poach', 'grill']

nlp = spacy.load("en_core_web_sm")

class Method:
    def __init__(self, input, order):
        self.order = order
        self.primary_cooking = []
        self.secondary_cooking = []
        self.direction = input
    def __str__(self):
        print("direction = {}".format(str(self.direction)))
        # primary cooking = {primary}, secondary cooking = {secondary}, direction = {direction}".format(
        #     order=self.order, primary = self.primary_cooking, secondary = self.secondary_cooking, direction = self.direction
        # ))


def parse_method(direction, i ):
    """ tokens = pos_tag(word_tokenize(directions[i].lower()))
    print(tokens)
    for j in range(len(tokens)):
        if tokens[j][1] == 'VB' or tokens[j][1] == 'VBP':
            print(tokens[j], i) """
    curr_method = Method(direction, i)
    doc = nlp(direction.lower())
    for token in doc:
        #print(token.text, token.pos_)
        if token.pos_ == 'VERB':
            if token.text in primary and not curr_method.primary_cooking:
                curr_method.primary_cooking.append(token.lemma_)
            else:
                curr_method.secondary_cooking.append(token.lemma_)
    if curr_method.secondary_cooking and not curr_method.primary_cooking:
        curr_method.primary_cooking.append(curr_method.secondary_cooking.pop())
    return curr_method