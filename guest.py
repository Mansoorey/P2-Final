from Booking import Booking
from host import Host
class Guest(Host):
    def __init__(self,guest_name,contact,age,prop_ID,prop_name,location,description,price,availability):
        super().__init__(prop_ID,prop_name,location,description,price,availability)
        self.guest_name = guest_name
        self.contact = contact
        self.age = age

    def choose(self):
        name = input("Enter name of the property that you want to get: ")
        for prop in self.props:
            if name == prop.prop_name:
                a = int(input("How many days you want to get: "))
                prop.price = prop.price * a
                book = Booking(book_ID, prop.prop_name, checkin_date, checkout_date, )
                checkin_date = input(("Enter date to checkin: ")
                checkout_date = input("Enter day til which you will stay:")
                book_ID = prop.prop_ID