__author__ = 'adam'


from unittest import TestCase
from nose.tools import *
import utils.userUtils as userUtils


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


secondName = "Davis"
email = "davisadam10@googlemail.com"
phoneNum = 07756134612
address1 = "69 Albury Road"
address2 = "Merstham"
city = "Redhill"
county = "Surrey"
postcode = "RH1 3LP"