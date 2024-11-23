import json


class Book:
    """Представляет книгу в библиотеке"""

    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        """Инициализирует объект книги"""

        self.id: int = id(self)
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    def to_dict(self) -> dict[str, str | int]:
        """Преобразует объект книги в словарь"""

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict[str, str | int]) -> "Book":
        """Создает объект книги из словаря"""

        book = Book(data["title"], data["author"], data["year"], data["status"])
        book.id = data["id"]
        return book


class Library:
    """Управляет коллекцией книг в библиотеке"""

    def __init__(self, storage_file: str = "storage.json"):
        """Инициализирует библиотеку и загружает данные из файла"""

        self.storage_file = storage_file
        self.books: list[Book] = self._load_books()

    def _load_books(self) -> list[Book]:
        """Загружает данные о книгах из файла"""

        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                return [Book.from_dict(book) for book in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_books(self):
        """Сохраняет данные о книгах в файл"""

        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет новую книгу в библиотеку"""

        new_book = Book(title, author, year)
        self.books.append(new_book)
        self._save_books()
        print(f"Книга '{title}' добавлена с ID {new_book.id}.")

    def remove_book(self, book_id: int):
        """Удаляет книгу из библиотеки по ее ID"""

        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self._save_books()
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def find_books(self, key: str, value: str | int):
        """Ищет книги по заданному ключу и значению"""

        results = [book for book in self.books if str(getattr(book, key, "")).lower() == str(value).lower()]
        if results:
            for book in results:
                print(book.to_dict())
        else:
            print("Книги по данному запросу не найдены.")

    def display_books(self):
        """Отображает список всех книг в библиотеке"""

        if self.books:
            for book in self.books:
                print(book.to_dict())
        else:
            print("Библиотека пуста.")

    def update_status(self, book_id: int, new_status: str):
        """Обновляет статус книги по ее ID"""

        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self._save_books()
                    print(f"Статус книги с ID {book_id} обновлен на '{new_status}'.")
                    return
                else:
                    print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")
                    return
        print(f"Книга с ID {book_id} не найдена.")
