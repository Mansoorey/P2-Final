from abc import ABC,abstractmethod

class AbsDoc(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def save(self):
        pass

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

class PDFDoc(AbsDoc):
    def __init__(self,file_name,file_size,content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content

    def open(self):
        with open(self.file_name+"_pdf.txt","w") as f:
            f.write(self.content)

    def read(self):
        with open(self.file_name+"_pdf.txt","r") as f:
            f.readlines()
        "The PDF file is currently being read"

    def save(self):
        print(f"The PDF file {self.file_name} has been saved")


class ExcelDoc:
    def __init__(self,file_name,file_size,content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content

    def open(self):
        with open(self.file_name+"_excel.txt","w") as f:
            f.write(self.content)

    def read(self):
        with open(self.file_name+"_excel.txt","r") as f:
            f.readlines()
            print(f"The Excel file is currently being read")


    def save(self):
        print(f"The Excel file {self.file_name} has been saved")

class DocumentFactory:
    def create_file(self,file_type):
        if file_type == "word":
            name = input("Enter name of file: ")
            file_name = name + ".word"
            file_size = int(input("Enter File Size: "))
            content = input("Enter the content for the file")
            return WordDoc(file_name,file_size,content)
        if file_type == "pdf":
            name = input("Enter name of file: ")
            file_name = name + ".pdf"
            file_size = int(input("Enter File Size: "))
            content = input("Enter the content for the file")
            return PDFDoc(file_name,file_size,content)
        if file_type == "excel":
            name = input("Enter name of file: ")
            file_name = name + ".pdf"
            file_size = int(input("Enter File Size: "))
            content = input("Enter the content for the file")
            return ExcelDoc(file_name,file_size,content)

word = WordDoc("word1",14," My name is mansoor and I am giving an exam")
word.open()
word.read()
word.save()
# file_type = input("Enter file type (word,pdf,excel): ")
doc_fac = DocumentFactory()
create_doc = doc_fac.create_file("word")
create_doc.open()
create_doc.read()
create_doc.save()






