"""Здесь надо написать тесты с использованием pytest для модуля phone."""

import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
	# смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
	return Phone("iPhone 14", 120_000, 5, 2)


def test_str(phone1):
	'''
	Тестируем __str__ для Phone
	'''
	assert str(phone1) == 'iPhone 14'


def test_repr(phone1):
	'''
	Тестируем __repr__ для Phone
	'''
	assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone1):
	'''
	Тестирование возвращение значения симкарт
	'''
	assert phone1.number_of_sim == 2


def test_number_of_sim_set(phone1):
	'''
	Тестируем функцию задания количества симкарт
	'''
	with pytest.raises(ValueError):
		phone2 = Phone("iPhone 14", 120_000, 5, -1)
	for i in (-1, 0, 0.5, 1.5, 2.99):
		with pytest.raises(ValueError):
			phone1.number_of_sim = i
