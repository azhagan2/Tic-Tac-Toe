from cell import Cell 
import time
from tkinter import Button

class Box():
    def __init__(self, x1, y1, cell_size_x, cell_size_y,win=None):
        self._cells = []
        self._buttons = []
        self._x1 = x1
        self._y1 = y1
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.create_cell()

    def create_cell(self):
        print("in create_cell")
        for i in range(3):
            col_cells = []
            for j in range(3):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                col_cells.append(Cell(self._win))

                #have to build separetely like the maze program
                
            self._cells.append(col_cells)

        for i in range(3):
            for j in range(3):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        print("in _draw_cell")
        if self._win is None:
            return 
        
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        if i==0:
            self._cells[i][j].has_left_wall = False
        if j==0:
            self._cells[i][j].has_top_wall = False
        if i==2:
            self._cells[i][j].has_right_wall = False
        if j==2:
            self._cells[i][j].has_bottom_wall = False
        self._cells[i][j].draw(x1,y1,x2,y2)

        tk_win = self._win.get_tk()

        button_width = int(self._cell_size_x-10)  # Adjust width dynamically
        button_height = int(self._cell_size_y-10)

        self.create_button( tk_win,x1 + 6, y1 +6,button_width,button_height) 
        self._animate()

    
    def _animate(self):
        print("in _animate")
        if self._win is None:
            return 
        self._win.redraw()
        time.sleep(0.05)

    
    def create_button(self, win, x1,y1,width,height):
        button = Button(win, text = '', font=('Arial', 50, 'bold'),bg='black', relief='sunken',borderwidth=0, command=lambda: self.button_click(button))
        button.place(x=x1,y=y1, width=width, height=height)
        self._buttons.append(button)
        return button

    def button_click(self, button):
        if button['text'] == '':
            button['text'] = 'X'
        button.config(bg='#FF4C4C')




    