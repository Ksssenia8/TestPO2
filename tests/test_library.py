import unittest

from src.book import Book
from src.library import Library


class TestLibrary(unittest.TestCase):

    # Тестирование поиска книги по части названия
    def test_search_by_title_part(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        book2 = Book("Основы Python", "Иван Иванов", 2020)
        library.add_book(book1)
        library.add_book(book2)

        # Проверка поиска по части названия
        found_books = library.search_by_title("Python")
        self.assertEqual(len(found_books), 2, "Не все книги найдены по части названия")
        self.assertIn(book1, found_books, "Книга 'Изучаем Python' не найдена")
        self.assertIn(book2, found_books, "Книга 'Основы Python' не найдена")

    # Тестирование поиска по году
    def test_search_by_year(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        book2 = Book("Основы Python", "Иван Иванов", 2020)
        library.add_book(book1)
        library.add_book(book2)

        # Проверка поиска книг по году
        books_2021 = library.search_by_year(2021)
        self.assertEqual(len(books_2021), 1, "Неверное количество книг за 2021 год")
        self.assertIn(book1, books_2021, "Книга 'Изучаем Python' не найдена за 2021 год")

    # Тестирование поиска книг старше определенного года
    def test_search_older_than_empty(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        library.add_book(book1)

        # Проверка поиска книг старше определенного года, когда нет таких книг
        books = library.search_older_than(2000)
        self.assertEqual(len(books), 0, "Не должно быть книг старше 2000 года")

    # Тестирование получения количества книг по автору
    def test_get_books_count_by_author(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        book2 = Book("Основы Python", "Иван Иванов", 2020)
        library.add_book(book1)
        library.add_book(book2)

        # Проверка количества книг у автора
        count = library.get_books_count_by_author("Иван Иванов")
        self.assertEqual(count, 2, "Неверное количество книг у автора Иван Иванов")

    # Тестирование удаления книги, которой нет в библиотеке
    def test_remove_non_existent_book(self):
        library = Library()
        book = Book("Программирование на Python", "Джон Доу", 2020)

        # Пытаемся удалить книгу, которой нет в библиотеке
        library.remove_book(book)

        # Проверка, что библиотека осталась пустой
        self.assertEqual(len(library.books), 0, "Невозможно удалить книгу, которой нет в библиотеке")

    # Тестирование удаления всех книг из библиотеки
    def test_remove_all_books(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        book2 = Book("Основы Python", "Иван Иванов", 2020)
        library.add_book(book1)
        library.add_book(book2)

        # Удаление всех книг
        library.remove_book(book1)
        library.remove_book(book2)

        # Проверка, что библиотека пуста
        self.assertEqual(len(library.books), 0, "Библиотека не пуста после удаления всех книг")

    # Тестирование поиска книг по жанру
    def test_search_by_genre(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        book2 = Book("Основы Python", "Иван Иванов", 2020)
        book1.genre = "Программирование"
        book2.genre = "Наука"
        library.add_book(book1)
        library.add_book(book2)

        # Проверка поиска книг по жанру
        books_genre = library.search_by_genre("Программирование")
        self.assertEqual(len(books_genre), 1, "Неверное количество книг по жанру 'Программирование'")
        self.assertIn(book1, books_genre, "Книга 'Изучаем Python' не найдена по жанру 'Программирование'")

    # Тестирование поиска книг по языку программирования
    def test_search_by_language(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        book2 = Book("Основы Java", "Марк Смит", 2020)
        book1.language = "Python"
        book2.language = "Java"
        library.add_book(book1)
        library.add_book(book2)

        # Проверка поиска книг по языку программирования
        books_language = library.search_by_language("Python")
        self.assertEqual(len(books_language), 1, "Неверное количество книг по языку Python")
        self.assertIn(book1, books_language, "Книга 'Изучаем Python' не найдена по языку Python")

    # Тестирование поиска книг по ключевому слову в названии
    def test_search_by_keyword(self):
        library = Library()
        book1 = Book("Изучаем Python", "Иван Иванов", 2021)
        book2 = Book("Основы Python", "Иван Иванов", 2020)
        library.add_book(book1)
        library.add_book(book2)

        # Проверка поиска книг по ключевому слову в названии
        books_keyword = library.search_by_keyword("Основы")
        self.assertEqual(len(books_keyword), 1, "Неверное количество книг найдено по ключевому слову 'Основы'")
        self.assertIn(book2, books_keyword, "Книга 'Основы Python' не найдена по ключевому слову 'Основы'")
