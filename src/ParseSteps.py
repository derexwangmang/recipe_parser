import re

def parseSteps(directions):
    output = []
    for d in directions:
        c = re.split('[\.;]\s', d)
        for i, _ in enumerate(c[:-1]):
            if c[i+1][0].islower():
                c[i] = c[i] + '; '
            else:
                c[i] = c[i] + '. '
        output.append(c)
    return output
    