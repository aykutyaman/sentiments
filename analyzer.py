import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = self.get_lines(positives)
        self.negatives = self.get_lines(negatives)
        self.tokenizer = nltk.tokenize.TweetTokenizer()

    def get_lines(self, file):
        lines_list = []
        with open(file, 'r') as lines:
            for line in lines:
                if line.startswith('#') == False:
                    lines_list.append(line.strip())
        return lines_list

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        for token in self.tokenizer.tokenize(text):
            token = token.lower()
            if token in self.positives:
                score += 1
            elif token in self.negatives:
                score -= 1
        return score
