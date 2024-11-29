class Book:
    def __init__(self, title, author, year, genre=None, language=None):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre  # Новый атрибут для жанра
        self.language = language  # Новый атрибут для языка


    def __str__(self):
        return f"{self.title} ({self.year}) - {self.author} - {self.genre} - {self.language}"

    # Другие методы могут оставаться без изменений

    def is_older_than(self, year):
        """Проверить, старше ли книга заданного года."""
        return self.year < year

    def is_newer_than(self, year):
        """Проверить, новее ли книга заданного года."""
        return self.year > year

    def is_same_author(self, other_book):
        """Сравнить автора с другой книгой."""
        return self.author == other_book.author

    def get_book_info(self):
        """Возвращает строку с полной информацией о книге."""
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def update_author(self, new_author):
        """Обновить автора книги."""
        self.author = new_author

    def is_equal(self, other_book):
        """Проверяет, одинаковы ли две книги (по названию, автору и году)."""
        return self.title == other_book.title and self.author == other_book.author and self.year == other_book.year
