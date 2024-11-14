from library import Library
from book import Book
#проверка при пуше

def main():
    # Создание библиотеки
    library = Library()

    # Добавление книг
    book1 = Book("Python Programming", "John Doe", 2020)
    book2 = Book("Advanced Python", "John Doe", 2021)
    book3 = Book("Old Python", "Jane Smith", 1990)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Поиск книг по автору
    books_by_author = library.search_by_author("John Doe")
    print(f"Books by John Doe: {books_by_author}")

    # Поиск книг старше 2000 года
    old_books = library.search_older_than(2000)
    print(f"Books older than 2000: {old_books}")


if __name__ == "__main__":
    main()
