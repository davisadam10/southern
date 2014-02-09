__author__ = 'adam'
import pickle
import os


class Ticket(object):
    def __init__(self):
        self.__ticket_type = None
        self.__cost = None
        self.__ticket_photo_path = None
        self.__ticket_expire_date = None

    def set_ticket_type(self, ticket_type):
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



'''
ticket_type_1 = "monthly"
cost = 285.70
'''