from prop_manage import PropertyManagement
class Host:
    def __init__(self,name,contact,age,prop_ID,prop_name,location,description,price,availability):
        self.prop = PropertyManagement(prop_ID,prop_name,location,description,price,availability)
        self.name = name
        self.contact = contact
        self.age = age
        self.props = [self.prop]

    def add_prop(self,prop_ID,prop_name,location,description,price,availability):
        prop = PropertyManagement(prop_ID,prop_name,location,description,price,availability)
        self.props.append(prop)