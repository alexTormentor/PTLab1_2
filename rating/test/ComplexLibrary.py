from abc import ABC, abstractmethod
import numpy as np
from typing import List
import xml.etree.ElementTree as ET

DataType = dict[str, list[tuple[str, int]]]

RatingType = dict[str, float]


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating


class DataReader(ABC):

    @abstractmethod
    def read(self, path: str) -> DataType:
        pass


class StudentCharacteristics:
    def __init__(self, rating: RatingType) -> None:
        self.rating = rating

    def calculate_first_quartile(self) -> List[str]:

        ratings = list(self.rating.values())

        first_quartile = np.percentile(ratings, 25)

        first_quartile_students = [student for student, student_rating in
                                   self.rating.items()
                                   if student_rating <= first_quartile]

        return first_quartile_students


class StudentStatistics:
    def __init__(self, data: DataType):
        self.data = data
        self.rating = CalcRating(data).calc()
        self.students = list(self.rating.keys())

    def get_first_quartile_students(self) -> List[str]:
        ratings = list(self.rating.values())
        first_quartile = np.percentile(ratings, 25)

        first_quartile_students = [student for student, rating
                                   in self.rating.items()
                                   if rating <= first_quartile]

        return first_quartile_students


class TextDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            for line in file:
                if not line.startswith(" "):
                    self.key = line.strip()
                    self.students[self.key] = []
                else:
                    subj, score = line.split(":", maxsplit=1)
                    self.students[self.key].append(
                        (subj.strip(), int(score.strip())))
        return self.students


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
