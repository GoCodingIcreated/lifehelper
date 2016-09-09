import data.record as record
import config
import pickle


class DataManager:
    def __init__(self, dirpath):
        self.workdir = dirpath
        self.subjects_list = []
        try:
            self.load()
        except (FileExistsError, FileNotFoundError):
            self.create_base()

    def load(self):
        with open(self.workdir, "rb") as database:
            self.subjects_list = pickle.load(database)

    def save(self):
        with open(self.workdir, "wb") as database:
            pickle.dump(self.subjects_list, database)

    def create_base(self):
        self.subjects_list.append(record.Subject(name="all"))
        self.subjects_list[0].append(record.Record("the first commit"))
        self.subjects_list[0].append(record.Record("the second commit"))
        self.subjects_list[0].append(record.Record("the last commit"))
        self.save()

    def get(self, index):
        try:
            return self.subjects_list[index]
        except IndexError:
            print("LOG: wrong get index")
            return None

    def add(self, subject):
        self.subjects_list.append(subject)

    def erase(self, index):
        self.subjects_list.pop(index)


datamanager = DataManager(config.PATH)

if __name__ == '__main__':
    print(datamanager.subjects_list)