import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import spacy
from textblob import TextBlob
import re
# from parse_tools import Method


# primary = ['fry', 'saute', 'bake', 'roast', 'boil', 'steam', 'broil', 'poach', 'grill']

# nlp = spacy.load("en_core_web_sm")

class Method:
    def __init__(self, input, order):
        self.order = order
        self.primary_cooking = []
        self.secondary_cooking = []
        self.direction = input
    def __str__(self):
        print("order = {}".format(self.order))
        # primary cooking = {primary}, secondary cooking = {secondary}, direction = {direction}".format(
        #     order=self.order, primary = self.primary_cooking, secondary = self.secondary_cooking, direction = self.direction
        # ))

sp = spacy.load('en_core_web_sm')

def parse_tool(direction):

    sentences = direction.split(".")
    cleansentences = []
    for sentence in sentences:
        cleansentence = sentence.strip()
        cleansentence = cleansentence.lower()
        cleansentences.append(cleansentence)

    tools = []
    # print(cleansentences)
    for sentence in cleansentences:
        sentence = re.sub(r'[^\w\s]', '', sentence)
        print(sentence)
        spltsentence = sentence.split()
        cutword = None
        for i in range(len(spltsentence)):
            keywords = ["in", "into", "using","use"]
            if spltsentence[i] in keywords:
                cutword = spltsentence[(i+1):]

        toollst = []

        if cutword != None:
            sen = sp(" ".join(cutword))
            for j in range(len(cutword)):
                if sen[j].pos_ == "NOUN":
                    if sen[j-1].pos_ == "ADJ":
                        toollst.append(cutword[j-1])
                        toollst.append(cutword[j])
                    else:
                        toollst.append(cutword[j])
                    break
                
            tool = " ".join(toollst)
            tools.append(tool)

    return tools