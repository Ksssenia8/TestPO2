import unittest
from src.author import Author
#проверка
class TestAuthorAdditional(unittest.TestCase):

    def test_add_book_updates_books_written(self):
        author = Author("Антон Чехов", 1860, 5)
        author.update_books_written(3)
        self.assertEqual(author.books_written, 8, "Количество написанных книг должно быть 8")

    def test_is_alive_edge_case(self):
        author = Author("Жюль Верн", 1900)
        self.assertFalse(author.is_alive(2020), "Автор не должен быть жив спустя 120 лет")

    def test_add_book_negative_case(self):
        author = Author("Александр Пушкин", 1799)
        with self.assertRaises(ValueError):
            author.update_books_written(-3)

    def test_get_info_output_format(self):
        author = Author("Фёдор Достоевский", 1821, 10)
        expected_output = "Фёдор Достоевский, born in 1821, books written: 10"
        self.assertEqual(author.get_info(), expected_output, "Информация об авторе в неправильном формате")
