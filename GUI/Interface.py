import tkinter
from tkinter import scrolledtext
from tkinter import Menu

__do_not_access = ""

# constants for gui
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT)

TITLE = "Text Editor"

PAD_WIDTH = 600
PAD_HEIGHT = 400


class Interface(object):
    window = None
    text_pad = None
    menu = None
    file_menu = None

    def initialise_window(self):
        self.window = tkinter.Tk()
        self.window.wm_title(TITLE)
        self.window.geometry(WINDOW_SIZE)

        # add typing area
        self.text_pad = scrolledtext.ScrolledText(self.window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        self.add_options()
        self.text_pad.pack()
        self.window.mainloop()

    def add_options(self):
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        self.file_menu = Menu(self.window)
        self.options_menu = Menu(self.window)
        self.about_menu = Menu(self.window)

        # file filter menu
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.dummy_action)
        self.file_menu.add_command(label="Open", command=self.dummy_action)
        self.file_menu.add_command(label="Save", command=self.dummy_action)
        self.file_menu.add_command(label="Save As...", command=self.dummy_action)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.dummy_action)

        # option menu
        self.menu.add_cascade(label="Options", menu=self.options_menu)

        # about menu
        self.menu.add_cascade(label="About", menu=self.about_menu)

    def dummy_action(self):
        print(self.__class__.__name__ + " invoked")