__author__ = 'adam'
import pickle


class User(object):
    def __init__(self):
        self.__title = ""
        self.__forename = ""
        self.__surname = ""
        self.__email = ""
        self.__phoneNum = 0
        self.__address1 = ""
        self.__address2 = ""
        self.__city = ""
        self.__county = ""
        self.__postcode = ""
        self.__photocard_id = ""

    def set_title(self, user_title):
        """

        @param user_title: Title of the user, ie Mr, Mrs etc..
        """
        self.__title = user_title

    def get_title(self):
        """


        @return: The title of the user
        """
        return self.__title

    def set_forename(self, forename):
        """

        @param forename: The users first name
        """
        self.__forename = forename

    def get_forename(self):
        return self.__forename

    def set_surname(self, surname):
        """

        @param surname: The users family name
        """
        self.__surname = surname

    def get_surname(self):
        """


        @return:
        """
        return self.__surname

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        """


        @return:
        """
        return self.__email

    def set_phone_number(self, phone_number):
        """

        @param phone_number:
        """
        self.__phoneNum = phone_number

    def get_phone_number(self):
        """


        @return:
        """
        return self.__phoneNum

    def set_address1(self, address):
        """

        @param address:
        """
        self.__address1 = address

    def get_address1(self):
        """


        @return:
        """
        return self.__address1

    def set_address2(self, address):
        """

        @param address:
        """
        self.__address2 = address

    def get_address2(self):
        """


        @return:
        """
        return self.__address2

    def set_city(self, city):
        self.__city = city

    def get_city(self):
        """


        @return:
        """
        return self.__city

    def set_county(self, county):
        """

        @param county:
        """
        self.__county = county

    def get_county(self):
        """


        @return:
        """
        return self.__county

    def set_postcode(self, postcode):
        """

        @param postcode:
        """
        self.__postcode = postcode

    def get_postcode(self):
        """


        @return:
        """
        return self.__postcode

    def set_photocard_id(self, photocard_id):
        """

        @param photocard_id:
        """
        self.__photocard_id = photocard_id

    def get_photocard_id(self):
        """


        @return:
        """
        return self.__photocard_id

    def save(self, file_path):
        """

        :param file_path: the file path we wish to save too
        :return: the file path saved out
        """
        tmp_file = open(file_path, "w")
        pickle.dump(self, tmp_file)
        tmp_file.close()
        return file_path







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