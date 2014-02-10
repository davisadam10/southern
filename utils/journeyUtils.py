__author__ = 'adam'
from southern.utils.baseUtils import SouthernBase


class Journey(SouthernBase):
    def __init__(self):
        """
        Class which is used to represent a journey, which can be stored
        to disk and reloaded for quick reuse.


        """
        self.__departing_station = None
        self.__arriving_station = None
        self.__day = None
        self.__month = None
        self.__year = None
        self.__start_time_hour = None
        self.__start_time_min = None
        self.__end_time_hour = None
        self.__end_time_min = None

    def set_depart_station(self, station):
        """

        :param station: the name of the station the journey departed from
        """
        self.__departing_station = station

    def get_depart_station(self):
        """


        :return: the name of the station the journey departed from
        """
        return self.__departing_station

    def set_arriving_station(self, station):
        """

        :param station: the name of the station the journey arrives at
        """
        self.__arriving_station = station

    def get_arriving_station(self):
        """


        :return: the name of the station the journey arrives at
        """
        return self.__arriving_station

    def set_day(self, day):
        """

        :param day: the day which the journey took place
        """
        self.__day = day

    def get_day(self):
        """

        :param day: the day which the journey took place
        """
        return self.__day

    def set_month(self, month):
        """

        :param month: the month which the journey took place
        """

        self.__month = str(month).zfill(2)

    def get_month(self):

        """


        :return: the month which the journey took place
        """
        return self.__month

    def set_year(self, year):
        """

        :param year: the year which the journey took place
        """
        self.__year = year

    def get_year(self):
        """


        :return: the year which the journey took place
        """
        return self.__year

    def set_start_time_hour(self, hour):
        """

        :param hour: the hour the journey began
        """
        self.__start_time_hour = hour

    def get_start_time_hour(self):
        """


        :return: the hour the journey began
        """
        return self.__start_time_hour

    def set_start_time_min(self, minute):
        """

        :param minute: the minute that the journey began
        """
        self.__start_time_min = minute

    def get_start_time_min(self):
        """


        :return: the minute that the journey began
        """
        return self.__start_time_min

    def set_end_time_hour(self, hour):
        self.__end_time_hour = hour

    def get_end_time_hour(self):
        return self.__end_time_hour

    def set_end_time_min(self, minute):
        self.__end_time_min = minute

    def get_end_time_min(self):
        return self.__end_time_min

    def validate(self):
        valid = True
        errors = []

        if not self.__departing_station:
            valid = False
            errors.append('Journey: departing station not set')

        if not self.__arriving_station:
            valid = False
            errors.append('Journey: arriving station not set')

        if not self.__day:
            valid = False
            errors.append('Journey: day not set')

        if not self.__month:
            valid = False
            errors.append('Journey: month not set')

        if not self.__year:
            valid = False
            errors.append('Journey: year not set')

        if not self.__start_time_hour:
            valid = False
            errors.append('Jounrey: start hour not set')

        if not self.__start_time_min:
            valid = False
            errors.append('Journey: start min not set')

        if not self.__end_time_hour:
            valid = False
            errors.append('Journey: end hour not set')

        if not self.__end_time_min:
            valid = False
            errors.append('Journey: end min not set')

        return valid, errors

