from typing import List
from CalcRating import RatingType
import numpy as np


class StudentCharacteristics:
    def __init__(self, rating: RatingType) -> None:
        self.rating = rating

    def calculate_first_quartile(self) -> List[str]:

        ratings = list(self.rating.values())

        first_quartile = np.percentile(ratings, 25)

        first_quartile_students = [student for student, student_rating in self.rating.items() if student_rating <= first_quartile]

        return first_quartile_students
