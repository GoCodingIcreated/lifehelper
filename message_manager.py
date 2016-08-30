from base_classes import *
import record
import pickle

PATH = "database" #файл, куда происходит запись и загрузка данных


class MessageManager:
    """ Этот класс отвечает за сообщения: загрузка, сохранение, отображение, добавление и удаление сообщений.
        В качестве параметра принимает Frame, на котором будет отображаться поле вывода, поле ввода и кнопка для
        отправки нового сообщения."""
    def __init__(self, window):
        try:
            self.load()
        except FileNotFoundError:
            # файла не существует -- значит это первый запуск. производим начальную инициализацию базы
            self.subjects_list = []
            self.subjects_list.append(record.Subject(name="all"))
            self.subjects_list[0].append(record.Record("the first commit"))
            self.subjects_list[0].append(record.Record("the second commit"))
            self.subjects_list[0].append(record.Record("the last commit"))
        try:
            self.message_list = self.subjects_list[0]
            self.subject_index = 0
        except:
            # TODO: add new subject creation
            print("Error with self.message_list = self.subjects_list[0]")

        self.message_frame = MyFrame(window)
        self.message_frame.pack(side='top', fill='both', expand='yes')

        self.messages_scroll = Scroll(self.message_frame)
        self.messages_scroll.pack(side='right', fill='y')

        self.messages_area = InputText(self.message_frame,
                                       height=25,
                                       yscrollcommand=self.messages_scroll.set)
        self.messages_area.pack(side='top', fill='both', expand='yes')

        self.messages_scroll.configure(command=self.messages_area.yview)

        self.new_message_frame = MyFrame(window)
        self.new_message_frame.pack(side='top', fill='both', expand='yes')

        self.new_message_scroll = Scroll(self.new_message_frame)
        self.new_message_scroll.pack(side='right', fill='y')

        self.new_message_area = InputText(self.new_message_frame,
                                          height=5,
                                          yscrollcommand=self.new_message_scroll.set)
        self.new_message_area.pack(side='top', expand='yes', fill='both')

        self.new_message_scroll.configure(command=self.new_message_area.yview)

        self.commit_button_frame = MyFrame(window, height=1)
        self.commit_button_frame.pack(side='bottom', expand='yes', fill='both')
        self.commit_button = CommitButton(self.commit_button_frame, command=self.add, height=2, width=10)
        self.commit_button.pack(side='right', expand='no')

        self.reshow()

    def reshow(self, subject_index=0):
        self.messages_area.config(state='normal')
        self.messages_area.delete("1.0", "end")
        self.message_list = self.subjects_list[subject_index]
        self.subject_index = subject_index
        for rec in self.message_list:
            self.messages_area.insert("end", str(rec) + '\n')
        self.messages_area.config(state='disable')

    def add(self):
        """Метод add добавляет новое сообщение из поле ввода test_field при нажатии кнопки Commit"""
        string = self.new_message_area.get(1.0, "end").strip('\n')
        if len(string) > 0:
            self.message_list.append(record.Record(string))
            if self.subject_index != 0:
                self.subjects_list[0].append(self.message_list[-1])
            self.new_message_area.delete(1.0, "end")
            self.reshow(self.subject_index)
            self.save()

    def load(self):
        with open(PATH, "rb") as database:
            self.subjects_list = pickle.load(database)
        for subject in self.subjects_list:
            print(subject.name)
            for rec in subject:
                print("%s: %s" % (rec.creating_time, rec.text))

    def save(self):
        with open(PATH, "wb") as database:
            pickle.dump(self.subjects_list, database)

    def new_subject(self, subject):
        self.subjects_list.append(subject)
        self.save()

    def del_subject(self, index):
        self.subjects_list.pop(index)
        self.save()
        if self.subject_index == index:
            self.reshow(0)