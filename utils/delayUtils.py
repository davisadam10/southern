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

        self.__delays = ['30-59 mins',
                         '60-119 mins',
                         '120+ mins']

        self.__delay_reasons = ['Train cancelled',
                                'Delayed on route',
                                'Missed connection',
                                'Delayed departure']

    def set_delay_type(self, delay_type):
        if not delay_type in self.__delays:
            raise ValueError('delay type not valid')

        self.__delay = delay_type

    def get_delay_type(self):
        return self.__delay

    def set_delay_reason(self, reason):
        if not reason in self.__delay_reasons:
            raise ValueError('Reason not a valid selection')
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




