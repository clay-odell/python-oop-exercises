"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file_path):
        self.words = self.read_words(file_path)
        print(f"{len(self.words)} words read")
    
    def read_words(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file if line.strip() and not line.startswith('#')]
        except FileNotFoundError:
            print("The file was not found.")
            return []
        
    def random(self):
        return random.choice(self.words) if self.words else None
