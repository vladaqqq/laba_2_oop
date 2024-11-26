import tkinter
import tkinter.messagebox
import random

class Interface:
    def __init__(self):
        self._main_window = tkinter.Tk()
        self._main_window.title('Угадай число')
        self._main_window.geometry("400x400")
        self._label = tkinter.Label(self._main_window,text = 'Это игра "Угадай число"!\nВыбери,кто будет загадывать:',
                                    font=("Arial", 8, "bold"))
        self._label.pack()
        self._top_fame = tkinter.Frame()
        self._top_fame.pack(expand=True)
        self._first_button = tkinter.Button(self._top_fame, text='Число загадывает компьютер',
                                            command=self.game_start)
        self._first_button.pack()
        self._second_button = tkinter.Button(self._top_fame, text='Число загадывает пользователь',
                                             command=self.game_start)
        self._second_button.pack()

        self._main_window.mainloop()

    def game_start(self):
        self._main_window.destroy()
        secret_number = random.randint(1, 100)
        said_window = tkinter.Tk()
        said_window.title('Угадай число')
        said_window.geometry("400x400")
        label1 = tkinter.Label(said_window, text='Игра началась!\nКомпьютер загадал число от 1 до 100',
                              font=("Arial", 10, "bold"))
        label1.pack()
        enter = tkinter.Entry(said_window, width=30)
        enter.pack()
        third_button = tkinter.Button(said_window, text='Проверить',
                                      command=lambda: self.check_the_number(secret_number, enter))
        third_button.pack()

    def check_the_number(self,secret,enter):
        try:
            user_numer = int(enter.get())
            if user_numer < secret:
               tkinter.messagebox.showinfo('Результат','Слишком мало!\nПопробуйте еще раз')
            elif user_numer > secret:
                tkinter.messagebox.showinfo('Результат','Слишком много!\nПопробуйте еще раз')
            else:
                tkinter.messagebox.showinfo('Результат','Вы выиграли!')
        except ValueError:
            tkinter.messagebox.showinfo('Результат','Введите число,а не символ!')


if __name__ == '__main__':
    game = Interface()