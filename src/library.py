# src/library.py
class Library:
    def __init__(self):
        self.books = []  # Список для хранения книг

    def add_book(self, book):
        """Добавление книги в библиотеку"""
        self.books.append(book)

    def find_book_by_title(self, title):
        """Поиск книги по названию"""
        for book in self.books:
            if book.title == title:
                return book
        return None  # Если книга не найдена, возвращаем None

    def remove_book(self, book):
        """Удаление книги из библиотеки"""
        if book in self.books:
            self.books.remove(book)

    def search_by_author(self, author):
        """Поиск книг по автору"""
        return [book for book in self.books if book.author == author]

    def search_older_than(self, year):
        """Поиск книг, выпущенных раньше указанного года"""
        return [book for book in self.books if book.year < year]

    def get_books(self):
        """Возвращает все книги в библиотеке"""
        return self.books
