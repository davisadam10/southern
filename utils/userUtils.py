__author__ = 'adam'
import pickle
from southern.utils.baseUtils import SouthernBase


class User(SouthernBase):
    def __init__(self):
        self.__title = None
        self.__forename = None
        self.__surname = None
        self.__email = None
        self.__phoneNum = None
        self.__address1 = None
        self.__address2 = None
        self.__city = None
        self.__county = None
        self.__postcode = None
        self.__photocard_id = None

    def set_title(self, user_title):
        """

        :param user_title: Title of the user, ie Mr, Mrs etc..
        """
        self.__title = user_title

    def get_title(self):
        """


        :return: The title of the user
        """
        return self.__title

    def set_forename(self, forename):
        """

        :param forename: The users first name
        """
        self.__forename = forename

    def get_forename(self):
        return self.__forename

    def set_surname(self, surname):
        """

        :param surname: The users family name
        """
        self.__surname = surname

    def get_surname(self):
        """


        :return:
        """
        return self.__surname

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        """


        :return:
        """
        return self.__email

    def set_phone_number(self, phone_number):
        """

        :param phone_number:
        """
        self.__phoneNum = str(phone_number)

    def get_phone_number(self):
        """


        :return:
        """
        return str(self.__phoneNum)

    def set_address1(self, address):
        """

        :param address:
        """
        self.__address1 = address

    def get_address1(self):
        """


        :return:
        """
        return self.__address1

    def set_address2(self, address):
        """

        :param address:
        """
        self.__address2 = address

    def get_address2(self):
        """


        :return:
        """
        return self.__address2

    def set_city(self, city):
        self.__city = city

    def get_city(self):
        """


        :return:
        """
        return self.__city

    def set_county(self, county):
        """

        :param county:
        """
        self.__county = county

    def get_county(self):
        """


        :return:
        """
        return self.__county

    def set_postcode(self, postcode):
        """

        :param postcode:
        """
        self.__postcode = postcode

    def get_postcode(self):
        """


        :return: the post code of the user
        """
        return self.__postcode

    def set_photocard_id(self, photocard_id):
        """

        :param photocard_id: the photocard id of the user
        """
        self.__photocard_id = photocard_id

    def get_photocard_id(self):
        """


        :return: the photocard id of the user
        """
        return self.__photocard_id

    def validate(self):
        valid = True
        errors = []
        if not self.__title:
            valid = False
            errors.append('User: title not set')

        if not self.__forename:
            valid = False
            errors.append('User: forename not set')

        if not self.__surname:
            valid = False
            errors.append('User: surname not set')

        if not self.__email:
            valid = False
            errors.append('User: email address not set')

        if not self.__phoneNum:
            valid = False
            errors.append('User: phone number not set')

        if not self.__address1:
            valid = False
            errors.append('User: address line 1 not set')

        if not self.__address2:
            vaild = False
            errors.append('User: address line 2 not set')

        if not self.__city:
            valid = False
            errors.append('User: city not set')

        if not self.__county:
            valid = False
            errors.append('User: county not set')

        if not self.__postcode:
            valid = False
            errors.append('User: postcode not set')

        if not self.__photocard_id:
            valid = False
            errors.append('User: photocard id not set')

        return valid, errors


'''


ticket_type_1 = "monthly"
cost = 285.70


arrivingStation = "Merstham"
departingStation = "London Victoria"

day = 13
month = str(01).zfill(2)
year = 2014

startTime = 19.10
arivingTime = 19.53

delay = "60-119 mins"
delayReason = "Delayed departure"


compensation = "National Rail Vouchers"

photocard_id = "MJD2214"

    '''