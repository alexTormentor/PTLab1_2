import pytest
from StudentStatistics import StudentStatistics
from Types import DataType


class TestStudentStatistics:
    @pytest.fixture()
    def input_data(self) -> DataType:
        data: DataType = {
            'Student1': [('mathematics', 60), ('programming', 70), ('literature', 50)],
            'Student2': [('mathematics', 65), ('sociology', 55), ('chemistry', 45)],
            'Student3': [('mathematics', 75), ('programming', 80), ('literature', 70)],
        }
        return data

    def test_get_first_quartile_students(self, input_data: DataType):
        stats = StudentStatistics(input_data)
        first_quartile_students = stats.get_first_quartile_students()
        assert first_quartile_students == ['Student2']
