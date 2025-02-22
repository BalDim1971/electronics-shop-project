import csv
import os


class InstantiateCSVError(Exception):
	'''
	Исключение с сообщением “_Файл item.csv поврежден_”.
	'''
	
	def __init__(self, *args, **kwargs):
		self.message = 'Файл items.csv поврежден'
	
	def __str__(self):
		return self.message
 

class Item:
	"""
    Класс для представления товара в магазине.
    """
	pay_rate = 1.0
	all = []
	
	def __init__(self, name: str, price: float, quantity: int) -> None:
		"""
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
		self.__name = name
		self.price = price
		self.quantity = quantity
		self.all.append(self)
	
	def __repr__(self) -> str:
		'''
        Возвращает строку типа "Item('Смартфон', 10000, 20)"
        '''
		
		return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"
	
	def __str__(self):
		return self.__name
	
	def calculate_total_price(self) -> float:
		"""
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
		return self.price * self.quantity
	
	def apply_discount(self) -> None:
		"""
        Применяет установленную скидку для конкретного товара.
        """
		self.price *= self.pay_rate
	
	# Геттер для name
	@property
	def name(self):
		'''
        Возвращает значение приватной переменной __name
        '''
		return self.__name
	
	# Сеттер для __name
	@name.setter
	def name(self, name):
		'''
        Установить значение __name, если длина слова больше 10 - взять первые 10
        '''
		if len(name) > 10:
			name = name[0:10]
		self.__name = name
	
	@classmethod
	def instantiate_from_csv(cls, name_file=os.path.join('src', 'items.csv')):
		'''
        Функция инициации класса данными из файла.
        
        Реализовано в рамках конкретного задания: сделан переход для чтения файла от уровня выше
        Добавлена проверка на наличие перехода
        '''
		
		cls.all.clear()
		
		# В рамках задания и для тестирования, если нет файла по указанному пути,
		# пробуем найти его от каталога выше
		if not os.path.exists(name_file):
			name_file = os.path.join('..', name_file)

		try:
			# Читаем данные из файла csv
			with open(name_file, newline='') as csvfile:
				reader = csv.DictReader(csvfile)
				try:
					for row in reader:
						item = cls(row['name'], float(row['price']), int(row['quantity']))
				except KeyError:
					raise InstantiateCSVError
			
		except FileNotFoundError:
			raise FileNotFoundError("Отсутствует файл item.csv")
	
	@staticmethod
	def string_to_number(num: str):
		'''
        Превращаем строку-число в целое число.
        
        Если число с точкой, отрезаем лишнее после точки
        '''
		
		pos_point = num.find('.')
		if pos_point != -1:
			num = num[0:pos_point]
		return int(num)
	
	def __add__(self, other):
		'''
		Складываем два товара с проверкой принадлежности второго товара к подклассу основного
		'''
		if isinstance(other, Item):
			return self.quantity + other.quantity
		
		raise TypeError("Складывать можно только объекты классов с родительским классом Item")
