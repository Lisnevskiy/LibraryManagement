from library import Library


def main():
    """
    Главная функция для управления библиотекой.
    Позволяет взаимодействовать с пользователем через консольное меню для выполнения операций с книгами.

    Доступные операции:
    1. Добавление книги.
    2. Удаление книги.
    3. Поиск книги.
    4. Отображение всех книг.
    5. Изменение статуса книги.
    6. Выход из программы.
    """

    library = Library()

    while True:
        print("\n--- Управление библиотекой ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания: "))
                library.add_book(title, author, year)

            elif choice == "2":
                book_id = int(input("Введите ID книги: "))
                library.remove_book(book_id)

            elif choice == "3":
                key = input("Введите критерий поиска (title, author, year): ")
                value = input("Введите значение для поиска: ")
                library.find_books(key, value)

            elif choice == "4":
                library.display_books()

            elif choice == "5":
                book_id = int(input("Введите ID книги: "))
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                library.update_status(book_id, new_status)

            elif choice == "6":
                print("Выход из программы.")
                break

            else:
                print("Некорректный ввод. Попробуйте снова.")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
