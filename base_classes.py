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


class NewSubjectButton(tkinter.Button): pass