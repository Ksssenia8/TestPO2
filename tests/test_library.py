import unittest
from src.library import Library
from src.book import Book


class TestLibrary(unittest.TestCase):
    # Тестирование добавления книги в библиотеку
    def test_add_book(self):
        library = Library()
        book = Book("Программирование на Python", "Джон Доу", 2020)
        library.add_book(book)
        self.assertEqual(len(library.books), 1, "Книга не была добавлена в библиотеку")

    # Тестирование удаления книги из библиотеки
    def test_remove_book(self):
        library = Library()
        book = Book("Программирование на Python", "Джон Доу", 2020)
        library.add_book(book)
        library.remove_book(book)
        self.assertEqual(len(library.books), 0, "Книга не была удалена из библиотеки")

    # Тестирование поиска книги по названию
    def test_find_book_by_title(self):
        library = Library()
        book = Book("Изучаем Python", "Иван Иванов", 2021)
        library.add_book(book)
        found_book = library.find_book_by_title("Изучаем Python")
        self.assertEqual(found_book, book, "Книга не найдена по названию")

    # Тестирование поиска книги по несуществующему названию
    def test_find_book_by_nonexistent_title(self):
        library = Library()
        book = Book("Изучаем Python", "Иван Иванов", 2021)
        library.add_book(book)
        found_book = library.find_book_by_title("Неизвестная книга")
        self.assertIsNone(found_book, "Неверно, книга была найдена, хотя ее не существует")

    # Тестирование поиска книг по автору
    def test_search_by_author(self):
        library = Library()
        book1 = Book("Программирование на Python", "Джон Доу", 2020)
        book2 = Book("Продвинутое Python", "Джон Доу", 2021)
        book3 = Book("Java для начинающих", "Марк Смит", 2020)
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        # Проверка поиска книг по автору
        books_by_author = library.search_by_author("Джон Доу")
        self.assertEqual(len(books_by_author), 2, "Неверное количество книг найдено по автору Джон Доу")
        self.assertIn(book1, books_by_author, "Книга не найдена по автору Джон Доу")
        self.assertIn(book2, books_by_author, "Книга не найдена по автору Джон Доу")

    # Тестирование поиска книг старше определенного года
    def test_search_older_than(self):
        library = Library()
        book1 = Book("Программирование на Python", "Джон Доу", 2020)
        book2 = Book("Старый Python", "Джейн Смит", 1990)
        library.add_book(book1)
        library.add_book(book2)

        books = library.search_older_than(2000)
        self.assertEqual(len(books), 1, "Неверное количество книг старше 2000 года")
        self.assertEqual(books[0].title, "Старый Python", "Книга с нужным годом не найдена")

    # Тестирование метода get_books (получение всех книг из библиотеки)
    def test_get_books(self):
        library = Library()
        book1 = Book("Программирование на Python", "Джон Доу", 2020)
        book2 = Book("Старый Python", "Джейн Смит", 1990)
        library.add_book(book1)
        library.add_book(book2)

        all_books = library.get_books()
        self.assertEqual(len(all_books), 2, "Неверное количество книг в библиотеке")
        self.assertIn(book1, all_books, "Книга не найдена в списке всех книг")
        self.assertIn(book2, all_books, "Книга не найдена в списке всех книг")


class TestLibraryIntegration(unittest.TestCase):

    # Тестирование добавления книги в библиотеку
    def test_add_book_to_library(self):
        book = Book("Изучаем Python", "Иван Иванов", 2021)
        library = Library()

        library.add_book(book)

        # Проверка, что книга была добавлена в библиотеку
        self.assertIn(book, library.books, "Книга не была добавлена в библиотеку")

    # Тестирование поиска книги по названию
    def test_find_book_by_title(self):
        book = Book("Изучаем Python", "Иван Иванов", 2021)
        library = Library()

        library.add_book(book)

        # Проверка поиска книги по названию
        found_book = library.find_book_by_title("Изучаем Python")
        self.assertEqual(found_book, book, "Книга не найдена по названию")

    # Тестирование удаления книги из библиотеки
    def test_remove_book_from_library(self):
        book = Book("Изучаем Python", "Иван Иванов", 2021)
        library = Library()

        library.add_book(book)
        library.remove_book(book)

        # Проверка, что книга была удалена
        self.assertNotIn(book, library.books, "Книга не была удалена из библиотеки")



if __name__ == "__main__":
    unittest.main()
