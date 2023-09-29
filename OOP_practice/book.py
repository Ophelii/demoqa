class Book:

    def __init__(self, title, author):
        self.checked_out = False
        self.title = title
        self.author = author


    def check_out(self):
        if self.checked_out:
            print('Книга находится у абонента')
        else:
            self.checked_out = True
            print('Выдаем книгу абоненту')


    def check_in(self):
        if not self.checked_out:
            print('Книга в наличии ')
        else:
            self.checked_out = False
            print('Принимаем книгу в библиотеку')



story_book = Book('Современная история', 'Умный Кто. То.')

story_book.check_out()
story_book.check_out()


story_book.check_in()
story_book.check_in()