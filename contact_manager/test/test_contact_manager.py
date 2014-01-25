import unittest

from contact_manager.ContactManager import ContactManager


class TestContactManager(unittest.TestCase):

    def test_can_create_a_contact_manager(self):
        cm = ContactManager()
        self.assertTrue(cm)

    def test_contact_manager_has_zero_contacts(self):
        cm = ContactManager()
        self.assertTrue(0 == len(cm.contacts()))

    def test_contact_manager_has_one_correct_contact(self):
        cm = ContactManager()
        contact = "bob"
        cm.add_contact(contact)
        self.assertTrue(1 == len(cm.contacts()))
        self.assertTrue(contact in cm.contacts())



if __name__ == '__main__':
    unittest.main()