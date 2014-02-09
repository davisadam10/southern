__author__ = 'adam'


from unittest import TestCase
from nose.tools import *
import datetime
import southern.utils.ticketUtils as ticketUtils


class test_Ticket(TestCase):
    def setUp(self):
        self.ticket = ticketUtils.Ticket()

    def test_set_ticket_type(self):
        ticket_type = 'monthly'
        self.ticket.set_ticket_type(ticket_type)
        result = self.ticket.get_ticket_type()
        self.assertEquals(result, ticket_type)

    def test_set_ticket_cost(self):
        cost = 285.70
        self.ticket.set_ticket_cost(cost)
        result = self.ticket.get_ticket_cost()
        self.assertEquals(result, cost)

    def test_ticket_start_date(self):
        day = 1
        month = 2
        year = 2014
        self.ticket.set_ticket_start_date(day, month, year)
        result = self.ticket.get_ticket_start_date()

        self.assertEquals(
                datetime.date(
                    day=day,
                    month=month,
                    year=year
                ),
            result)

    def test_ticket_end_date(self):
        day = 1
        month = 2
        year = 2014
        self.ticket.set_ticket_end_date(day, month, year)
        result = self.ticket.get_ticket_end_date()

        self.assertEquals(datetime.date(
            day=day,
            month=month,
            year=year
        ),
            result
        )