from tkinter import Tk, BOTH, Canvas, Button


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Tic Tac Toe")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="Black", height=height, width=width)
        self.__canvas.pack()
        self.__running = False

    def get_tk(self):
        return self.__root

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1, p2):
        self.p1 = p1
        self.p2 = p2 

    def draw(self, canvas, fill_colour = 'White'):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill= fill_colour, width = 3)
        