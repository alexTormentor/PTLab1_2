from typing import List
from CalcRating import RatingType
import numpy as np


class StudentCharacteristics:
    def __init__(self, rating: RatingType) -> None:
        self.rating = rating

    def calculate_first_quartile(self) -> List[str]:
        # получаем словарь
        ratings = list(self.rating.values())

        # вычисляем квартиль
        first_quartile = np.percentile(ratings, 75)

        # студенты у которых рейтинг в первом квартиле
        first_quartile_students = [student for student, student_rating in
                                   self.rating.items()
                                   if student_rating >= first_quartile]

        return first_quartile_students
