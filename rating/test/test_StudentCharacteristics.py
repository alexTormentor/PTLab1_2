import pytest
from StudentCharacteristics import StudentCharacteristics

# тест кейсы
@pytest.mark.parametrize("input_data, expected_result", [
    ({"Иванов": 60.0, "Петров": 55.0, "Абрамов": 75.0, "Барабулька": 16.0}, ["Барабулька"]),
])
def test_calculate_first_quartile(input_data, expected_result):
    student_char = StudentCharacteristics(input_data)
    result = student_char.calculate_first_quartile()
    assert result == expected_result


if __name__ == '__main__':
    pytest.main()
