from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            tree = ET.parse(file)
            root = tree.getroot()
            for student_elem in root.findall('student'):
                self.key = student_elem.find('name').text
                self.students[self.key] = []
                for subject_elem in student_elem.findall('subject'):
                    subj = subject_elem.find('name').text
                    score = int(subject_elem.find('score').text)
                    self.students[self.key].append((subj, score))
        return self.students
