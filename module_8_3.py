class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        self.message = message


class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        """
        :param model: название автомобиля (строка)
        :param vin: vin номер автомобиля (целое число). Уровень доступа private.
        :param numbers: номера автомобиля (строка).
        """
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.model = model
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number: int) -> bool:
        """
        Уровень доступа private. Проверяет vin_number на корректность.
        :param vin_number: vin номер автомобиля (целое число)
        :return: True, если корректный, в других случаях выбрасывает исключение.
        """
        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')

        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        # если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, numbers: str) -> bool:
        """
        Уровень доступа private. Проверяет numbers на корректность.
        :param numbers: номера автомобиля (строка).
        :return: True, если корректный, в других случаях выбрасывает исключение.
        """
        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка.
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True


def test():
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    """
    Вывод на консоль:
    Model1 успешно создан
    Неверный диапазон для vin номера
    Неверная длина номера
    """


if __name__ == '__main__':
    test()


"""
2023/11/26 00:00|Домашнее задание по теме "Создание исключений"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи. Повторить тему ООП и принцип инкапсуляции.

Задача "Некорректность":

Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.
__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.

ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при объявлении атрибутов __vin и __numbers).

Пример результата выполнения программы:
Пример выполняемого кода:
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
Вывод на консоль:
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера

Примечания:
Для выбрасывания исключений используйте оператор raise
Файл module_8_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""