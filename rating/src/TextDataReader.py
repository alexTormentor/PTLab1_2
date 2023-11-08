# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader


class TextDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""  # студент
        self.students: DataType = {}  # ключ студент, знач -
        # спсиок предмет+оценка

    def read(self, path: str) -> DataType:
        # Открываем указанный текстовый файл для чтения
        # с указанной кодировкой UTF-8
        with open(path, encoding='utf-8') as file:
            for line in file:
                # Перебираем строки в файле
                if not line.startswith(" "):
                    # Если строка не с пробела, это студент
                    # определяем ключ (студента)
                    self.key = line.strip()
                    self.students[self.key] = []  # создает
                    # пустой список и связывает со студентом
                else:
                    # Если строка с пробела, это предмет+оценка
                    # Разделяем строку на 2 части по символу :
                    subj, score = line.split(":", maxsplit=1)
                    # создаем кортеж с именем предмета и оценкой
                    # и вяжем к студенту
                    self.students[self.key].append(
                        (subj.strip(), int(score.strip())))
        return self.students
