import argparse
import os
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from StudentCharacteristics import StudentCharacteristics
from XMLDataReader import XMLDataReader


class DataProcessor:
    def __init__(self, data_format):
        self.data_format = data_format

    def processData(self, path):  # принимает путь к файлу
        _, file_extension = os.path.splitext(path)  # путь к файлу на базовое
        # имя и расширение.
        # Результат присваивается file_extension.
        # _ отбросит то, что осталось ЗА сплитом, эдакая заглушка
        if file_extension == ".txt":
            reader = TextDataReader()
        elif file_extension == ".xml":
            reader = XMLDataReader()
        else:
            raise ValueError("Unsupported file format. Use '.txt' or '.xml'.")

        students = reader.read(path)  # читаем с пути
        print("Students: ", students)

        rating = CalcRating(students).calc()  # объекту CalcRating даем
        # данные(кортеж то бишь студент: предмет-оценка)
        print("Rating: ", rating)

        student_char = StudentCharacteristics(rating)  # сюда даем рейтинг

        first_quartile_students = student_char.calculate_first_quartile()
        # счтаем квартиль
        print("First Quartile Students: ", first_quartile_students)


def main():
    parser = argparse.ArgumentParser(description="Path to data file")
    parser.add_argument("-p", dest="path", type=str,
                        required=True, help="Path to data file")
    args = parser.parse_args()

    data_processor = DataProcessor(args.path)
    data_processor.processData(args.path)


if __name__ == "__main__":
    main()
