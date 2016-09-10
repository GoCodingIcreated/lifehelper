import dialogfind
import dialognewsub
import data.datamanager as datamanager
from message_manager import *


class Application(MyFrame):
    def __init__(self, master):
        MyFrame.__init__(self, master)
        self.master = master
        self.master.title("LifeHelper")
        self.master.geometry("640x640+300+0")
        self.master.minsize(640, 640)
        self.pack(expand='yes', fill='both')

        self.top_menu = MyFrame(self, height=25)
        self.top_menu.pack(side='top', fill='x', expand='no', pady=0)

        self.bot_menu = MyFrame(self, height=25)
        self.bot_menu.pack(side='bottom', fill='x', expand='no', pady=0)

        self.mid_frame = MyFrame(self)
        self.mid_frame.pack(fill='both', expand='yes')

        self.list_frame = MyFrame(self.mid_frame, width=150)
        self.list_frame.pack(side='left', fill='both', expand='yes')

        self.buttons_frame = MyFrame(self.mid_frame, width=50)
        self.buttons_frame.pack(side='left', fill='both', expand='no')
        self.create_frame_buttons(self.buttons_frame)

        self.text_frame = MyFrame(self.mid_frame, width=200)
        self.text_frame.pack(side='right', fill='both', expand='yes')

        # создание полей работы с сообщениями
        self.message_manager = MessageManager(self.text_frame)

        # создание панели выбора раздела
        self.create_list_box(self.list_frame)
        # создание верхнего меню
        #self.create_menu(self.top_menu)


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
        for subject in datamanager.datamanager.subjects_list:
            self.subjects_box.insert('end', subject.name)

    def search(self):
        dialog = dialogfind.DialogFind(self.master)
        return_value = dialog.go()
        print(return_value)
        if return_value:
            Application.__dict__['search_' + return_value.type](self, return_value.example, return_value.date)

    def search_text(self, text, date=None):
        result = []
        for subject in datamanager.datamanager.subjects_list:
            for message in subject:
                if text in message.text and Application.compare_dates(date, message.creating_time):
                    result.append(message)
        self.message_manager.show(result)

    def search_tag(self, tag, date=None):
        result = []
        for subject in datamanager.datamanager.subjects_list:
            for message in subject:
                if tag in message.text and Application.compare_dates(date, message.creating_time):
                    result.append(message)
        self.message_manager.show(result)

    def search_date(self, text, date):
        result = []
        for subject in datamanager.datamanager.subjects_list:
            for message in subject:
                if Application.compare_dates(date, message.creating_time):
                    result.append(message)
        self.message_manager.show(result)


    @staticmethod
    def compare_dates(mydate, libdate):
        if not mydate or not libdate:
            return True
        return (mydate['year'] == libdate.year and
                    mydate['month'] == libdate.month and
                    mydate['day'] == libdate.day)

    def create_frame_buttons(self, frame):
        self.button_list = []
        for button_text, func in (("+", self.new_subject_add),
                                  ("-", self.del_subject),
                                  ("up", None),
                                  ("down", None),
                                  ("find", self.search)):
            self.button_list.append(MenuListButton(frame, text=button_text, command=func))
            self.button_list[-1].pack(side='top', expand='no', pady=5)

    def create_list_box(self, frame):
        self.subjects_box = SubjectsList(self.list_frame)
        self.subjects_box.pack(side='top', fill='both', expand='yes')
        for subject in datamanager.datamanager.subjects_list:
            self.subjects_box.insert('end', subject.name)
        self.subjects_box.bind('<ButtonRelease-1>', self.new_subject_selected)

    def create_menu(self, frame):
        self.new_subject_button = MenuButton(self.top_menu, text="new sub..", command=self.new_subject_add)
        self.new_subject_button.pack(side='left', expand='no')
        self.del_subject_button = MenuButton(self.top_menu, text="del sub", command=self.del_subject)
        self.del_subject_button.pack(side='left', expand='no')
        self.find_messages_button = MenuButton(self.top_menu, text="find..", command=self.search)
        self.find_messages_button.pack(side='left', expand='no')

if __name__ == "__main__":

    root = tkinter.Tk()
    application = Application(root)

    root.mainloop()
    #datetime.now().strftime("[%Y.%m.%d %H:%M]")

# this comment just for test github