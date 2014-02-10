__author__ = 'adam'
import sys
from PyQt4 import QtCore, QtGui
from southern.ui.mainUI import Ui_MainWindow
from southern.utils.userUtils import User
from southern.utils.delayUtils import Delay
from southern.utils.journeyUtils import Journey
from southern.utils.ticketUtils import Ticket
from southern.utils import delayRepayUtils


class MainUI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user = User()
        self.journey = Journey()
        self.ticket = Ticket()
        self.delay = Delay()

        # Connect up ui signals
        self.ui.titleComboBox.currentIndexChanged.connect(self.set_user_title)
        self.ui.forenameLineEdit.editingFinished.connect(self.set_user_forename)
        self.ui.surnameLineEdit.editingFinished.connect(self.set_user_surname)
        self.ui.emailLineEdit.editingFinished.connect(self.set_user_email)
        self.ui.phoneLineEdit.editingFinished.connect(self.set_user_phone)
        self.ui.photocardIdLineEdit.editingFinished.connect(self.set_user_photo_id)
        self.ui.address1LineEdit.editingFinished.connect(self.set_user_address1)
        self.ui.address2LineEdit.editingFinished.connect(self.set_user_address2)
        self.ui.cityLineEdit.editingFinished.connect(self.set_user_city)
        self.ui.countyLineEdit.editingFinished.connect(self.set_user_county)
        self.ui.postcodeLineEdit.editingFinished.connect(self.set_user_postcode)

        self.ui.departingStationCombo.currentIndexChanged.connect(self.set_journey_depart)
        self.ui.departureHourCombo.currentIndexChanged.connect(self.set_journey_depart_time)
        self.ui.departureMinCombo.currentIndexChanged.connect(self.set_journey_depart_time)
        self.ui.arrivalHour_Combo.currentIndexChanged.connect(self.set_journey_arrive_time)
        self.ui.arrivalMin_Combo.currentIndexChanged.connect(self.set_journey_arrive_time)

        self.ui.actionPassenger_InfoSave.triggered.connect(self.save_user_settings)
        self.ui.actionPassenger_InfoLoad.triggered.connect(self.load_user_settings)
        self.ui.submitCLaimButton.clicked.connect(self.submit_claim)

    def submit_claim(self):
        valid = []
        errors = []

        user_valid, user_errors = self.user.validate()
        valid.append(user_valid)
        errors.extend(user_errors)

        journey_valid, journey_errors = self.journey.validate()
        valid.append(journey_valid)
        errors.extend(journey_errors)

        ticket_valid, ticket_errors = self.ticket.validate()
        valid.append(ticket_valid)
        errors.extend(ticket_errors)

        delay_valid, delay_errors = self.delay.validate()
        valid.append(delay_valid)
        errors.extend(delay_errors)

        if not False in valid:
            QtGui.QMessageBox.information( self, 'Sucess', "Delay Repay Submitted - Check Your Email")
            #Run Submit
        else:
            QtGui.QMessageBox.critical( self, 'Error: Incomplete Form', "\n".join(errors))
            return

    def save_user_settings(self):
        file_type = '.DRPUser'
        file_name = QtGui.QFileDialog.getSaveFileName( self, "Save User Settings", "/home/adam", "*%s"%(file_type), "*%s"%(file_type))
        if file_name:
            file_name = str(file_name)
            if not file_name.endswith(file_type):
                file_name += file_type
            valid, errors = self.user.validate()
            if not valid:
                QtGui.QMessageBox.critical( self, 'Error: Incomplete Form', "\n".join(errors))
            else:
                self.user.save(file_name)
                QtGui.QMessageBox.information( self, 'Sucess', "User Settings Saved")

    def load_user_settings(self):
        file_type = '.DRPUser'
        file_name = QtGui.QFileDialog.getOpenFileName( self, "Save User Settings", "/home/adam", "*%s"%(file_type), "*%s"%(file_type))
        if file_name:
            self.user = delayRepayUtils.load_setting(file_name)
            self.refresh_user_ui()

    def refresh_user_ui(self):
        title = self.user.get_title()
        x = 0
        while x in xrange(self.ui.titleComboBox.count()):
            item = str(self.ui.titleComboBox.itemText(x))
            if item == title:
                self.ui.titleComboBox.setCurrentIndex(x)
            x += 1

        forename = self.user.get_forename()
        self.ui.forenameLineEdit.setText(forename)

        surname = self.user.get_surname()
        self.ui.surnameLineEdit.setText(surname)

        email = self.user.get_email()
        self.ui.emailLineEdit.setText(email)

        phone_num = self.user.get_phone_number()
        self.ui.phoneLineEdit.setText(phone_num)

        photocard_id = self.user.get_photocard_id()
        self.ui.photocardIdLineEdit.setText(photocard_id)

        address1 = self.user.get_address1()
        address2 = self.user.get_address2()
        self.ui.address1LineEdit.setText(address1)
        self.ui.address2LineEdit.setText(address2)

        city = self.user.get_city()
        county = self.user.get_county()
        postcode = self.user.get_postcode()
        self.ui.cityLineEdit.setText(city)
        self.ui.countyLineEdit.setText(county)
        self.ui.postcodeLineEdit.setText(postcode)

    def set_user_title(self):
        title = self.ui.titleComboBox.currentText()
        self.user.set_title(title)

    def set_user_forename(self):
        forename = self.ui.forenameLineEdit.text()
        self.user.set_forename(str(forename))

    def set_user_surname(self):
        surname = self.ui.surnameLineEdit.text()
        self.user.set_surname(str(surname))

    def set_user_email(self):
        email = self.ui.emailLineEdit.text()
        self.user.set_email(str(email))

    def set_user_phone(self):
        phone = self.ui.phoneLineEdit.text()
        self.user.set_phone_number(str(phone))

    def set_user_photo_id(self):
        photo_id = self.ui.photocardIdLineEdit.text()
        self.user.set_photocard_id(str(photo_id))

    def set_user_address1(self):
        address1 = self.ui.address1LineEdit.text()
        self.user.set_address1(str(address1))

    def set_user_address2(self):
        address2 = self.ui.address2LineEdit.text()
        self.user.set_address2(str(address2))

    def set_user_county(self):
        county = self.ui.countyLineEdit.text()
        self.user.set_county(str(county))

    def set_user_city(self):
        city = self.ui.cityLineEdit.text()
        self.user.set_city(str(city))

    def set_user_postcode(self):
        postcode = self.ui.postcodeLineEdit.text()
        self.user.set_postcode(postcode)

    def set_journey_depart(self):
        departing_station = self.ui.departingStationCombo.currentText()
        self.journey.set_depart_station(str(departing_station))

    def set_journey_depart_time(self):
        depart_hour = self.ui.departureHourCombo.currentText()
        depart_min = self.ui.departureMinCombo.currentText()

        self.journey.set_start_time_hour(str(depart_hour))
        self.journey.set_start_time_min(str(depart_min))

    def set_journey_arrive_time(self):
        arrive_hour = self.ui.arrivalHour_Combo.currentText()
        arrive_min = self.ui.arrivalMin_Combo.currentText()

        self.journey.set_end_time_hour(str(arrive_hour))
        self.journey.set_end_time_min(str(arrive_min))











app = QtGui.QApplication(sys.argv)
window = MainUI()
window.show()
sys.exit(app.exec_())


