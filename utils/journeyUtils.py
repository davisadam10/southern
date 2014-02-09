__author__ = 'adam'


class Journey(object):
    def __init__(self):
        """
        Class which is used to represent a journey, which can be stored
        to disk and reloaded for quick reuse.


        """
        self.__departing_station = ""
        self.__arriving_station = ""
        self.__day = 0
        self.__month = 0
        self.__year = 0
        self.__start_time_hour = 0
        self.__start_time_min = 0
        self.__end_time_hour = 0
        self.__end_time_min = 0
        self.__delay = ""
        self.__delay_reason = ""


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

    def set_delay_type(self, delay_type):
        self.__delay = delay_type

    def get_delay_type(self):
        return self.__delay

    def set_delay_reason(self, reason):
        self.__delay_reason = reason

    def get_delay_reason(self):
        return self.__delay_reason


