from tkinter import *
from tkinter import messagebox
import settings
import random
import sys


class Cell:
    all = []
    cell_count = settings.CELLS_COUNT
    flag_count = settings.MINES_COUNT
    cells_left_label_box_object = None
    flags_left_label_box_object = None

    def __init__(self, x, y, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.is_mine_candidate = False

        # Appending cell objects to a list all
        Cell.all.append(self)

    def create_cell_btn(self, location):
        btn = Button(
            location,
            text='',
            width=10,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def cells_left_label_box(location):
        lbl = Label(
            location,
            width=5,
            height=2,
            text=Cell.cell_count,
            highlightbackground='black',
            highlightthickness=2,
            font=("Arial Bold", 30, "italic")
        )
        Cell.cells_left_label_box_object = lbl

    @staticmethod
    def flags_left_label_box(location):
        lbl = Label(
            location,
            width=5,
            height=2,
            text=Cell.flag_count,
            highlightbackground='black',
            highlightthickness=2,
            font=("Arial Bold", 30, "italic")
        )
        Cell.flags_left_label_box_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            if self.surrounded_cells_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()

        if settings.MINES_COUNT == Cell.cell_count:
            messagebox.showinfo("Game Won", "CONGRATULATIONS")
            sys.exit()

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def show_mine(self):
        self.cell_btn_object.configure(
            bg='red',
            text='MINE'
        )
        messagebox.showerror("Game Over", "TRY AGAIN!!")
        sys.exit()

    @staticmethod
    def get_cell_by_axis(x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length,
                bg='gray85'
            )
            self.is_opened = True

            # Cells_left_label_box CODE
            if self.is_opened:
                Cell.cell_count -= 1
            Cell.cells_left_label_box_object.configure(
                text=Cell.cell_count
            )

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange',
                text='FLAG'
            )
            self.is_mine_candidate = True
            Cell.flag_count -= 1
            Cell.flags_left_label_box_object.configure(
                text=Cell.flag_count
            )
        else:
            Cell.flag_count += 1
            self.cell_btn_object.configure(
                bg='gray85',
                text=''
            )
            Cell.flags_left_label_box_object.configure(
                text=Cell.flag_count
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        random_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in random_cells:
            cell.is_mine = True

