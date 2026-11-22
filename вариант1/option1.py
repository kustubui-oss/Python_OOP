class Book:
    def __init__(self, title='Неизвестная книга', author='Неизвестный автор', pages=1):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def set_title(self, new_title):
        while new_title.strip() == '':
            print('Ошибка: название книги не может быть пустым.')
            self.__title = new_title.strip()

    def get_title(self):
        return self.__title

    def set_author(self, new_author):
        if new_author.strip() != '':
            self.__author = new_author.strip()
        else:
            print('Ошибка: имя автора не может быть пустым.')

    def get_author(self):
        return self.__author

    def set_pages(self, new_pages):
        if (str(new_pages).isdigit()) and (new_pages > 0):
            self.__pages = new_pages
        else:
            print('Ошибка: количество страниц должно быть целым числом больше нуля.')

    def get_pages(self):
        return self.__pages

    def amount_words(self):
        return self.get_pages() * 300

    def is_big_book(self) -> bool:
        return self.get_pages() > 200

    def show_information(self):
        print('\n--- ИНФОРМАЦИЯ О КНИГЕ ---')
        print('Название книги:', self.get_title())
        print('Автор книги:', self.get_author())
        print('Количество страниц:', self.get_pages())



class Menu:
    def __init__(self):
        self.book1 = Book()
        self.book2 = Book()
        self.book3 = Book()

    def run(self):
        while True:
            print('\n--- МЕНЮ ---')
            print('1. Показать книги')
            print('2. Изменить книгу')
            print('3. Посчитать количество слов')
            print('4. Проверить размер книги')
            print('5. Выход')

            choice = input('Выберите действие: ')

            if choice == '1':
                self.book1.show_information()
                self.book2.show_information()
                self.book3.show_information()

            elif choice == '2':
                number = input('Выберите книгу (1, 2 или 3): ')

                if number == '1':
                    book = self.book1
                elif number == '2':
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
                number = input('Выберите книгу (1, 2 или 3): ')

                if number == '1':
                    print(self.book1.amount_words())
                elif number == '2':
                    print(self.book2.amount_words())
                else:
                    print(self.book3.amount_words())

            elif choice == '4':
                number = input('Выберите книгу (1, 2 или 3): ')

                if number == '1':
                    print(self.book1.is_big_book())
                elif number == '2':
                    print(self.book2.is_big_book())
                else:
                    print(self.book3.is_big_book())

            elif choice == '5':
                print('Программа завершена.')
                break

            else:
                print('Неверный пункт меню!')


def set_pages(self, new_pages):
    if (new_pages.isdigit()) and (new_pages > 0):
        self.__pages = new_pages
    else:
        print('Ошибка: количество страниц должно быть целым числом больше нуля.')

menu = Menu()
menu.run()
