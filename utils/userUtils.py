__author__ = 'adam'


class User ( object ):
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

    def set_title(self, user_title):
        self.__title = user_title



title = "Mr"
firstName = "Adam"
secondName = "Davis"
email = "davisadam10@googlemail.com"
phoneNum = 07756134612
address1 = "69 Albury Road"
address2 = "Merstham"
city = "Redhill"
county = "Surrey"
postcode = "RH1 3LP"
ticket_type_1 = "monthly"
cost = 285.70
day = 13
month = str(01).zfill(2)
year = 2014

startTime = 19.10
arivingTime = 19.53

delay = "60-119 mins"
delayReason = "Delayed departure"

arrivingStation = "Merstham"
departingStation = "London Victoria"

compensation = "National Rail Vouchers"

photocard_id = "MJD2214"