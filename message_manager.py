import pickle
import data.datamanager as datamanager

from base_classes import *
from data import record

PATH = "database" #файл, куда происходит запись и загрузка данных


class MessageManager:
    """ Этот класс отвечает за сообщения: загрузка, сохранение, отображение, добавление и удаление сообщений.
        В качестве параметра принимает Frame, на котором будет отображаться поле вывода, поле ввода и кнопка для
        отправки нового сообщения."""
    def __init__(self, window):

        self.subject_index = 0
        self.message_list = datamanager.datamanager.get(self.subject_index)

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

        self.state_label = StateLabel(self.commit_button_frame,
                                      text=self.message_list.name)
        self.state_label.pack(side='left', expand='no')
        self.reshow()

    def reshow(self, subject_index=0):
        self.messages_area.config(state='normal')
        self.messages_area.delete("1.0", "end")
        self.subject_index = subject_index
        self.message_list = datamanager.datamanager.get(subject_index)
        for rec in self.message_list:
            self.messages_area.insert("end", str(rec) + '\n')
        self.messages_area.config(state='disable')
        self.state_label.change_text(self.message_list.name)

    def show(self, messages):
        self.messages_area.config(state='normal')
        self.messages_area.delete("1.0", "end")
        for rec in messages:
            self.messages_area.insert("end", str(rec) + '\n')
        self.messages_area.config(state='disable')
        self.state_label.change_text("SearchResult")

    def add(self):
        """Метод add добавляет новое сообщение из поле ввода test_field при нажатии кнопки Commit"""
        string = self.new_message_area.get(1.0, "end").strip('\n')
        if len(string) > 0:
            self.message_list.append(record.Record(string))
            if self.subject_index != 0:
                datamanager.datamanager.get(0).append(self.message_list[-1])
            self.new_message_area.delete(1.0, "end")
            self.reshow(self.subject_index)
            datamanager.datamanager.save()

    def new_subject(self, subject):
        datamanager.datamanager.add(subject)
        datamanager.datamanager.save()

    def del_subject(self, index):
        datamanager.datamanager.erase(index)
        datamanager.datamanager.save()
        if self.subject_index == index:
            self.reshow(0)