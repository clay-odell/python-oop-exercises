"""Word Finder: finds random words from a dictionary.
   
"""
import random

class WordFinder:
    def __init__(self, file_path):
        dict_file = open(file_path)
        self.words = self.read_words(dict_file)
        print(f"{len(self.words)} words read.")
     
    def read_words(self, dict_file):
        return [line.strip() for line in dict_file]
    
    def random(self):
        return random.choice(self.words) if self.words else None
    
class SpecialWordFinder(WordFinder):
    def read_words(self, dict_file):
        return [line.strip() for line in dict_file if line.strip() and not line.startswith('#')]