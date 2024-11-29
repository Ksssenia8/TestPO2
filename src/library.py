class Library:
    def __init__(self):
        self.books = []  # Список для хранения книг
        self.author_books_count = {}  # Словарь для хранения количества книг каждого автора

    def add_book(self, book):
        """Добавление книги в библиотеку"""
        self.books.append(book)

        # Обновляем количество книг у автора
        if book.author in self.author_books_count:
            self.author_books_count[book.author] += 1
        else:
            self.author_books_count[book.author] = 1

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

            # Уменьшаем количество книг у автора
            if book.author in self.author_books_count:
                self.author_books_count[book.author] -= 1
                # Если у автора не осталось книг, удаляем его из словаря
                if self.author_books_count[book.author] == 0:
                    del self.author_books_count[book.author]

    def search_by_author(self, author):
        """Поиск книг по автору"""
        return [book for book in self.books if book.author == author]

    def search_older_than(self, year):
        """Поиск книг, выпущенных раньше указанного года"""
        return [book for book in self.books if book.year < year]

    def search_by_title(self, title):
        """Поиск книги по названию"""
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_year(self, year):
        """Поиск книг, выпущенных в определённом году"""
        return [book for book in self.books if book.year == year]

    def search_by_keyword(self, keyword):
        """Поиск книг с ключевым словом в названии"""
        return [book for book in self.books if keyword.lower() in book.title.lower()]

    def search_by_genre(self, genre):
        """Поиск книг по жанру"""
        return [book for book in self.books if book.genre and genre.lower() in book.genre.lower()]

    def search_by_language(self, language):
        """Поиск книг по языку программирования (предположим, что язык в жанре)"""
        return [book for book in self.books if book.language and language.lower() in book.language.lower()]

    def get_books(self):
        """Возвращает все книги в библиотеке"""
        return self.books

    def get_books_count_by_author(self, author):
        """Возвращает количество книг у автора"""
        return self.author_books_count.get(author, 0)

