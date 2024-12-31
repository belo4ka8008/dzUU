import string
class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding="utf-8") as file:
                lines = file.readlines()
                words = []
                for line in lines:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation)).replace('-','')
                    words.extend(line.split())
                    all_words[file_name] = words
                return all_words
    def find(self, word):
        for name, words in self.get_all_words().items():
           if word.lower() in words:
               return {name: words.index(word.lower())+1}
    def count(self, word):
        counter = 0
        for name, words in self.get_all_words().items():
            for word_ in words:
                if word.lower() == word_:
                    counter += 1
        return {name: counter}
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))