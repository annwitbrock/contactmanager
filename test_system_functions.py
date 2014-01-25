import unittest
from contact_manager.ContactManager import ContactManager

class TestSystemFunctions(unittest.TestCase):

    def setUp(self):
        self.phone_vcard = '''BEGIN:VCARD
VERSION:2.1
N:Smith;Jan;A;;
FN:Smith, J A
TEL;CELL;PREF:+44208123456
END:VCARD
'''
        self.email_vcard = '''BEGIN:VCARD
VERSION:2.1
N:Smith;J;;;
FN:Jan Smith
EMAIL;PREF:jsmith@example.com
END:VCARD
'''
        pass

    def tearDown(self):
        pass

    def test_CanSelectContactImportSource(self):
        pass

    def test_CanSelectContactExportSource(self):
        pass

    def test_CanReadAVCFFile(self):
        pass

    def test_CanWriteAVCFFile(self):
        pass

    def test_CanFindAContact(self):
        contact1 = self.phone_vcard
        cm = ContactManager()
        cm.add_contact(contact1)
        self.assertTrue(contact1 in cm.contacts())
        #TODO retrieve details by name

    def test_CanSortAListOfContactsByFirstName(self):
        pass

    def test_CanSortAListOfContactsByLastName(self):
        pass

    def test_CanFindAllContactsWithMatchingFirstName(self):
        pass

    def test_CanFindAllContactsWithMatchingLastName(self):
        pass

    def test_CanFindAllContactsWithMatchingPhone(self):
        pass

    def test_CanFindContactsWithMatchingAddress(self):
        pass

    def test_CanRecommendMergingSetOfContacts(self):
        pass

    def test_CanMergeSetOfContacts(self):
        pass

    def test_CanDisplaySetOfContacts(self):
        contact1 = self.phone_vcard
        contact2 = self.email_vcard
        cm = ContactManager()
        cm.add_contact(contact1)
        cm.add_contact(contact2)
        self.assertTrue(contact1 in cm.contacts())
        self.assertTrue(contact2 in cm.contacts())
        #TODO list of contacts
        #TODO appears in display

    def test_CanDisplayPotentialMergedContact(self):
        pass

    def test_CanStepThroughDisplayedSetOfContacts(self):
        pass

    def test_CanDisplayContactDetails(self):
        pass

    def test_CanDisplayEmptyResult(self):
        pass





if __name__ == '__main__':
    unittest.main()