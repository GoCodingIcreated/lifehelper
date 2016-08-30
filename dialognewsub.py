import tkinter
from base_classes import *


class DialogOkNo:
    def __init__(self, master):
        self.sub_name = None

        self.window = tkinter.Toplevel(master)
        self.window.title("New Subject")
        self.window.geometry("300x150+500+200")
        self.window.resizable(width=False, height=False)
        self.frame = MyFrame(self.window)
        self.frame.pack(fill='both', expand='yes')

        self.name_frame = MyFrame(self.frame)
        self.name_frame.pack(side='top', fill='x', expand='yes')
        self.name_label = tkinter.Label(self.name_frame, text='name')
        self.name_label.pack(side='left', fill='x', expand='no')

        self.name_entry_text = tkinter.StringVar()
        self.name_entry = tkinter.Entry(self.name_frame, textvariable=self.name_entry_text)
        self.name_entry.pack(side='right', fill='x', expand='yes')

        self.button_frame = MyFrame(self.frame)
        self.button_frame.pack(side='top', fill='x', expand='yes')
        self.ok_button = OkButton(self.button_frame, command=self.ok_command)
        self.ok_button.pack(side='left', expand='no')

        self.cancel_button = CancelButton(self.button_frame, command=self.cancel_command)
        self.cancel_button.pack(side='right', expand='no')
        self.window.protocol("WM_DELETE_WINDOW", self.cancel_command)

    def go(self):
        self.window.grab_set()
        self.window.focus_set()
        self.window.wait_window()
        return self.sub_name

    def ok_command(self):
        self.sub_name = self.name_entry_text.get()
        self.window.destroy()

    def cancel_command(self):
        self.sub_name = None
        self.window.destroy()