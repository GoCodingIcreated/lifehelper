import tkinter


class MyFrame(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
        #self['relief'] = 'ridge'
        self['bd'] = 5


class CommitButton(tkinter.Button):
    def __init__(self, *args, **kwargs):
        tkinter.Button.__init__(self, *args, **kwargs)
        self["text"] = "Commit"
        self['bd'] = 5


class InputText(tkinter.Text):
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)


class SubjectsList(tkinter.Listbox):
    def __init__(self, master=None, *args, **kwargs):
        tkinter.Listbox.__init__(self, master, *args, **kwargs)


class Scroll(tkinter.Scrollbar):
    def __init__(self, master=None, *args, **kwargs):
        tkinter.Scrollbar.__init__(self, master, *args, **kwargs)


class MenuButton(tkinter.Button):
    def __init__(self, master=None, *args, **kwargs):
        tkinter.Button.__init__(self, master, *args, **kwargs)
        self["height"] = 1
        self["bd"] = 0


class OkButton(tkinter.Button):
    def __init__(self, master=None, *args, **kwargs):
        tkinter.Button.__init__(self, master, *args, **kwargs)
        self["text"] = 'OK'
        self["height"] = 2
        self["width"] = 10


class CancelButton(tkinter.Button):
    def __init__(self, master=None, *args, **kwargs):
        tkinter.Button.__init__(self, master, *args, **kwargs)
        self["text"] = 'Cancel'
        self["height"] = 2
        self["width"] = 10


class SearchResult:
    def __init__(self, type, example, date=None):
        self.type = type
        self.example = example
        self.date = date

    def __str__(self):
        return str(self.type) + '\n' + str(self.example) + '\n' + str(self.date)


class MenuListButton(tkinter.Button):
    def __init__(self, master=None, *args, **kwargs):
        tkinter.Button.__init__(self, master, *args, **kwargs)
        self["width"] = 4
        self["height"] = 2


class StateLabel(tkinter.Label):
    def __init__(self, master=None, *args, **kwargs):
        tkinter.Label.__init__(self, master, *args, **kwargs)
        self["bg"] = 'white'
        self.change_text(self["text"])
        self['anchor'] = 'w'
        self["width"] = 40
        self['height'] = 2

    def change_text(self, text):
        self["text"] = "Current Subject:\t" + text
