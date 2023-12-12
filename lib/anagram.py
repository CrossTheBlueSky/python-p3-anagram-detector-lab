# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        out = []
        for entry in list:
            if sorted(entry) == sorted(self.word):
                out.append(entry)
        return out