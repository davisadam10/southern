__author__ = 'adam'


from unittest import TestCase
from nose.tools import *
import southern.utils.userUtils as userUtils
import tempfile


class test_User(TestCase):
    def setUp(self):
        self.user = userUtils.User()

    def test_user_title(self):
        expected_title = 'Mr'
        self.user.set_title(expected_title)
        user_title = self.user.get_title()
        self.assertEquals(expected_title, user_title)

    def test_forename(self):
        expected_forename = "Adam"
        self.user.set_forename(expected_forename)
        user_forename = self.user.get_forename()
        self.assertEquals(expected_forename, user_forename)

    def test_surname(self):
        expected_surname = "Davis"
        self.user.set_surname(expected_surname)
        user_surname = self.user.get_surname()
        self.assertEquals(user_surname, expected_surname)

    def test_email(self):
        expected_email = "davisadam10@googlemail.com"
        self.user.set_email(expected_email)
        user_email = self.user.get_email()
        self.assertEquals(expected_email, user_email)

    def test_phone_number(self):
        expected_phone_num = 07756134612
        self.user.set_phone_number(expected_phone_num)
        user_phone_number = self.user.get_phone_number()
        self.assertEquals(expected_phone_num, user_phone_number)

    def test_address(self):
        expected_address1 = "69 Albury Road"
        expected_address2 = "Merstham"
        self.user.set_address1(expected_address1)
        self.user.set_address2(expected_address2)
        user_address1 = self.user.get_address1()
        user_address2 = self.user.get_address2()

        self.assertEquals(expected_address1, user_address1)
        self.assertEquals(expected_address2, user_address2)

    def test_city(self):
        expected_city = "Redhill"
        self.user.set_city(expected_city)
        user_city = self.user.get_city()
        self.assertEquals(expected_city, user_city)

    def test_county(self):
        expected_county = "Surrey"
        self.user.set_county(expected_county)
        user_county = self.user.get_county()
        self.assertEquals(expected_county, user_county)

    def test_postcode(self):
        expected_postcode = "RH1 3LP"
        self.user.set_postcode(expected_postcode)
        user_postcode = self.user.get_postcode()
        self.assertEquals(expected_postcode, user_postcode)

    def test_photocard_id(self):
        expected_photocard_id = "MJD2214"
        self.user.set_photocard_id(expected_photocard_id)
        user_photocard_id = self.user.get_photocard_id()
        self.assertEquals(expected_photocard_id, user_photocard_id)

    def test_save(self):
        tmp_file = tempfile.NamedTemporaryFile('w').name

        title = 'Mr'
        self.user.set_title(title)

        forename = 'Adam'
        self.user.set_forename(forename)

        surname = 'Davis'
        self.user.set_surname(surname)

        email = 'davisadam10@googlemail.com'
        self.user.set_email(email)

        phone_number = 07756134612
        self.user.set_phone_number(phone_number)

        address1 = '69 Albury Road'
        address2 = 'Merstham'
        city = 'Redhill'
        county = 'Surrey'
        postcode = 'RH1 3LP'
        self.user.set_address1(address1)
        self.user.set_address2(address2)
        self.user.set_city(city)
        self.user.set_county(county)
        self.user.set_postcode(postcode)

        photocard_id = "MJD2214"
        self.user.set_photocard_id(photocard_id)

        self.user.save(tmp_file)



