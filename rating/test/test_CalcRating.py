# -*- coding: utf-8 -*-
from Types import DataType
from CalcRating import CalcRating
import pytest

RatingType = dict[str, float]


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 70),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 76.5000
        }

        return  data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType, RatingType]) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingType]) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score, abs=0.001) == input_data[1][student]

    def test_empty_data(self, input_data: tuple[DataType, RatingType]) -> None:
        # Создайте объект CalcRating с пустыми данными
        calc_rating = CalcRating({})

        # Вызовите метод calc() для вычисления рейтинга
        rating = calc_rating.calc()

        # Проверьте, что результатом является пустой словарь рейтингов
        assert rating == {}

    def test_negative_scores(self):
        data: DataType = {
            "Иванов Иван": [("математика", -80), ("русский язык", -76)],
            "Петров Петр": [("математика", -61), ("русский язык", -70)],
        }

        expected_scores: RatingType = {
            "Иванов Иван": -78.0,
            "Петров Петр": -65.5,
        }

        rating = CalcRating(data).calc()
        for student, expected_score in expected_scores.items():
            assert pytest.approx(rating[student], abs=0.001) == expected_score


