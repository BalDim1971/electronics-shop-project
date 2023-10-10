from src.item import Item


class Phone(Item):
	'''
	Класс для представления товара - телефон
	Наследуем от Item
	'''
	
	def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
		'''
        Создание экземпляра класса Phone.
		
		Параметры унаследованы от Item. Добавлен:
        :param count_sim: Количество Поддерживаемых сим-карт.
		'''
		super().__init__(name, price, quantity)
		self.number_of_sim = number_of_sim
	
	def __repr__(self) -> str:
		'''
        Возвращает строку типа "Phone('iPhone 14', 120000, 5, 2)"
        '''
		
		my_str = super().__repr__()
		my_str = my_str.replace(')', f', {self.__number_of_sim})')
		return my_str
	
	# Геттер для number_of_sim
	@property
	def number_of_sim(self):
		'''
        Возвращает значение приватной переменной __number_of_sim
        '''
		return self.__number_of_sim
	
	# Сеттер для __number_of_sim
	@number_of_sim.setter
	def number_of_sim(self, number_of_sim):
		'''
        Установить значение __number_of_sim
        Должно быть больше 0
        Если 0, выкинуть ошибку
        '''
		if number_of_sim > 0 and type(number_of_sim) == int:
			self.__number_of_sim = number_of_sim
		else:
			raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

