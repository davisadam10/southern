__author__ = 'adam'


class Journey(object):
    def __init__(self):
        self.departing_station = ""
        self.arriving_station = ""
        self.start_time_hour = 0
        self.start_time_min = 0
        self.end_time_hour = 0
        self.end_time_min = 0
        self.delay = ""
        self.delay_reason = ""

    def set_depart_station(self, station):
        self.departing_station = station

    def get_depart_station(self):
        return self.departing_station

    def set_arriving_station(self, station):
        self.arriving_station = station

    def get_arriving_station(self):
        return self.arriving_station

    def set_start_time_hour(self, hour):
        self.start_time_hour = hour

    def get_start_time_hour(self):
        return self.start_time_hour

    def set_start_time_min(self, minute):
        self.start_time_min = minute

    def get_start_time_min(self):
        return self.start_time_min

    def set_end_time_hour(self, hour):
        self.end_time_hour = hour

    def get_end_time_hour(self):
        return self.end_time_hour

    def set_end_time_min(self, minute):
        self.end_time_min = minute

    def get_end_time_min(self):
        return self.end_time_min

    def set_delay_type(self, delay_type):
        self.delay = delay_type

    def get_delay_type(self):
        return self.delay

    def set_delay_reason(self, reason):
        self.delay_reason = reason

    def get_delay_reason(self):
        return self.delay_reason


