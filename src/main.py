from src.book import Book
from src.library import Library


def main():
    # Создание библиотеки и добавление книг
    library = Library()

    # Добавление книг
    # Добавление книг с жанрами и языками
    book1 = Book("Программирование на Python", "Джон До", 2020, genre="Программирование", language="Python")
    book2 = Book("Продвинутый Python", "Джон До", 2021, genre="Программирование", language="Python")
    book3 = Book("Старый Python", "Джейн Смит", 1990, genre="Программирование", language="Python")
    book4 = Book("Машинное обучение", "Энн Ли", 2018, genre="Программирование", language="Python")
    book5 = Book("Искусственный интеллект", "Энн Ли", 2015, genre="Программирование", language="Python")
    book6 = Book("Программирование на C++", "Майкл Браун", 2005, genre="Программирование", language="C++")
    book7 = Book("Основы Java", "Лиза Уайт", 1998, genre="Программирование", language="Java")
    book8 = Book("Алгоритмы и структуры данных", "Джеймс Блэк", 2012, genre="Программирование", language="Java")
    book9 = Book("Разработка игр", "Кейт Грей", 2023, genre="Программирование", language="Python")
    book10 = Book("История IT", "Томас Грин", 1985, genre="История", language="Русский")
    book11 = Book("Базы данных для начинающих", "Мария Иванова", 2010, genre="Программирование", language="Python")
    book12 = Book("Основы HTML и CSS", "Джеймс Блэк", 2008, genre="Веб-разработка", language="HTML/CSS")
    book13 = Book("Основы JavaScript", "Лиза Уайт", 2011, genre="Веб-разработка", language="JavaScript")
    book14 = Book("Кибербезопасность", "Энн Ли", 2019, genre="Безопасность", language="English")
    book15 = Book("Программирование игр", "Джон До", 2022, genre="Программирование", language="Python")
    book16 = Book("Java для начинающих", "Джон Смит", 2007, genre="Программирование", language="Java")
    book17 = Book("Python для начинающих", "Лиза Смарт", 2020, genre="Программирование", language="Python")
    book18 = Book("Теория графов", "Майкл Джейкобс", 2015, genre="Математика", language="English")
    book19 = Book("Объектно-ориентированное программирование", "Стивен Парк", 2016, genre="Программирование",
                  language="Java")
    book20 = Book("Интернет вещей", "Майкл Браун", 2021, genre="Технологии", language="English")
    book21 = Book("Системы искусственного интеллекта", "Энн Ли", 2020, genre="Искусственный интеллект",
                  language="English")
    book22 = Book("Глубокое обучение", "Джон Беннет", 2018, genre="Искусственный интеллект", language="English")
    book23 = Book("Алгоритмы и их применения", "Роберт Хилл", 2017, genre="Программирование", language="English")
    book24 = Book("Основы математического анализа", "Сара Фергюсон", 2013, genre="Математика", language="English")
    book25 = Book("Введение в базы данных", "Питер Смит", 2009, genre="Программирование", language="English")

    # Добавляем книги в библиотеку
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    library.add_book(book7)
    library.add_book(book8)
    library.add_book(book9)
    library.add_book(book10)
    library.add_book(book11)
    library.add_book(book12)
    library.add_book(book13)
    library.add_book(book14)
    library.add_book(book15)
    library.add_book(book16)
    library.add_book(book17)
    library.add_book(book18)
    library.add_book(book19)
    library.add_book(book20)
    library.add_book(book21)
    library.add_book(book22)
    library.add_book(book23)
    library.add_book(book24)
    library.add_book(book25)

    # Поиск книг по автору
    books_by_author = library.search_by_author("Джон До")
    print("Книги Джона До:")
    for book in books_by_author:
        print(book)

    # Поиск книг старше 2000 года
    old_books = library.search_older_than(2000)
    print("Книги старше 2000 года:")
    for book in old_books:
        print(book)

    # Поиск книг по названию
    books_by_title = library.search_by_title("Основы Java")
    print("Книги с названием 'Основы Java':")
    for book in books_by_title:
        print(book)

    # Поиск книг, выпущенных в 2018 году
    books_by_year = library.search_by_year(2018)
    print("Книги, выпущенные в 2018 году:")
    for book in books_by_year:
        print(book)

    # Поиск книг по ключевому слову
    books_with_word = library.search_by_keyword("Основы")
    print("Книги с ключевым словом 'Основы':")
    for book in books_with_word:
        print(book)

    # Поиск книг по жанру (предположим, что у книг есть жанры)
    # Допустим, метод search_by_genre реализован в библиотеке
    books_by_genre = library.search_by_genre("Программирование")
    print("Книги в жанре 'Программирование':")
    for book in books_by_genre:
        print(book)

    # Поиск книг по языку (предположим, что добавлен метод поиска по языку)
    books_by_language = library.search_by_language("Python")
    print("Книги на тему 'Python':")
    for book in books_by_language:
        print(book)

    # Получение количества книг для автора "Джон До"
    print(f"Количество книг у Джона Доу: {library.get_books_count_by_author('Джон До')}")

    # Перебор всех авторов и их количества книг
    for author_name, count in library.author_books_count.items():
        print(f"Автор: {author_name}, Количество книг: {count}")

if __name__ == "__main__":
    main()
