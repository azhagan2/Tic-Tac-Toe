from cell import Cell 
import time
from tkinter import Button
from popup import Pop


count=0

class Box():
    def __init__(self, x1, y1, cell_size_x, cell_size_y,win=None):
        self._cells = []
        self._buttons = [[None for _ in range(3)] for _ in range(3)]
        self._button_clicked = []
        self._x_click = []
        self._o_click = []
        self.clicked = False
        self._x1 = x1
        self._y1 = y1
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._game_over = False
        self._game_end = False

        self.create_cell()

    
    def restart(self):
        
        global count
        count=0
        for i in range(3):
            for j in range(3):
                self._buttons[i][j].destroy()
        self._cells = []
        self._buttons = [[None for _ in range(3)] for _ in range(3)]
        self._button_clicked = []
        self._x_click = []
        self._o_click = []
        self.clicked = False
        self._cells = []
        self._game_over = False
        self._game_end = False
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

        self.create_button( tk_win,x1 + 6, y1 +6,button_width,button_height, i, j) 
        self._animate()

    
    def _animate(self):
        print("in _animate")
        if self._win is None:
            return 
        self._win.redraw()
        time.sleep(0.05)

    
    def create_button(self, win, x1,y1,width,height,i,j):
        button = Button(win, text = '', font=('Arial', 50, 'bold'),bg='black', relief='sunken',borderwidth=0, command=lambda: self.button_click(button, i, j))
        button.place(x=x1,y=y1, width=width, height=height)
        button.pos = (i, j)
        self._buttons[i][j] = button 
        return button


    def button_click(self, button, i, j):
        tk_win = self._win.get_tk()
        global count
        count+=1
        if count%2!=0:
            if (i,j) not in self._x_click:
                self._x_click.append((i,j)) 
            if button['text'] == '':
                button['text'] = 'X'
            button.config(bg='#FF4C4C')
            button['state'] ='disabled'
            button.config(disabledforeground= 'black')
            # print(i, j)   
            if(self.is_solved(self._x_click)):
                self._game_over = True
                result = "X Won"
                self.disable()
                a = Pop(tk_win, result, self)
                a.clicker()
                return

        else:
            if (i,j) not in self._o_click:
                self._o_click.append((i,j)) 
            if button['text'] == '':
                button['text'] = 'O'
            button.config(bg='#FF4C4C')
            button['state'] ='disabled'
            button.config(disabledforeground= 'black')
            if(self.is_solved(self._o_click)):
                self._game_over = True
                result = "O Won"
                self.disable()
                a = Pop(tk_win, result, self)
                a.clicker()
                return
        if (not self._game_over and count==9):
            result = "Game Draw"
            self._game_over = True
            self.disable()
            a = Pop(tk_win, result, self)
            a.clicker()
            return
        
    def is_solved(self,l):
        if len(l) > 2:
            for i in range(0,len(l)-2):
                for j in range(i+1,len(l)-1):
                    for k in range(i+2,len(l)):
                        if ((l[i][0]==l[j][0] and l[i][0]==l[k][0])):
                            if((l[i][1]+l[j][1]+l[k][1])==3):
                                if(self.color_cells(l[i], l[j], l[k])):
                                    print("vertical")
                                    return True
                                
                        if ((l[i][1]==l[j][1] and l[i][1]==l[k][1]) ):
                            if((l[i][0]+l[j][0]+l[k][0])==3):
                                if(self.color_cells(l[i], l[j], l[k])):
                                    print("Horizontal")
                                    return True
                        if(((0,0) in l) and ((1,1) in l) and ((2,2) in l)):
                            if(self.color_cells((0,0), (1,1), (2,2))):
                                    print("diagonal 1")
                                    return True
                        if(((0,2) in l) and ((1,1) in l) and ((2,0) in l)):
                            if(self.color_cells((0,2), (1,1), (2,0))):
                                    print("diagonal 2")
                                    return True
        return False
        
    def color_cells(self, a, b, c):
        print(a,b,c)
        for cell in [a,b,c]:
            i, j = cell
            if self._buttons[i][j]:
                self._buttons[i][j]['state'] ='active'
                self._buttons[i][j].config(bg='green')
                self._buttons[i][j]['state'] ='disabled'
        return True


    def disable(self):
        for i in range(3):
            for j in range(3):
                self._buttons[i][j]['state'] = 'disabled'

            

                


        





    