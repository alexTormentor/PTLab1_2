from typing import List, Tuple
from CalcRating import CalcRating
from Types import DataType
import numpy as np


class StudentStatistics:
    def __init__(self, data: DataType):
        self.data = data
        self.rating = CalcRating(data).calc()
        self.students = list(self.rating.keys())

    def get_first_quartile_students(self) -> List[str]:
        ratings = list(self.rating.values())
        first_quartile = np.percentile(ratings, 25)

        first_quartile_students = [student for student, rating in self.rating.items() if rating <= first_quartile]

        return first_quartile_students
