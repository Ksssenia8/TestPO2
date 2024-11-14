class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def is_older_than(self, year):
        """Проверить, старше ли книга заданного года."""
        return self.year < year
