__author__ = 'adam'
import pickle


class Ticket(object):
    def __init__(self):
        self.__ticket_type = ""
        self.__cost = None

    def set_ticket_type(self, ticket_type):
        self.__ticket_type = ticket_type

    def get_ticket_type(self):
        return self.__ticket_type

    def set_ticket_cost(self, cost):
        self.__cost = cost

    def get_ticket_cost(self):
        return self.__cost


'''
ticket_type_1 = "monthly"
cost = 285.70
'''