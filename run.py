from prop_manage import PropertyManagement
from host import Host
from guest import Guest
from Booking import Booking

host = Host("Mansoor",12343,23,"werProp","Mansoor House","Johar Town","Good House",123,"Available")
host.add_prop("Hanna",12341233,25,"13Prop"," House","Johar Town","Good House",1345,"Available")
guest = Guest("Hammad",1343,56)
guest.choose()