import tkinter

class Interface:
    def __init__(self):
        self._main_window = tkinter.Tk()
        self._main_window.title('Угадай число')
        self._main_window.geometry("400x400")
        self._label = tkinter.Label(self._main_window,text = 'Это игра "Угадай число"!  Выбери,кто будет загадывать:',
                                    font=("Arial", 8, "bold"))
        self._label.pack()
        self._top_fame = tkinter.Frame()
        self._top_fame.pack(expand=True)
        self._first_button = tkinter.Button(self._top_fame, text='Число загадывает компьютер',
                                            command=self.game_start)
        self._first_button.pack()
        self._second_button = tkinter.Button(self._top_fame, text='Число загадывает компьютер',
                                             command=self.game_start)
        self._second_button.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    game = Interface()