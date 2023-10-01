"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_calculate_total_price():
	'''
	Когда создан класс Смартфон, то должно вернуть 200000
	Для Ноутбук - 100000
	'''
	assert item1.calculate_total_price() == 200000
	assert item2.calculate_total_price() == 100000


def test_apply_discount():
	'''
	Тестируем применение дискаунта
	'''
	Item.pay_rate = 0.8
	item1.apply_discount()
	assert item1.price == 8000.0
	assert item2.price == 20000
	

def test_name():
	'''
	Тестирование возвращение значения приватной переменной
	'''
	assert item1.name == "Смартфон"
	assert item2.name == "Ноутбук"


def test_name_set():
	'''
	Тестируем функцию задания имени
	'''
	item1.name = 'Калькулятор'
	assert item1.name == 'Калькулято'


def test_string_to_number():
	'''
	Тестируем преобразование из строки-числа в целое число
	'''
	assert Item.string_to_number('5.5') == 5
