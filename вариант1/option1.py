class Book:
    """класс хранит название книги, автора, количество страниц и показывает информацию о книге"""

    def __init__(self, title: str = 'Неизвестная книга', author: str = 'Неизвестный автор', pages: str ="Неизвестное количество страниц") -> None:
        """
        Метод инициализации объекта класса
        Args:
            title: названеие книги
            author: автор книги
            pages: количество страниц
        """
        self.__title = title
        self.__author = author
        self.__pages = pages

    def set_title(self, new_title: str) -> None:
        """
        Сеттер названия книги
        Args:
            new_title: новое название книги
        """
        while new_title.strip() == '':
            print('Ошибка: Название книги не может быть пустым. Попробуйте еще раз!')
            new_title = input()
        self.__title = new_title.strip()

    def get_title(self) -> str:
        """
        Геттер названия книги
        :return: название книги
        """
        return self.__title

    def set_author(self, new_author: str) -> None:
        """
        Сеттер автора книги
        Args:
            new_author: новый автор книги
        """
        while new_author.strip() == '':
            print('Ошибка: Имя автора не может быть пустым. Попробуйте еще раз!')
            new_author = input()
        self.__author = new_author.strip()

    def get_author(self) -> str:
        """
        Геттер автора книги
        :return: автор книги
        """
        return self.__author

    def set_pages(self, new_pages) -> None:
        """
        Сеттер количества страниц
        Args:
            new_pages: новое количество страниц
        """
        while (new_pages.isdigit() == False) or ((new_pages.isdigit()) and (int(new_pages) <= 0)):
            print('Ошибка: Количество страниц должно превышать нулевое значение. Попробуйте еще раз!')
            new_pages = input()
        self.__pages = int(new_pages.strip())

    def get_pages(self) -> str | int:
        """
        Геттер количества страниц
        :return: количество страниц
        """
        return self.__pages

    def amount_words(self) -> str:
        """
        Подсчет примерного количества слов в книге
        :return: примерное количество слов
        """
        return f"Примерное количество слов {self.get_pages() * 300}"

    def is_big_book(self) -> None:
        """Метод на проверку размера книги по объему"""
        if self.get_pages() > 200:
            print('Книга здоровенная (больше 200 страниц)')
        else:
            print('Книга малюсенькая (меньше 200 страниц)')

    def show_information(self, number: int) -> None:
        """Метод, показывающий всю информацию о текущей книге"""
        print(f'\n--- ИНФОРМАЦИЯ О КНИГЕ {number}---')
        print('Название книги:', self.get_title())
        print('Автор книги:', self.get_author())
        print('Количество страниц:', self.get_pages())


class Menu:
    """Класс для взаимодействия пользователя с меню"""
    def __init__(self) -> None:
        """Метод инициализации объекта класса"""
        self.book1 = Book()
        self.book2 = Book()
        self.book3 = Book()

    def correct_number(self) -> None:
        """Метод на проверку корректно введенного номера"""
        while (number := input('Выберите книгу (1, 2 или 3): ')) not in ('1', '2', '3'):
            print('Ошибка! Введите корректный номер книги')
        self.number = number

    def run(self) -> None:
        """Метод, делающий меню интерактивным"""
        while True:
            print('\n--- МЕНЮ ---')
            print('1. Показать книги')
            print('2. Изменить книгу')
            print('3. Посчитать количество слов')
            print('4. Проверить размер книги')
            print('5. Выход')

            choice = input('Выберите действие: ')

            if choice == '1':
                self.book1.show_information(1)
                self.book2.show_information(2)
                self.book3.show_information(3)

            elif choice == '2':
                self.correct_number()
                if self.number == '1':
                    book = self.book1
                elif self.number == '2':
                    book = self.book2
                else:
                    book = self.book3

                title = input('Введите название: ')
                author = input('Введите автора: ')
                pages = input('Введите количество страниц: ')

                book.set_title(title)
                book.set_author(author)
                book.set_pages(pages)

            elif choice == '3':
                self.correct_number()
                sp = [self.book1.get_pages(), self.book2.get_pages(), self.book3.get_pages()]
                if sp[int(self.number) - 1] == 'Неизвестное количество страниц':
                    print('У этой книги нет информации')
                elif self.number == '1':
                    print(self.book1.amount_words())
                elif self.number == '2':
                    print(self.book2.amount_words())
                else:
                    print(self.book3.amount_words())

            elif choice == '4':
                self.correct_number()
                sp = [self.book1.get_pages(), self.book2.get_pages(), self.book3.get_pages()]
                if sp[int(self.number) - 1] == 'Неизвестное количество страниц':
                    print('У этой книги нет информации')
                elif self.number == '1':
                    self.book1.is_big_book()
                elif self.number == '2':
                    self.book2.is_big_book()
                else:
                    self.book3.is_big_book()

            elif choice == '5':
                print('Программа завершена.')
                break

            else:
                print('Неверный пункт меню!')


menu = Menu()
menu.run()