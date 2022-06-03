import spacy
import re

# class Method:
#     def __init__(self, input, order):
#         self.order = order
#         self.primary_cooking = []
#         self.secondary_cooking = []
#         self.direction = input
#     def __str__(self):
#         print("order = {}".format(self.order))

import spacy
sp = spacy.load('en_core_web_sm')

toollist = ["bowl", "frying pan", "skillet", "fork", "spoon", "chopsticks",
"plate", "microwave", "oven", "air fryer", "saucepan", "pot", "sheet pan", 
"baking pan", "pan", "baking dish", "knife", "knives", "measuring spoon",
"measuring cup", "peeler", "whisk", "tongs", "cutting board", "colander",
"can opener", "grater", "microplane", 'blender', "spatula", "slotted spoon",
"corkscrew", "plastic bag", "broiler pan"]
method_to_tool = {"whisk": "whisk", "grate": "grater", "blend":"blender", "deep fry":"deep fryer",
"stir":"spoon", "microwave":"microwave", "drain":"colander", "bake":"oven", 
"strain":"strainer", "saute":"wooden spoon", "chop":"knife", "mix":"spoon"}


def parse_tool(directions):
    def parse(direction):
        sentences = direction.split(".")
        cleansentences = []
        for sentence in sentences:
            sentence = sentence.split(';')
            if sentence == ['']:
                break
            else:
                for s in sentence:
                    cleansentence = s.strip()
                    cleansentence = cleansentence.lower()
                    cleansentences.append(cleansentence)

        tools = []
        tool_pattern = re.compile('in|into|using|use|to')
        sent_containing_tool = list(filter(tool_pattern.search, cleansentences))

        for sentence in cleansentences:
            spltsentence = sentence.split()
            if sentence in sent_containing_tool:
                sentence = re.sub(r'[^\w\s]', '', sentence)
                
                sen = sp(sentence)
                # print("sentence is: ", sentence)
                # toolwords = []
                for tool in toollist:
                    toolwords = []
                    if tool in sentence: 
                        finaltool = None
                        # print("THE TOOL FOUND IS: ", tool)
                        toolsplt = tool.split(" ")
                        # print("the first word in the split tool list is ", toolsplt[0])
                        if toolsplt[0] in spltsentence:
                            index = spltsentence.index(toolsplt[0])
                        else:
                            break
                        # print("SPLIT TOOL IS ", toolsplt)
                        if sen[index-1].pos_ == "ADJ":
                            toolwords.append(str(sen[index-1]))
                            for word in toolsplt:
                                toolwords.append(word)
                            # print("toolwords is ", toolwords, "(WITH ADJECTIVE)")
                        else:
                            for word in toolsplt:
                                toolwords.append(word)
                            # print("toolwords is ", toolwords, "(NO ADJECTIVE)")
                        # print("the toolwords as a list is: ", toolwords)
                        finaltool = " ".join(toolwords)
                        # print("FINAL TOOL FOUND: ", finaltool)
                        tools.append(finaltool) 
            else:
                for word in spltsentence:
                    for method in method_to_tool.keys():
                        if word == method:
                            tools.append(method_to_tool.get(method))   
        tools = list(set(tools))
        return tools

    result = []
    for i in range(len(directions)):
        currtool = parse(directions[i])
        result.extend(currtool)
    result = list(set(result))
    return result