__author__ = 'adam'
from southern.utils.baseUtils import SouthernBase


class Delay(SouthernBase):
    def __init__(self):
        """
        Class which is used to represent a delay, which can be stored
        to disk and reloaded for quick reuse.


        """
        self.__delay = None
        self.__delay_reason = None

    def set_delay_type(self, delay_type):
        self.__delay = delay_type

    def get_delay_type(self):
        return self.__delay

    def set_delay_reason(self, reason):
        self.__delay_reason = reason

    def get_delay_reason(self):
        return self.__delay_reason

    def validate(self):
        valid = True
        errors = []

        if not self.__delay:
            valid = False
            errors.append('Delay: type of delay not set')

        if not self.__delay_reason:
            valid = False
            errors.append('Delay: delay reason not set')

        return valid, errors




