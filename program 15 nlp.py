class PCFGParser:
    def __init__(self, pcfg):
        self.pcfg = pcfg

    def parse(self, sentence):
        words = sentence.split()
        n = len(words)
        
        # Initialize chart for dynamic programming
        chart = [[{} for _ in range(n+1)] for _ in range(n+1)]

        # Fill in chart for words of length 1
        for i in range(1, n+1):
            for X in self.pcfg:
                if (words[i-1],) in self.pcfg[X]:
                    chart[i-1][i][X] = self.pcfg[X][(words[i-1],)]

        # CKY algorithm
        for span in range(2, n+1):
            for begin in range(n+1-span):
                end = begin + span
                for split in range(begin+1, end):
                    for X in self.pcfg:
                        for Y in self.pcfg[X]:
                            for Z in self.pcfg[Y]:
                                if (Y, Z) in chart[begin][split] and (Z,) in chart[split][end]:
                                    prob = chart[begin][split][Y, Z] * chart[split][end][Z,]
                                    if X not in chart[begin][end] or prob > chart[begin][end][X]:
                                        chart[begin][end][X] = prob

        if 'S' in chart[0][n]:
            return chart[0][n]['S']
        else:
            return 0.0


# Example usage
pcfg = {
    'S': {('NP', 'VP'): 0.9, ('X', 'VP'): 0.1},
    'NP': {('Det', 'N'): 0.6, ('N',): 0.4},
    'VP': {('V', 'NP'): 0.7, ('V', 'PP'): 0.3},
    'PP': {('P', 'NP'): 1.0},
    'Det': {('the',): 0.5, ('a',): 0.5},
    'N': {('man',): 0.3, ('ball',): 0.3, ('woman',): 0.4},
    'V': {('hit',): 0.6, ('saw',): 0.4},
    'P': {('with',): 1.0}
}

parser = PCFGParser(pcfg)
sentence = "the man saw a woman with a ball"
probability = parser.parse(sentence)
print("Probability of the sentence:", probability)
