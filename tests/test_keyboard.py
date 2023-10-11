"""
Здесь надо написать тесты с использованием pytest для модуля keyboard.
"""

import pytest
from src.keyboard import Keyboard


@pytest.fixture
def kb():
	# смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
	return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(kb):
	'''
	Тестируем __str__ для keyboard
	'''
	assert str(kb) == 'Dark Project KD87A'


def test_change_lang(kb):
	'''
	Тестируем переключение языка
	'''
	assert str(kb.language) == "EN"

	kb.change_lang()
	assert str(kb.language) == "RU"
	
	# Сделали EN -> RU -> EN
	kb.change_lang().change_lang().change_lang()
	assert str(kb.language) == "EN"
