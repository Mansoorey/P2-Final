from Abc import AbsDoc

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