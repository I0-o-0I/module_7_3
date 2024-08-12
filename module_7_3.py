import re
class WordsFinder:
    def __init__(self, *name):
        self.file_names = name

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line_new = re.sub(r'[^\w\s]', '', line)
                    words.extend(line_new.split())
                    all_words[name] = words
                return all_words
    def find(self, word):
        word = word.lower()
        find = {}
        for name, words in self.get_all_words().items():
            if word in words:
                index = words.index(word)
                find[name] = index + 1
        return find
    def count(self, word):
        word = word.lower()
        count = {}
        for name, words in self.get_all_words().items():
            count[name] = words.count(word)
        return count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего