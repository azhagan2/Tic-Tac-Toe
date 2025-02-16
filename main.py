from graphics import Window
from box import Box

def main():

    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)
    cell_size_x = (screen_x - 2 * 50) / 3
    cell_size_y = (screen_y - 2 * 50) / 3
    try:
        cell = Box(50, 50,cell_size_x, cell_size_y, win)  # Example test
    except Exception as e:
        print(f"Error: {e}")

    win.wait_for_close()


main()