from tkinter import *

class Pop():
    def __init__(self, win, result, game_instance):
        self.pop = Toplevel(win)
        self.pop.title("Game Over")
        self.pop.geometry("350x200")
        self.pop.config(bg = "black")
        self.result = result
        self._win = win
        self.game_instance = game_instance

    def choice(self,option):
        self.pop.destroy()
        if option == 'restart':
            try:
                self.game_instance.restart()
            except Exception as e:
                print(f"Error: {e}")
                 
        else:
            self.pop.master.destroy()

         


    def clicker(self):
            # original = Image.open("images/tictactoe.png")
            # # Adjust these numbers to get the size you want
            # resized = original.resize((100, 100))  # width, height in pixels
            # self.xo = ImageTk.PhotoImage(resized)

            pop_label = Label(self.pop, text=f"{self.result}!!!...", bg = "#82CAFF", fg="black", font=("helvetica",15,'bold'))
            pop_label.pack(pady=10)

            my_frame = Frame(self.pop, bg = "black")
            my_frame.pack(pady=5, expand=True)

            restart = Button(my_frame, text = 'Restart',font=('Arial', 12, 'bold'), command=lambda: self.choice("restart"), bg = 'orange')
            restart.grid(row=1, column=0)
            restart.config(width=10, height=5)

            exit = Button(my_frame, text = 'Exit',font=('Arial', 12, 'bold'), command=lambda: self.choice("exit"), bg = 'yellow')
            exit.grid(row=1, column=1) 
            exit.config(width=10, height=5)