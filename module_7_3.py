import string


class WordsFinder:

    def __init__(self, *file_names):
        pass
       #self.file_names = file_names[]

    def get_all_words(self):
        all_words ={}
        for i in self.file_names:
            with open(self.file_names) as file:
                line_l = []
                for line in file:
                    table = str.maketrans("", "", string.punctuation)
                    new_line = line.translate(table)
                    new_line = line.lower()
                    new_line.split()
                    line_l = new_line.split()
            for key in self.file_names:
                for value in line_l:
                    all_words[key] = value
                    break

    def find(self, word):
        find_d = {}
        for name, words in get_all_words().items():
        pass

    def count(self, word):
        pass
