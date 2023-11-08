import pytest
from src.StudentCharacteristics import StudentCharacteristics


# тест кейсы
@pytest.mark.parametrize("input_data, expected_result", [
    ({"Иванов": 60.0, "Петров": 55.0, "Абрамов": 75.0, "Барабулька": 16.0},
     ["Абрамов"]),
    ({"Иванов": 60.0}, ["Иванов"]),  # 1 элемент
    ({"Иванов": 75.0, "Петров": 75.0, "Сидоров": 75.0},
     ["Иванов", "Петров", "Сидоров"]),  # Словарь рейтингов
    # с несколькими студентами, все с одинаковым рейтингом
    ({"Иванов": 0.0, "Петров": 0.0, "Сидоров": 0.0, "Абрамов": 0.0},
     ["Иванов", "Петров", "Сидоров", "Абрамов"]),


])
def test_calculate_first_quartile(input_data, expected_result):
    student_char = StudentCharacteristics(input_data)
    result = student_char.calculate_first_quartile()
    assert result == expected_result


if __name__ == '__main__':
    pytest.main()
