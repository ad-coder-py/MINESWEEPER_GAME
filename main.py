from tkinter import *
import settings
import utils
from cell import Cell


window = Tk()
window.configure(bg="gray")
window.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
window.resizable(False, False)
window.title("MineSweeper Game")

# Top Frame
top_frame = Frame(
    window,
    bg="gray",
    highlightbackground="black",
    highlightthickness=1,
    width=settings.WIDTH,
    height=utils.height_prct(15),
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    fg="black",
    bg="gray",
    text="MINESWEEPER GAME",
    font=("Arial Bold", 70, "italic")
)
game_title.place(
    x=utils.width_prct(15), y=0
)

# Right Frame
right_frame = Frame(
    window,
    bg="gray",
    highlightbackground="black",
    highlightthickness=2,
    width=utils.width_prct(30),
    height=utils.height_prct(82.5),

)
right_frame.place(
    x=utils.width_prct(70),
    y=utils.height_prct(15)
)

cells_left_label = Label(
    right_frame,
    fg='black',
    bg='gray',
    text='CELLS LEFT',
    font=("Arial Bold", 30, "italic")
)
cells_left_label.place(
    x=utils.width_prct(6),
    y=utils.height_prct(8.3)
)

Cell.cells_left_label_box(right_frame)
Cell.cells_left_label_box_object.place(
    x=utils.width_prct(9.5),
    y=utils.height_prct(15.5)
)

flags_left_label = Label(
    right_frame,
    fg='black',
    bg='gray',
    text='FLAGS LEFT',
    font=("Arial Bold", 30, "italic")
)
flags_left_label.place(
    x=utils.width_prct(6.5),
    y=utils.height_prct(30)
)

Cell.flags_left_label_box(right_frame)
Cell.flags_left_label_box_object.place(
    x=utils.width_prct(10),
    y=utils.height_prct(38)
)


def try_again_btn_action():
    sys.exit()


try_again_btn = Button(
    right_frame,
    width=8,
    height=3,
    text='TRY \n AGAIN!!!',
    font=("Arial Bold", 30, "italic"),
    command=try_again_btn_action
)
try_again_btn.place(
    x=utils.width_prct(8),
    y=utils.height_prct(56)
)

# Centre_Frame
centre_frame = Frame(
    window,
    bg='black',
    highlightbackground='black',
    highlightthickness=2,
    width=utils.width_prct(75),
    height=utils.height_prct(85)
)
centre_frame.place(x=0, y=utils.height_prct(15))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        cell_obj = Cell(x, y)  # Each object (cell_obj) of class Cell is a cell!
        cell_obj.create_cell_btn(centre_frame)
        cell_obj.cell_btn_object.grid(
            row=x, column=y
        )

Cell.randomize_mines()

window.mainloop()
