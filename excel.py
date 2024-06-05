from Abc import AbsDoc

class ExcelDoc(AbsDoc):
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