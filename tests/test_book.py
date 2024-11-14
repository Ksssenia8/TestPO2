import unittest
from src.book import Book
from src.library import Library


class TestBook(unittest.TestCase):

    # Тестирование создания книги
    def test_book_creation(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        self.assertEqual(book.title, "Программирование на Python", "Название книги не совпадает")
        self.assertEqual(book.author, "Джон Доу", "Автор книги не совпадает")
        self.assertEqual(book.year, 2020, "Год выпуска книги не совпадает")

    # Тестирование метода is_older_than
    def test_is_older_than(self):
        book = Book("Старый Python", "Джейн Смит", 1990)
        self.assertTrue(book.is_older_than(2000), "Книга должна быть старше 2000 года")
        self.assertFalse(book.is_older_than(1980), "Книга не должна быть старше 1980 года")

    # Тестирование метода is_older_than для книг, выпущенных в том же году
    def test_is_older_than_same_year(self):
        book = Book("Современный Python", "Джон Доу", 2020)
        self.assertFalse(book.is_older_than(2020), "Книга не должна быть старше 2020 года")

    # Тестирование метода __str__
    def test_str_method(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        expected_str = "Book(title='Программирование на Python', author='Джон Доу', year=2020)"
        self.assertEqual(str(book), expected_str, "__str__ метод возвращает неправильную строку")

    # Тестирование изменения года выпуска
    def test_change_year(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        book.year = 2021
        self.assertEqual(book.year, 2021, "Год книги не был изменен")


class TestBookAcceptance(unittest.TestCase):

    # Тестирование функциональности, которую ожидает пользователь
    def test_create_and_check_book(self):
        book = Book("Изучаем Python", "Иван Иванов", 2021)
        # Пользователь ожидает, что книга будет иметь правильные аттрибуты
        self.assertEqual(book.title, "Изучаем Python", "Название книги не соответствует ожиданиям")
        self.assertEqual(book.author, "Иван Иванов", "Автор книги не соответствует ожиданиям")
        self.assertEqual(book.year, 2021, "Год книги не соответствует ожиданиям")

    def test_is_older_than_acceptance(self):
        # Тестирование функции для более старых книг
        book = Book("Секреты Python", "Петр Петров", 1999)
        self.assertTrue(book.is_older_than(2000), "Книга должна быть старше 2000 года по версии бизнеса")

if __name__ == "__main__":
    unittest.main()
