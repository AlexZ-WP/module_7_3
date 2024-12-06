import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r') as file:
                line_l = []  # режим открытия можно и не указывать
                line = file.read()
                table = str.maketrans("", "", string.punctuation)
                #line = line.translate(table) # если используем данную переменную, то убираются все
                # знаки кроме букв "its"
                new_line = line.translate(table) # при такой переменной апостроф не убирается "it's"
                new_line = line.lower()
                line_l.append(new_line.split())

                for key in self.file_names:
                    for value in line_l:
                        all_words[key] = value

        """Вариант для разбора, выводит или первую строку файла если используем break
        или последнюю строку, если не используем break
        """
        # for i in self.file_names:
        #     with open(i, 'r') as file:
        #         line_l = []
        #         for line in file:
        #             table = str.maketrans("", "", string.punctuation)
        #             new_line = line.translate(table)
        #             new_line = new_line.lower()
        #             line_l.append(new_line.split())
        #             # break
        #         for key in self.file_names:
        #             for value in line_l:
        #                 all_words[key] = value
        #                 break
        file.close()
        return all_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова