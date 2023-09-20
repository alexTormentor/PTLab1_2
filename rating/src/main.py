# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XMLDataReader import XMLDataReader  # Import the XMLDataReader class


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    parser.add_argument("-f", dest="format", type=str, required=True,
                        choices=["text", "xml"], help="Data format (text or xml)")
    args = parser.parse_args(args)
    return args.path, args.format

def main():
    path, data_format = get_path_from_arguments(sys.argv[1:])

    if data_format == "text":
        reader = TextDataReader()
    elif data_format == "xml":
        reader = XMLDataReader()
    else:
        print("Invalid data format. Use 'text' or 'xml'.")
        return

    students = reader.read(path)
    print("Студенты: ", students)

    rating = CalcRating(students).calc()
    print("Общий рейтинг: ", rating)

if __name__ == "__main__":
    main()



# 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 - токен гитхаба