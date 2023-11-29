# -*- coding: utf-8 -*-
from Types import DataType
from abc import ABC, abstractmethod


class DataReader(ABC):

    @abstractmethod
    def read(self, path: str) -> DataType:
        pass


'''
абстрактный метод, который ожидается в конкретных реализациях
класса DataReader.принимает аргумент path,
представляющий путь к файлу, возвращает структуру,
представленную DataType(словарь, в котором ключи -
строки (имена), значения - списки кортежей с предметоп и оценкой0
'''
