# -*- coding: utf-8 -*-
from Types import DataType

# словарь, ключами являются имена студентов,
# значениями - рейтинги студентов
RatingType = dict[str, float]


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data  # информация о студентах
        self.rating: RatingType = {}  # будет заполнен рейтингами студентов

    def calc(self) -> RatingType:
        for key in self.data:  # Для каждого студента
            self.rating[key] = 0.0  # начальное значение рейтинга
            for subject in self.data[key]:  # для каждого предмета
                # (имя предмета и оценка) студента
                self.rating[key] += subject[1]  # суммирование оценок
            self.rating[key] /= len(self.data[key])  # сумма оценок делится
            # на количество предметов у студента
        return self.rating  # ключами являются имена студентов,
        # а значениями - их рейтинги
