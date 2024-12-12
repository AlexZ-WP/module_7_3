import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding="utf-8") as file:
                line = file.read()
                table = str.maketrans("", "", ',.=!?;:-')
                line = line.translate(table)
                new_line = line.lower()
                all_words[i] = new_line.split()

        return all_words

    def find(self, word):
        """
        Возвращает словарь, где ключ - название файла, значение - позиция первого
        такого слова в списке слов этого файла.
        """
        word_list = {}
        word = word.lower()
        #counter = 0
        for file_names, values in self.get_all_words().items():
            counter = 0
            for val in values:
                counter += 1
                if word == val.lower():
                    word_list[file_names] = counter
                    break
        return word_list

    def count(self, word):
        """
        Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
        """
        word_count = {}
        word = word.lower()
        for file_names, values in self.get_all_words().items():
            counter = 0
            for val in values:
                if word == val.lower():
                    counter += 1
            word_count[file_names] = counter

        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего