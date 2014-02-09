__author__ = 'adam'
import pickle


class SouthernBase(object):
    def validate(self):
        return True, []

    def save(self, file_path):
        """

        :param file_path: the file path we wish to save too
        :return: the file path saved out
        """
        valid, errors = self.validate()
        if valid:
            tmp_file = open(file_path, "w")
            pickle.dump(self, tmp_file)
            tmp_file.close()
            return file_path
        else:
            raise StandardError('\n'.join(errors))









'''


ticket_type_1 = "monthly"
cost = 285.70


arrivingStation = "Merstham"
departingStation = "London Victoria"

day = 13
month = str(01).zfill(2)
year = 2014

startTime = 19.10
arivingTime = 19.53

delay = "60-119 mins"
delayReason = "Delayed departure"


compensation = "National Rail Vouchers"

photocard_id = "MJD2214"

    '''