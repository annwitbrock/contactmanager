class ContactManager(object):
    def __init__(self):
        self.contact_list = []

    def contacts(self):
        return self.contact_list

    def add_contact(self, contact):
        self.contact_list.append(contact)


