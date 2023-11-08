from typing import List
from CalcRating import RatingType
import numpy as np


class StudentCharacteristics:
    def __init__(self, rating: RatingType) -> None:
        self.rating = rating  # словарь

    def calculate_first_quartile(self) -> List[str]:
        # получаем словарь
        ratings = list(self.rating.values())  # содержит все рейтинги студентов

        # вычисляем квартиль
        first_quartile = np.percentile(ratings, 75)

        # студенты у которых рейтинг в первом квартиле
        first_quartile_students = [student for student, student_rating
                                   in  # перечисленоие по кортежу
                                   self.rating.items()  # пары ключ=знач с
                                   # студентом и рейтингом
                                   if student_rating >= first_quartile]
        # очевидно если выше 75%

        return first_quartile_students
