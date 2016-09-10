import tkinter
import tkinter.ttk
from base_classes import *


class DialogFind:
    def __init__(self, master):
        self.return_value = None

        self.window = tkinter.Toplevel(master)
        self.window.geometry("320x320+500+100")
        self.window.resizable(height=False, width=False)
        self.main_frame = MyFrame(self.window)
        self.main_frame.pack(fill='both', expand='yes')


        self.text_search_frame = MyFrame(self.main_frame)
        self.text_search_frame.pack(side='top', expand='no', fill='x')
        self.text_search_label = tkinter.Label(self.text_search_frame, text="Text:")
        self.text_search_label.pack(side='left', expand='no')
        self.text_search_entry = tkinter.Entry(self.text_search_frame)
        self.text_search_entry.pack(side='right', expand='yes', fill='x')

        self.button_frame = MyFrame(self.main_frame)
        self.button_frame.pack(side='bottom', fill='x')
        self.buttonFind = OkButton(self.button_frame, command=self.find_command)
        self.buttonFind["text"] = "Find"
        self.buttonFind.pack(side='left')
        self.buttonCancel = CancelButton(self.button_frame, command=self.cancel_command)
        self.buttonCancel.pack(side='right')

        self.radio_button_frame = MyFrame(self.main_frame)
        self.radio_button_frame.pack(side='bottom', fill='both')

        """
        self.radio_var = tkinter.IntVar()
        self.radio_button_list = []
        self.radio_frame_list = []
        for (index, button) in enumerate(("Search by text", "Search by tag")):
            self.radio_frame_list.append(MyFrame(self.radio_button_frame))
            self.radio_frame_list[-1].pack(fill='both')
            self.radio_button_list.append(tkinter.Radiobutton(self.radio_frame_list[-1],
                                                              text=button,
                                                              variable=self.radio_var,
                                                              value=index))
            self.radio_button_list[-1].pack(side='left', fill='x')
        """
        self.window.protocol("WM_DELETE_WINDOW", self.cancel_command)

        self.search_type = tkinter.StringVar()
        self.is_text_search_radiobutton = tkinter.Radiobutton(self.radio_button_frame,
                                                              text="Search by text",
                                                              variable=self.search_type,
                                                              value="text")
        self.is_text_search_radiobutton.pack(anchor="nw", padx=15)
        self.is_text_search_radiobutton.select()

        self.is_tag_search_radiobutton = tkinter.Radiobutton(self.radio_button_frame,
                                                             text="Search by tag",
                                                             variable=self.search_type,
                                                             value="tag")
        self.is_tag_search_radiobutton.pack(anchor='nw', padx=15)
        self.is_tag_search_radiobutton.deselect()

        self.is_date_used = tkinter.IntVar()
        self.is_date_used_checkbox = tkinter.Checkbutton(self.radio_button_frame,
                                                         text='Search by data',
                                                         variable=self.is_date_used,
                                                         command=self.unable_timeinterval)
        self.is_date_used_checkbox.pack(anchor='nw', padx=15)

        self.is_timeinterval_used = tkinter.IntVar()
        self.is_timeinterval_used_checkbox = tkinter.Checkbutton(self.radio_button_frame,
                                                                 text='Search in timeinterval',
                                                                 variable=self.is_timeinterval_used,
                                                                 state='disabled',
                                                                 command=self.unable_time)
        self.is_timeinterval_used_checkbox.pack(anchor='nw', padx=35)
        # TODO: add search by data

        self.date_frame = MyFrame(self.main_frame)
        self.date_frame.pack(side='top', expand='yes', fill='both')

        self.create_date_widgets(self.date_frame)

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

    def unable_timeinterval(self):
        if self.is_timeinterval_used_checkbox['state'] == 'disabled':
            self.is_timeinterval_used_checkbox['state'] = 'normal'
        else:
            self.is_timeinterval_used_checkbox['state'] = 'disabled'
            self.is_timeinterval_used_checkbox.deselect()
        self.unable_time()

    def create_date_widgets(self, date_frame):
        self.date_label = tkinter.Label(date_frame, text="Date:")
        self.date_label.pack(anchor='nw', expand='no')

        self.date_start_frame = MyFrame(date_frame)
        self.date_start_frame.pack(side='top', fill='x')
        self.date_start_label = tkinter.Label(self.date_start_frame, text="Begin:", state='disabled')
        self.date_start_label.pack(side='left', expand='no', padx=20)
        self.date_start_day = tkinter.ttk.Combobox(self.date_start_frame,
                                                   width=3,
                                                   values=[x for x in range(1, 32)],
                                                   state='disabled')
        self.date_start_day.pack(side='left', expand='no')
        self.date_start_month = tkinter.ttk.Combobox(self.date_start_frame,
                                                     width=3,
                                                     values=[x for x in range(1, 13)],
                                                     state='disabled')
        self.date_start_month.pack(side='left', expand='no')
        self.date_start_year = tkinter.ttk.Combobox(self.date_start_frame,
                                                    width=5,
                                                    values=[x for x in range(2016, 2030)],
                                                    state='disabled')
        self.date_start_year.pack(side='left', expand='no')

        self.date_end_frame = MyFrame(date_frame)
        self.date_end_frame.pack(side='top', fill='x')
        self.date_end_label = tkinter.Label(self.date_end_frame, text="End:", state='disabled')
        self.date_end_label.pack(side='left', expand='no', padx=25)
        self.date_end_day = tkinter.ttk.Combobox(self.date_end_frame,
                                                 width=3,
                                                 values=[x for x in range(1, 32)],
                                                 state='disabled')
        self.date_end_day.pack(side='left', expand='no')
        self.date_end_month = tkinter.ttk.Combobox(self.date_end_frame,
                                                   width=3,
                                                   values=[x for x in range(1, 13)],
                                                   state='disabled')
        self.date_end_month.pack(side='left', expand='no')
        self.date_end_year = tkinter.ttk.Combobox(self.date_end_frame,
                                                  width=5,
                                                  values=[x for x in range(2016, 2030)],
                                                  state='disabled')
        self.date_end_year.pack(side='left', expand='no')

    def unable_time(self):
        if self.is_date_used.get():
            self.date_start_label['state'] = 'normal'
            self.date_start_day['state'] = 'normal'
            self.date_start_month['state'] = 'normal'
            self.date_start_year['state'] = 'normal'
        else:
            self.date_start_label['state'] = 'disabled'
            self.date_start_day['state'] = 'disabled'
            self.date_start_month['state'] = 'disabled'
            self.date_start_year['state'] = 'disabled'

        if self.is_timeinterval_used.get():
            self.date_end_label['state'] = 'normal'
            self.date_end_day['state'] = 'normal'
            self.date_end_month['state'] = 'normal'
            self.date_end_year['state'] = 'normal'
        else:
            self.date_end_label['state'] = 'disabled'
            self.date_end_day['state'] = 'disabled'
            self.date_end_month['state'] = 'disabled'
            self.date_end_year['state'] = 'disabled'


if __name__ == '__main__':
    root = tkinter.Tk()
    dialog = DialogFind(root)
    print(dialog.go())