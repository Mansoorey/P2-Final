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