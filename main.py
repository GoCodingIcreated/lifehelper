import tkinter
import record
import dialognewsub
import dialogfind
from base_classes import *
from message_manager import *


class Application(MyFrame):
    def __init__(self, master):
        MyFrame.__init__(self, master)
        self.master = master
        self.master.title("LifeHelper")
        self.master.geometry("640x640+300+0")
        self.pack(expand='yes', fill='both')

        self.top_menu = MyFrame(self, height=25)
        self.top_menu.pack(side='top', fill='x', expand='no', pady=0)

        self.bot_menu = MyFrame(self, height=25)
        self.bot_menu.pack(side='bottom', fill='x', expand='no', pady=0)

        self.mid_frame = MyFrame(self)
        self.mid_frame.pack(fill='both', expand='yes')

        self.list_frame = MyFrame(self.mid_frame, width=150)
        self.list_frame.pack(side='left', fill='both', expand='yes')

        self.text_frame = MyFrame(self.mid_frame, width=200)
        self.text_frame.pack(side='right', fill='both', expand='yes')

        self.message_manager = MessageManager(self.text_frame)

        self.subjects_box = SubjectsList(self.list_frame)
        self.subjects_box.pack(side='top', fill='both', expand='yes')
        for subject in self.message_manager.subjects_list:
            self.subjects_box.insert('end', subject.name)
        self.subjects_box.bind('<ButtonRelease-1>', self.new_subject_selected)

        self.new_subject_button = MenuButton(self.top_menu, text="new sub..", command=self.new_subject_add)
        self.new_subject_button.pack(side='left', expand='no')
        self.del_subject_button = MenuButton(self.top_menu, text="del sub", command=self.del_subject)
        self.del_subject_button.pack(side='left', expand='no')
        self.find_messages_button = MenuButton(self.top_menu, text="find..", command=self.search)
        self.find_messages_button.pack(side='left', expand='no')

    def new_subject_selected(self, event):
        self.message_manager.reshow(self.subjects_box.curselection()[0])

    def new_subject_add(self):
        dialog = dialognewsub.DialogOkNo(self.master)
        name = dialog.go()
        self.message_manager.new_subject(record.Subject(name))
        self.subject_reshow()

    def del_subject(self):
        self.message_manager.del_subject(self.subjects_box.curselection()[0])
        self.subject_reshow()

    def subject_reshow(self):
        self.subjects_box.delete(0, 'end')
        for subject in self.message_manager.subjects_list:
            self.subjects_box.insert('end', subject.name)

    def search(self):
        dialog = dialogfind.DialogFind(self.master)
        return_value = dialog.go()
        print(return_value)

    def search_text(self):
        pass

    def search_tag(self):
        pass

    def search_date(self):
        pass

if __name__ == "__main__":

    root = tkinter.Tk()
    application = Application(root)

    root.mainloop()
    #datetime.now().strftime("[%Y.%m.%d %H:%M]")
