import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from StudentCharacteristics import StudentCharacteristics
from XMLDataReader import XMLDataReader
from StudentStatistics import StudentStatistics


class DataProcessor:
    def __init__(self, data_format):
        self.data_format = data_format

    def getDataReader(self):
        if self.data_format == "txt":
            return TextDataReader()
        elif self.data_format == "xml":
            return XMLDataReader()
        else:
            raise ValueError("Invalid data format. Use 'txt' or 'xml'.")

    def processData(self, path):
        reader = self.getDataReader()
        students = reader.read(path)
        print("Students: ", students)

        rating = CalcRating(students).calc()
        print("Rating: ", rating)

        # For quartile determination
        student_char = StudentCharacteristics(rating)

        # Output
        first_quartile_students = student_char.calculate_first_quartile()
        print("First Quartile Students: ", first_quartile_students)


def main():
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-f", dest="format", type=str, required=True,
                        choices=["txt", "xml"],
                        help="Data format (txt or xml)")
    args = parser.parse_args()

    data_type = "Text Data" if args.format == "txt" else "xml"
    data_processor = DataProcessor(args.format)
    data_processor.processData(f"./data/data.{args.format}")


if __name__ == "__main__":
    main()
