import csv

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
    def instantiate_from_csv(cls, name_file):
        '''
        Функция инициации класса данными из файла
        Реализовано в рамках конкретного задания: сделан переход для чтения файла от уровня выше
        Добавлена проверка на наличие перехода
        '''
        
        cls.all.clear()
        if name_file[0:2] != '..':
            name_file = '../' + name_file
        
        with open(name_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
    
    @staticmethod
    def string_to_number(num: str):
        '''
        Превращаем строку-число в целое число
        Если число с точкой, отрезаем лишнее после точки
        '''
        
        pos_point = num.find('.')
        if pos_point != -1:
            num = num[0:pos_point]
        return int(num)
