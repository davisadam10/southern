__author__ = 'adam'


from unittest import TestCase
from nose.tools import *
import southern.utils.delayUtils as delayUtils
import tempfile


class test_Delay(TestCase):
    def setUp(self):
        self.delay = delayUtils.Delay()

    def test_delay(self):
        delay = "60-119 mins"
        self.delay.set_delay_type(delay)
        result = self.delay.get_delay_type()
        self.assertEquals(delay, result)

    def test_delay_reason(self):
        delay_reason = "Delayed departure"
        self.delay.set_delay_reason(delay_reason)
        result = self.delay.get_delay_reason()
        self.assertEquals(result, delay_reason)


    def test_save(self):
        tmp_file = tempfile.NamedTemporaryFile('w').name

        delayType = "60-119 mins"
        self.delay.set_delay_type(delayType)

        delayReason = "Delayed departure"
        self.delay.set_delay_reason(delayReason)

        self.delay.save(tmp_file)




