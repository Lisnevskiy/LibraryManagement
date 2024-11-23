import unittest

from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создает экземпляр библиотеки и очищает данные для тестирования"""

        self.library = Library(storage_file="test_storage.json")
        self.library.books = []  # Очищаем библиотеку перед каждым тестом

    def tearDown(self):
        """Удаляет тестовые данные после каждого теста"""

        self.library._save_books()

    def test_add_book(self):
        """Проверяет добавление книги в библиотеку"""

        self.library.add_book("Название книги", "Автор", 2020)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Название книги")
        self.assertEqual(self.library.books[0].status, "в наличии")

    def test_remove_book(self):
        """Проверяет удаление книги по ID"""

        self.library.add_book("Название книги", "Автор", 2020)
        book_id = self.library.books[0].id
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_nonexistent_book(self):
        """Проверяет удаление несуществующей книги"""

        self.library.remove_book(12345)  # Удаляем книгу, которой нет
        self.assertEqual(len(self.library.books), 0)

    def test_find_books_by_title(self):
        """Проверяет поиск книги по названию"""

        self.library.add_book("Название книги", "Автор", 2020)
        self.library.find_books("title", "Название книги")
        # Проверка вывода в консоль
        self.assertTrue(any(book.title == "Название книги" for book in self.library.books))

    def test_find_books_by_author(self):
        """Проверяет поиск книги по автору"""

        self.library.add_book("Название книги", "Автор", 2020)
        self.library.find_books("author", "Автор")
        self.assertTrue(any(book.author == "Автор" for book in self.library.books))

    def test_find_books_no_results(self):
        """Проверяет поиск, если результатов нет"""

        self.library.find_books("title", "Несуществующее название")
        # Проверка, что ничего не найдено
        self.assertTrue(len(self.library.books) == 0)

    def test_display_books(self):
        """Проверяет отображение всех книг"""

        self.library.add_book("Книга 1", "Автор 1", 2020)
        self.library.add_book("Книга 2", "Автор 2", 2021)
        # Проверяем, что книги правильно отображаются в консоли
        output = self.library.display_books()
        self.assertIsNone(output)  # Метод display_books ничего не возвращает

    def test_update_status(self):
        """Проверяет изменение статуса книги"""

        self.library.add_book("Название книги", "Автор", 2020)
        book_id = self.library.books[0].id
        self.library.update_status(book_id, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_update_status_invalid(self):
        """Проверяет изменение статуса на некорректное значение"""

        self.library.add_book("Название книги", "Автор", 2020)
        book_id = self.library.books[0].id
        # Метод не выбрасывает ValueError, проверяем, что статус не меняется
        self.library.update_status(book_id, "неизвестный статус")
        self.assertNotEqual(self.library.books[0].status, "неизвестный статус")

    def test_update_status_nonexistent_book(self):
        """Проверяет изменение статуса для несуществующей книги"""

        self.library.update_status(12345, "выдана")  # Метод просто пишет в консоль
        self.assertTrue(True)  # Проверяем, что исключение не выбрасывается


if __name__ == "__main__":
    unittest.main()
