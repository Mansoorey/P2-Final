from abc import ABC,abstractmethod
from Abc import AbsDoc

class WordDoc(AbsDoc):
    def __init__(self,file_name,file_size,content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content

    def open(self):
        with open(self.file_name+"_word.txt","w") as f:
            f.write(self.content)

    def read(self):
        with open(self.file_name+"_word.txt","r") as f:
            f.readlines()
            "The word file is currently being read"

    def save(self):
        print(f"The file {self.file_name} has been saved")