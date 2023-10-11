######################################################################################
# Описание товара - клавиатура
######################################################################################

from src.item import Item


class MixinLang:
	'''
	Класс для переключения языка клавиатуры
	Атрибут language и метод для изменения атрибута
	'''
	
	def __init__(self):
		self.__language = 'EN'
	
	def change_lang(self):
		if self.__language == 'EN':
			self.__language = 'RU'
		else:
			self.__language = 'EN'
		return self
	
	# Геттер для language
	@property
	def language(self):
		'''
        Возвращает значение приватной переменной __name
        '''
		return self.__language


class Keyboard(Item, MixinLang):
	'''
	Класс для представления товара - клавиатура
	Наследуем от Item.
	'''
	
	def __init__(self, name: str, price: float, quantity: int):
		'''
		Инициируем экземпляр класса
		'''
		
		super().__init__(name, price, quantity)
		MixinLang.__init__(self)
