__author__ = 'adam'


from unittest import TestCase
from nose.tools import *
import southern.utils.journeyUtils as journeyUtils

class test_Journey(TestCase):
    def setUp(self):
        self.journey = journeyUtils.Journey()

    def test_departing_station(self):
        expected_station = 'Merstham'
        self.journey.set_depart_station(expected_station)
        result = self.journey.get_depart_station()
        self.assertEquals(result, expected_station)

    def test_arriving_station(self):
        expected_station = 'London Victoria'
        self.journey.set_arriving_station(expected_station)
        result = self.journey.get_arriving_station()
        self.assertEquals(result, expected_station)

    def test_start_time_hour(self):
        hour = 1
        self.journey.set_start_time_hour(hour)
        result = self.journey.get_start_time_hour()
        self.assertEquals(hour, result)

    def test_start_time_min(self):
        minute = 32
        self.journey.set_start_time_min(minute)
        result = self.journey.get_start_time_min()
        self.assertEquals(minute, result)

    def test_end_time_hour(self):
        hour = 1
        self.journey.set_end_time_hour(hour)
        result = self.journey.get_end_time_hour()
        self.assertEquals(hour, result)

    def test_end_time_min(self):
        minute = 32
        self.journey.set_end_time_min(minute)
        result = self.journey.get_end_time_min()
        self.assertEquals(minute, result)

    def test_delay(self):
        delay = "60-119 mins"
        self.journey.set_delay_type(delay)
        result = self.journey.get_delay_type()
        self.assertEquals(delay, result)

    def test_delay_reason(self):
        delay_reason = "Delayed departure"
        self.journey.set_delay_reason(delay_reason)
        result = self.journey.get_delay_reason()
        self.assertEquals(result, delay_reason)

    def test_day(self):
        day = 1
        self.journey.set_day(day)
        result = self.journey.get_day()
        self.assertEquals(day, result)

    def test_month(self):
        month = 1
        self.journey.set_month(month)
        result = self.journey.get_month()
        month = str(month).zfill(2)
        self.assertEquals(result, month)

    def test_year(self):
        year = 2014
        self.journey.set_year(year)
        result = self.journey.get_year()
        self.assertEquals(result, year)


