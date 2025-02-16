from graphics import Line, Point

class Cell:
    def __init__(self,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win 

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return 
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line, "Black")
        
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y1), Point(x2, y2))
            self._win.draw_line(line, "Black")

        if self.has_top_wall:
            line = Line(Point(x1,y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x2, y1))
            self._win.draw_line(line, "Black")

        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x2, y2))
            self._win.draw_line(line, "Black")

    


        