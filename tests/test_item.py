"""
Тесты с использованием pytest для модуля item.
"""

import os

import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def item1():
	return Item("Смартфон", 10000, 20)


item2 = Item("Ноутбук", 20000, 5)


def test_repr(item1):
	assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):
	assert str(item1) == 'Смартфон'


def test_calculate_total_price(item1):
	'''
	Когда создан класс Смартфон, то должно вернуть 200000.
	'''
	assert item1.calculate_total_price() == 200000


def test_calculate_total_price():
	'''
	Когда создан класс Ноутбук должно вернуть 100000.
	'''
	assert item2.calculate_total_price() == 100000


def test_apply_discount(item1):
	'''
	Тестируем применение скидки.
	'''
	Item.pay_rate = 0.8
	item1.apply_discount()
	assert item1.price == 8000.0
	assert item2.price == 20000


def test_name(item1):
	'''
	Тестирование возвращение значения приватной переменной.
	'''
	assert item1.name == "Смартфон"
	assert item2.name == "Ноутбук"


def test_name_set(item1):
	'''
	Тестируем функцию задания имени.
	'''
	item1.name = 'Калькулятор'
	assert item1.name == 'Калькулято'


def test_string_to_number():
	'''
	Тестируем преобразование из строки-числа в целое число.
	'''
	assert Item.string_to_number('5') == 5
	assert Item.string_to_number('5.0') == 5
	assert Item.string_to_number('5.9') == 5


def test_add():
	'''
	Тестируем сложение данных разных товаров.
	'''
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	item2 = Item("Смартфон", 10000, 20)
	assert item2 + phone1 == 25
	assert phone1 + phone1 == 10
	with pytest.raises(TypeError):
		item2 + 5


def test_instantiate_from_csv():
	'''
	Тестируем корректность загрузки из файла и наличие файла.
	'''
	Item.instantiate_from_csv(os.path.join('src', 'items.csv'))
	assert len(Item.all) == 5
	
	with pytest.raises(FileNotFoundError):
		Item.instantiate_from_csv(os.path.join('items.csv'))


def test_instantiate_from_csv_corrupted_file():
	'''
	Проверяем, что исключение InstantiateCSVError возбуждается
	'''
	
	assert str(InstantiateCSVError()) == 'Файл items.csv поврежден'
	with pytest.raises(InstantiateCSVError):
		Item.instantiate_from_csv(os.path.join('tests', 'items_cor.csv'))
