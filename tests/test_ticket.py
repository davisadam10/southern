__author__ = 'adam'


from unittest import TestCase
from nose.tools import *
import southern.utils.ticketUtils as ticketUtils


class test_Ticker(TestCase):
    def setUp(self):
        self.ticket = ticketUtils.Ticket()

    def test_set_ticketType(self):
        ticket_type = 'monthly'
        self.ticket.set_ticket_type(ticket_type)
        result = self.ticket.get_ticket_type()
        self.assertEquals(result, ticket_type)

    def test_set_ticket_cost(self):
        cost = 285.70
        self.ticket.set_ticket_cost(cost)
        result = self.ticket.get_ticket_cost()
        self.assertEquals(result, cost)