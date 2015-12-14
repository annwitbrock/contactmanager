class ContactManager(object):
    def __init__(self):
        self.contacts = []

    def contacts(self):
        return self.contacts

    def add_contact(self, contact):
        self.contacts.append(contact)


