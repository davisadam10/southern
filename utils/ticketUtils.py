__author__ = 'adam'
import datetime
import os
from southern.utils.baseUtils import SouthernBase


class Ticket(SouthernBase):
    def __init__(self):
        self.__ticket_type = None
        self.__cost = None
        self.__ticket_photo_path = None

        self.__ticket_start_day = None
        self.__ticket_start_month = None
        self.__ticket_start_year = None

        self.__ticket_expire_day = None
        self.__ticket_expire_month = None
        self.__ticket_expire_year = None

        self.__valid_ticket_types = ['monthly']

    def set_ticket_type(self, ticket_type):
        if ticket_type not in self.__valid_ticket_types:
            raise ValueError('Ticket Type not valid')
        self.__ticket_type = ticket_type

    def get_ticket_type(self):
        return self.__ticket_type

    def set_ticket_cost(self, cost):
        self.__cost = cost

    def get_ticket_cost(self):
        return self.__cost

    def set_ticket_photo_path(self, path):
        if not os.path.exists(path):
            raise OSError("File Path to your photo does not exist")
        if not path.endswith('.jpg') or not path.endswith('jpeg'):
            raise OSError("File type needs to be JPG")
        self.__ticket_photo_path = path

    def get_ticket_photo_path(self):
        return self.__ticket_photo_path

    def set_ticket_start_date(self, day, month, year):
        self.__ticket_start_day = day
        self.__ticket_start_month = month
        self.__ticket_start_year = year

    def get_ticket_start_date(self):
        return datetime.date(day=self.__ticket_start_day,
                             month=self.__ticket_start_month,
                             year=self.__ticket_start_year
        )

    def set_ticket_end_date(self, day, month, year):
        self.__ticket_expire_day = day
        self.__ticket_expire_month = month
        self.__ticket_expire_year = year

    def get_ticket_end_date(self):
        return datetime.date(day=self.__ticket_expire_day,
                             month=self.__ticket_expire_month,
                             year=self.__ticket_expire_year
        )

    def validate(self):
        valid = True
        errors = []

        if not self.__ticket_type:
            valid = False
            errors.append('Ticket: ticket type not set')

        if not self.__cost:
            valid = False
            errors.append('Ticket: cost not set')

        if not self.__ticket_photo_path:
            valid = False
            errors.append('Ticket: photo path not set')

        #todo
        #self.__ticket_expire_date = None

        return valid, errors






'''
ticket_type_1 = "monthly"
cost = 285.70
'''