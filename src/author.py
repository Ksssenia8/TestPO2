# src/author.py

class Author:
    def __init__(self, name, birth_year, books_written=0):
        self.name = name
        self.birth_year = birth_year
        self.books_written = books_written

    def __hash__(self):
        # Хешируем объект на основе имени и года рождения
        return hash((self.name, self.birth_year))

    def __eq__(self, other):
        # Сравниваем объекты по имени и году рождения
        return (self.name == other.name) and (self.birth_year == other.birth_year)

    def __str__(self):
        return self.name

    def is_alive(self, current_year):
        """Предполагает, что автор жив, если ему менее 120 лет."""
        return (current_year - self.birth_year) < 120

    def update_books_written(self, additional_books):
        """Обновляет количество книг, написанных автором."""
        if additional_books < 0:
            raise ValueError("Количество дополнительных книг не может быть отрицательным")
        self.books_written += additional_books

    def get_info(self):
        """Возвращает строку с информацией об авторе."""
        return f"{self.name}, born in {self.birth_year}, books written: {self.books_written}"

    def __eq__(self, other):
        """Сравнивает двух авторов по имени и дате рождения."""
        return self.name == other.name and self.birth_year == other.birth_year

