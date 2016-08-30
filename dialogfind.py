import tkinter
from base_classes import *


class DialogFind:
    def __init__(self, master):
        self.return_value = None

        self.window = tkinter.Toplevel(master)
        self.window.geometry("320x320+500+100")
        self.main_frame = MyFrame(self.window)
        self.main_frame.pack(fill='both', expand='yes')

        self.text_search_frame = MyFrame(self.main_frame)
        self.text_search_frame.pack(side='top', expand='no', fill='x')
        self.text_search_label = tkinter.Label(self.text_search_frame, text="Text:")
        self.text_search_label.pack(side='left', expand='no')
        self.text_search_entry = tkinter.Entry(self.text_search_frame)
        self.text_search_entry.pack(side='right', expand='yes', fill='x')

        self.tag_frame = MyFrame(self.main_frame)
        self.tag_frame.pack(side='top', expand='no', fill='x')
        self.tag_label = tkinter.Label(self.tag_frame, text='#tag:')
        self.tag_label.pack(side='left', expand='no')
        self.tag_entry = tkinter.Entry(self.tag_frame)
        self.tag_entry.pack(side='right', expand='yes', fill='x')

        self.button_frame = MyFrame(self.main_frame)
        self.button_frame.pack(side='bottom', fill='x')
        self.buttonFind = OkButton(self.button_frame, command=self.find_command)
        self.buttonFind["text"] = "Find"
        self.buttonFind.pack(side='left')
        self.buttonCancel = CancelButton(self.button_frame, command=self.cancel_command)
        self.buttonCancel.pack(side='right')

        self.radio_button_frame = MyFrame(self.main_frame)
        self.radio_button_frame.pack(side='bottom', fill='both')

        self.radio_var = tkinter.IntVar()
        self.radio_button_list = []
        self.radio_frame_list = []
        for (index, button) in enumerate(("Search by text", "Search by tag", "Search by date")):
            self.radio_frame_list.append(MyFrame(self.radio_button_frame))
            self.radio_frame_list[-1].pack(fill='both')
            self.radio_button_list.append(tkinter.Radiobutton(self.radio_frame_list[-1],
                                                              text=button,
                                                              variable=self.radio_var,
                                                              value=index))
            self.radio_button_list[-1].pack(side='left', fill='x')

        self.window.protocol("WM_DELETE_WINDOW", self.cancel_command)

        # TODO: add search by data

        self.date_frame = MyFrame(self.main_frame)
        self.date_frame.pack(side='top', expand='no', fill='both')

        self.date_label = tkinter.Label(self.date_frame, text="Date:")
        self.date_label.pack(side='left', expand='no')
        self.date_day = tkinter.ttk.Combobox(self.date_frame, width=3, values=[x for x in range(1, 32)])
        self.date_day.pack(side='left', expand='no')
        self.date_month = tkinter.ttk.Combobox(self.date_frame, width=3, values=[x for x in range(1, 13)])
        self.date_month.pack(side='left', expand='no')
        self.date_year = tkinter.ttk.Combobox(self.date_frame, width=5, values=[x for x in range(2016, 2030)])
        self.date_year.pack(side='left', expand='no')

    def go(self):
        self.window.grab_set()
        self.window.focus_set()
        self.window.wait_window()
        return self.return_value

    def get_date(self):
        if self.date_year.get() == '' or self.date_month.get() == '' or self.date_year.get() == '':
            return None
        return {'year' : int(self.date_year.get()),
                'month' : int(self.date_month.get()),
                'day' : int(self.date_day.get())}

    def find_command(self):
        if self.radio_var.get() == 0:
            self.return_value = SearchResult("text", self.text_search_entry.get(), self.get_date())
        elif self.radio_var.get() == 1:
            self.return_value = SearchResult("tag", self.tag_entry.get(), self.get_date())
        elif self.radio_var.get() == 2:
            self.return_value = SearchResult("date", '', self.get_date())
        else:
            raise RuntimeError
        self.window.destroy()

    def cancel_command(self):
        self.return_value = None
        self.window.destroy()