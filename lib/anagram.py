# your code goes here!

class Anagram():
    def __init__(self, word):
        self.word = word
    def match (self, list):
        possible_anagrams = []

        list_word = sorted (letter for letter in self.word)
        for word in list:
            if sorted(letter for letter in word) == list_word:
                possible_anagrams.append(word)
        return possible_anagrams

