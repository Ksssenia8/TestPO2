import unittest
from src.author import Author
from src.book import Book


class TestBook(unittest.TestCase):

    # Тестирование создания книги с заданными параметрами
    def test_book_creation(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        self.assertEqual(book.title, "Программирование на Python", "Название книги не совпадает")
        self.assertEqual(book.author, "Джон Доу", "Автор книги не совпадает")
        self.assertEqual(book.year, 2020, "Год выпуска книги не совпадает")

    # Тестирование метода is_older_than для проверки, что книга старше указанного года
    def test_is_older_than(self):
        book = Book("Старый Python", "Джейн Смит", 1990)
        self.assertTrue(book.is_older_than(2000), "Книга должна быть старше 2000 года")
        self.assertFalse(book.is_older_than(1980), "Книга не должна быть старше 1980 года")

    # Тестирование метода is_newer_than для проверки, что книга новее указанного года
    def test_is_newer_than(self):
        book = Book("Продвинутое Python", "Джон Доу", 2022)
        self.assertTrue(book.is_newer_than(2020), "Книга должна быть новее 2020 года")
        self.assertFalse(book.is_newer_than(2025), "Книга не должна быть новее 2025 года")

    # Тестирование метода is_same_author для проверки авторства
    def test_is_same_author(self):
        book1 = Book("Python для начинающих", "Джон Доу", 2020)
        book2 = Book("Продвинутое Python", "Джон Доу", 2021)
        book3 = Book("Основы Python", "Иван Иванов", 2019)

        self.assertTrue(book1.is_same_author(book2), "Книги должны быть от одного автора")
        self.assertFalse(book1.is_same_author(book3), "Книги не должны быть от одного автора")

    # Тестирование метода get_book_info для получения корректной информации о книге
    def test_get_book_info(self):
        book = Book("Продвинутое программирование", "Иван Иванов", 2023)
        expected_info = "'Продвинутое программирование' by Иван Иванов, published in 2023"
        self.assertEqual(book.get_book_info(), expected_info, "Информация о книге неправильная")

    # Тестирование метода update_author для изменения автора книги
    def test_update_author(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        book.update_author("Алексей Алексеев")
        self.assertEqual(book.author, "Алексей Алексеев", "Автор книги не обновился")

    # Тестирование метода is_equal для проверки, одинаковые ли книги
    def test_is_equal(self):
        book1 = Book("Python для начинающих", "Джон Доу", 2020)
        book2 = Book("Python для начинающих", "Джон Доу", 2020)
        book3 = Book("Основы Python", "Иван Иванов", 2021)

        self.assertTrue(book1.is_equal(book2), "Книги должны быть одинаковыми")
        self.assertFalse(book1.is_equal(book3), "Книги не должны быть одинаковыми")

    # Дополнительные тесты

    # Тестирование формата строки книги с жанром и языком
    def test_str_with_genre_and_language(self):
        book = Book("Программирование на Python", "Джон Доу", 2020, "Programming", "Russian")
        expected_str = "Программирование на Python (2020) - Джон Доу - Programming - Russian"
        self.assertEqual(str(book), expected_str, "Формат строки с жанром и языком неверен")

    # Тестирование формата строки книги без жанра и языка
    def test_str_without_genre_and_language(self):
        book = Book("Основы Python", "Джон Доу", 2020)
        expected_str = "Основы Python (2020) - Джон Доу - None - None"
        self.assertEqual(str(book), expected_str, "Формат строки без жанра и языка неверен")

    # Тестирование метода is_older_than для книги, которая не должна быть старше указанного года
    def test_is_older_than_same_year(self):
        book = Book("Старый Python", "Джейн Смит", 1990)
        self.assertFalse(book.is_older_than(1990), "Книга не должна быть старше 1990 года")

    # Тестирование метода is_newer_than для книги, которая не должна быть новее указанного года
    def test_is_newer_than_same_year(self):
        book = Book("Старый Python", "Джейн Смит", 1990)
        self.assertFalse(book.is_newer_than(1990), "Книга не должна быть новее 1990 года")

    # Тестирование метода get_book_info без жанра и языка
    def test_get_book_info_without_genre_and_language(self):
        book = Book("Основы Python", "Джон Доу", 2020)
        expected_info = "'Основы Python' by Джон Доу, published in 2020"
        self.assertEqual(book.get_book_info(), expected_info,
                         "Информация о книге с отсутствующими жанром и языком неверна")

    # Тестирование метода update_author для случая, когда автор не изменяется
    def test_update_author_to_same_author(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        book.update_author("Джон Доу")
        self.assertEqual(book.author, "Джон Доу", "Автор книги не обновился корректно")

    # Тестирование метода is_equal для книг с разными годами
    def test_is_equal_different_year(self):
        book1 = Book("Python для начинающих", "Джон Доу", 2020)
        book2 = Book("Python для начинающих", "Джон Доу", 2021)
        self.assertFalse(book1.is_equal(book2), "Книги с разными годами не должны быть одинаковыми")

    # Тестирование метода is_equal для книг с разными названиями
    def test_is_equal_different_title(self):
        book1 = Book("Python для начинающих", "Джон Доу", 2020)
        book2 = Book("Продвинутое программирование на Python", "Джон Доу", 2020)
        self.assertFalse(book1.is_equal(book2), "Книги с разными названиями не должны быть одинаковыми")

    # Тестирование метода is_same_author для случая с None в качестве автора
    def test_is_same_author_with_none(self):
        book1 = Book("Python для начинающих", None, 2020)
        book2 = Book("Основы Python", "Иван Иванов", 2020)
        self.assertFalse(book1.is_same_author(book2), "Книги с автором None не должны быть от одного автора")

    # Тестирование метода is_older_than для будущих годов
    def test_is_older_than_future_year(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        self.assertTrue(book.is_older_than(9999), "Книга должна быть старше 9999 года")

    # Тестирование метода update_author для пустой строки
    def test_update_author_empty_string(self):
        book = Book("Программирование на Python", "Джон Доу", 2020)
        book.update_author("")
        self.assertEqual(book.author, "", "Автор книги не обновился на пустую строку")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
