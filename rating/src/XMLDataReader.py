from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        # Открываем указанный XML-файл для чтения с указанной кодировкой UTF-8
        with open(path, encoding='utf-8') as file:
            # Создаем объект ElementTree и загружаем XML-данные из файла
            tree = ET.parse(file)
            root = tree.getroot()
            # Для каждого элемента <student>
            for student_elem in root.findall('student'):
                # Извлекаем имя студента
                self.key = student_elem.find('name').text
                # Создаем пустой список для предметов и оценок
                self.students[self.key] = []
                # Для каждого элемента <subject> внутри <student>
                for subject_elem in student_elem.findall('subject'):
                    # Извлекаем имя предмета
                    subj = subject_elem.find('name').text
                    # Извлекаем оценку и в число
                    score = int(subject_elem.find('score').text)
                    # Добавляем предмет и оценку в список для студента
                    self.students[self.key].append((subj, score))
        return self.students
