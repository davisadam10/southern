# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Mon Feb 10 17:09:30 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(775, 595)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mainTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.mainTabWidget.setGeometry(QtCore.QRect(0, 0, 711, 551))
        self.mainTabWidget.setObjectName(_fromUtf8("mainTabWidget"))
        self.userTab = QtGui.QWidget()
        self.userTab.setObjectName(_fromUtf8("userTab"))
        self.journeyInfoGroupBox = QtGui.QGroupBox(self.userTab)
        self.journeyInfoGroupBox.setGeometry(QtCore.QRect(10, 230, 341, 181))
        self.journeyInfoGroupBox.setObjectName(_fromUtf8("journeyInfoGroupBox"))
        self.departureMinCombo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.departureMinCombo.setGeometry(QtCore.QRect(260, 50, 81, 27))
        self.departureMinCombo.setObjectName(_fromUtf8("departureMinCombo"))
        self.departureHourCombo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.departureHourCombo.setGeometry(QtCore.QRect(160, 50, 81, 27))
        self.departureHourCombo.setObjectName(_fromUtf8("departureHourCombo"))
        self.journeyDat_label = QtGui.QLabel(self.journeyInfoGroupBox)
        self.journeyDat_label.setGeometry(QtCore.QRect(10, 140, 131, 27))
        self.journeyDat_label.setObjectName(_fromUtf8("journeyDat_label"))
        self.arrivalMin_Combo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.arrivalMin_Combo.setGeometry(QtCore.QRect(260, 110, 81, 27))
        self.arrivalMin_Combo.setObjectName(_fromUtf8("arrivalMin_Combo"))
        self.journeyDate_YearCombo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.journeyDate_YearCombo.setGeometry(QtCore.QRect(260, 140, 81, 27))
        self.journeyDate_YearCombo.setObjectName(_fromUtf8("journeyDate_YearCombo"))
        self.arrivingStationCombo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.arrivingStationCombo.setGeometry(QtCore.QRect(160, 80, 181, 27))
        self.arrivingStationCombo.setObjectName(_fromUtf8("arrivingStationCombo"))
        self.arrivingStationCombo.addItem(_fromUtf8(""))
        self.arrivingStationCombo.setItemText(0, _fromUtf8(""))
        self.arrivingStationCombo.addItem(_fromUtf8(""))
        self.arrivingStationCombo.addItem(_fromUtf8(""))
        self.arrivingStationCombo.addItem(_fromUtf8(""))
        self.arrivingStationCombo.addItem(_fromUtf8(""))
        self.arrivalHour_Combo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.arrivalHour_Combo.setGeometry(QtCore.QRect(160, 110, 81, 27))
        self.arrivalHour_Combo.setObjectName(_fromUtf8("arrivalHour_Combo"))
        self.departingStationLabel = QtGui.QLabel(self.journeyInfoGroupBox)
        self.departingStationLabel.setGeometry(QtCore.QRect(10, 20, 131, 27))
        self.departingStationLabel.setObjectName(_fromUtf8("departingStationLabel"))
        self.departureTimeLabel = QtGui.QLabel(self.journeyInfoGroupBox)
        self.departureTimeLabel.setGeometry(QtCore.QRect(10, 50, 131, 27))
        self.departureTimeLabel.setObjectName(_fromUtf8("departureTimeLabel"))
        self.arrivingStation = QtGui.QLabel(self.journeyInfoGroupBox)
        self.arrivingStation.setGeometry(QtCore.QRect(10, 80, 131, 27))
        self.arrivingStation.setObjectName(_fromUtf8("arrivingStation"))
        self.journeyDate_MonthCombo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.journeyDate_MonthCombo.setGeometry(QtCore.QRect(210, 140, 51, 27))
        self.journeyDate_MonthCombo.setObjectName(_fromUtf8("journeyDate_MonthCombo"))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.setItemText(0, _fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.journeyDate_MonthCombo.addItem(_fromUtf8(""))
        self.departingStationCombo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.departingStationCombo.setGeometry(QtCore.QRect(160, 20, 181, 27))
        self.departingStationCombo.setObjectName(_fromUtf8("departingStationCombo"))
        self.departingStationCombo.addItem(_fromUtf8(""))
        self.departingStationCombo.setItemText(0, _fromUtf8(""))
        self.departingStationCombo.addItem(_fromUtf8(""))
        self.departingStationCombo.addItem(_fromUtf8(""))
        self.departingStationCombo.addItem(_fromUtf8(""))
        self.departingStationCombo.addItem(_fromUtf8(""))
        self.journeyDate_DayCombo = QtGui.QComboBox(self.journeyInfoGroupBox)
        self.journeyDate_DayCombo.setGeometry(QtCore.QRect(160, 140, 51, 27))
        self.journeyDate_DayCombo.setObjectName(_fromUtf8("journeyDate_DayCombo"))
        self.arrivalTimeLabel = QtGui.QLabel(self.journeyInfoGroupBox)
        self.arrivalTimeLabel.setGeometry(QtCore.QRect(10, 110, 131, 27))
        self.arrivalTimeLabel.setObjectName(_fromUtf8("arrivalTimeLabel"))
        self.TicketInfoGroupBox = QtGui.QGroupBox(self.userTab)
        self.TicketInfoGroupBox.setGeometry(QtCore.QRect(360, 230, 381, 201))
        self.TicketInfoGroupBox.setObjectName(_fromUtf8("TicketInfoGroupBox"))
        self.ticketTypeLabel = QtGui.QLabel(self.TicketInfoGroupBox)
        self.ticketTypeLabel.setGeometry(QtCore.QRect(30, 20, 131, 27))
        self.ticketTypeLabel.setObjectName(_fromUtf8("ticketTypeLabel"))
        self.costLineEdit = QtGui.QLineEdit(self.TicketInfoGroupBox)
        self.costLineEdit.setGeometry(QtCore.QRect(130, 50, 201, 27))
        self.costLineEdit.setObjectName(_fromUtf8("costLineEdit"))
        self.validFromDate_Combo_2 = QtGui.QComboBox(self.TicketInfoGroupBox)
        self.validFromDate_Combo_2.setGeometry(QtCore.QRect(130, 110, 51, 27))
        self.validFromDate_Combo_2.setObjectName(_fromUtf8("validFromDate_Combo_2"))
        self.firstNameLabel_2 = QtGui.QLabel(self.TicketInfoGroupBox)
        self.firstNameLabel_2.setGeometry(QtCore.QRect(30, 50, 91, 27))
        self.firstNameLabel_2.setObjectName(_fromUtf8("firstNameLabel_2"))
        self.validFromDate_Combo = QtGui.QComboBox(self.TicketInfoGroupBox)
        self.validFromDate_Combo.setGeometry(QtCore.QRect(130, 80, 51, 27))
        self.validFromDate_Combo.setObjectName(_fromUtf8("validFromDate_Combo"))
        self.validUntilLabel = QtGui.QLabel(self.TicketInfoGroupBox)
        self.validUntilLabel.setGeometry(QtCore.QRect(30, 110, 101, 27))
        self.validUntilLabel.setObjectName(_fromUtf8("validUntilLabel"))
        self.validFromMonth_Combo = QtGui.QComboBox(self.TicketInfoGroupBox)
        self.validFromMonth_Combo.setGeometry(QtCore.QRect(180, 80, 51, 27))
        self.validFromMonth_Combo.setObjectName(_fromUtf8("validFromMonth_Combo"))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.setItemText(0, _fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.validFromMonth_Combo.addItem(_fromUtf8(""))
        self.photopathLineEdit = QtGui.QLineEdit(self.TicketInfoGroupBox)
        self.photopathLineEdit.setGeometry(QtCore.QRect(130, 140, 151, 27))
        self.photopathLineEdit.setObjectName(_fromUtf8("photopathLineEdit"))
        self.validFromLabel = QtGui.QLabel(self.TicketInfoGroupBox)
        self.validFromLabel.setGeometry(QtCore.QRect(30, 80, 101, 27))
        self.validFromLabel.setObjectName(_fromUtf8("validFromLabel"))
        self.validUntilMonth_Combo = QtGui.QComboBox(self.TicketInfoGroupBox)
        self.validUntilMonth_Combo.setGeometry(QtCore.QRect(180, 110, 51, 27))
        self.validUntilMonth_Combo.setObjectName(_fromUtf8("validUntilMonth_Combo"))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.setItemText(0, _fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.validUntilMonth_Combo.addItem(_fromUtf8(""))
        self.ticketTypeCombo = QtGui.QComboBox(self.TicketInfoGroupBox)
        self.ticketTypeCombo.setGeometry(QtCore.QRect(130, 20, 201, 27))
        self.ticketTypeCombo.setObjectName(_fromUtf8("ticketTypeCombo"))
        self.ticketTypeCombo.addItem(_fromUtf8(""))
        self.ticketTypeCombo.setItemText(0, _fromUtf8(""))
        self.ticketTypeCombo.addItem(_fromUtf8(""))
        self.ticketTypeCombo.addItem(_fromUtf8(""))
        self.photoBrowseButton = QtGui.QPushButton(self.TicketInfoGroupBox)
        self.photoBrowseButton.setGeometry(QtCore.QRect(130, 170, 151, 27))
        self.photoBrowseButton.setObjectName(_fromUtf8("photoBrowseButton"))
        self.validFromYearCombo = QtGui.QComboBox(self.TicketInfoGroupBox)
        self.validFromYearCombo.setGeometry(QtCore.QRect(230, 80, 101, 27))
        self.validFromYearCombo.setObjectName(_fromUtf8("validFromYearCombo"))
        self.validUntilYearCombo = QtGui.QComboBox(self.TicketInfoGroupBox)
        self.validUntilYearCombo.setGeometry(QtCore.QRect(230, 110, 101, 27))
        self.validUntilYearCombo.setObjectName(_fromUtf8("validUntilYearCombo"))
        self.firstNameLabel_3 = QtGui.QLabel(self.TicketInfoGroupBox)
        self.firstNameLabel_3.setGeometry(QtCore.QRect(30, 140, 91, 27))
        self.firstNameLabel_3.setObjectName(_fromUtf8("firstNameLabel_3"))
        self.groupBox = QtGui.QGroupBox(self.userTab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 691, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.photocardIdLabel = QtGui.QLabel(self.groupBox)
        self.photocardIdLabel.setGeometry(QtCore.QRect(20, 170, 91, 27))
        self.photocardIdLabel.setObjectName(_fromUtf8("photocardIdLabel"))
        self.countyLineEdit = QtGui.QLineEdit(self.groupBox)
        self.countyLineEdit.setGeometry(QtCore.QRect(480, 140, 209, 27))
        self.countyLineEdit.setText(_fromUtf8(""))
        self.countyLineEdit.setObjectName(_fromUtf8("countyLineEdit"))
        self.firstNameLabel = QtGui.QLabel(self.groupBox)
        self.firstNameLabel.setGeometry(QtCore.QRect(20, 50, 74, 27))
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.address1LineEdit = QtGui.QLineEdit(self.groupBox)
        self.address1LineEdit.setGeometry(QtCore.QRect(480, 50, 209, 27))
        self.address1LineEdit.setText(_fromUtf8(""))
        self.address1LineEdit.setObjectName(_fromUtf8("address1LineEdit"))
        self.cityLabel = QtGui.QLabel(self.groupBox)
        self.cityLabel.setGeometry(QtCore.QRect(380, 110, 74, 27))
        self.cityLabel.setObjectName(_fromUtf8("cityLabel"))
        self.emailLineEdit = QtGui.QLineEdit(self.groupBox)
        self.emailLineEdit.setGeometry(QtCore.QRect(120, 110, 209, 27))
        self.emailLineEdit.setText(_fromUtf8(""))
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.cityLineEdit = QtGui.QLineEdit(self.groupBox)
        self.cityLineEdit.setGeometry(QtCore.QRect(480, 110, 209, 27))
        self.cityLineEdit.setText(_fromUtf8(""))
        self.cityLineEdit.setObjectName(_fromUtf8("cityLineEdit"))
        self.photocardIdLineEdit = QtGui.QLineEdit(self.groupBox)
        self.photocardIdLineEdit.setGeometry(QtCore.QRect(120, 170, 209, 27))
        self.photocardIdLineEdit.setText(_fromUtf8(""))
        self.photocardIdLineEdit.setObjectName(_fromUtf8("photocardIdLineEdit"))
        self.postcodeLineEdit = QtGui.QLineEdit(self.groupBox)
        self.postcodeLineEdit.setGeometry(QtCore.QRect(480, 170, 209, 27))
        self.postcodeLineEdit.setText(_fromUtf8(""))
        self.postcodeLineEdit.setObjectName(_fromUtf8("postcodeLineEdit"))
        self.address2Label = QtGui.QLabel(self.groupBox)
        self.address2Label.setGeometry(QtCore.QRect(380, 80, 74, 27))
        self.address2Label.setObjectName(_fromUtf8("address2Label"))
        self.surnameLabel = QtGui.QLabel(self.groupBox)
        self.surnameLabel.setGeometry(QtCore.QRect(20, 80, 74, 27))
        self.surnameLabel.setObjectName(_fromUtf8("surnameLabel"))
        self.surnameLineEdit = QtGui.QLineEdit(self.groupBox)
        self.surnameLineEdit.setGeometry(QtCore.QRect(120, 80, 209, 27))
        self.surnameLineEdit.setObjectName(_fromUtf8("surnameLineEdit"))
        self.address2LineEdit = QtGui.QLineEdit(self.groupBox)
        self.address2LineEdit.setGeometry(QtCore.QRect(480, 80, 209, 27))
        self.address2LineEdit.setText(_fromUtf8(""))
        self.address2LineEdit.setObjectName(_fromUtf8("address2LineEdit"))
        self.phoneLabel = QtGui.QLabel(self.groupBox)
        self.phoneLabel.setGeometry(QtCore.QRect(20, 140, 74, 27))
        self.phoneLabel.setObjectName(_fromUtf8("phoneLabel"))
        self.phoneLineEdit = QtGui.QLineEdit(self.groupBox)
        self.phoneLineEdit.setGeometry(QtCore.QRect(120, 140, 209, 27))
        self.phoneLineEdit.setText(_fromUtf8(""))
        self.phoneLineEdit.setObjectName(_fromUtf8("phoneLineEdit"))
        self.titleLabel = QtGui.QLabel(self.groupBox)
        self.titleLabel.setGeometry(QtCore.QRect(20, 20, 74, 27))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.postCodeLabel = QtGui.QLabel(self.groupBox)
        self.postCodeLabel.setGeometry(QtCore.QRect(380, 170, 74, 27))
        self.postCodeLabel.setObjectName(_fromUtf8("postCodeLabel"))
        self.titleComboBox = QtGui.QComboBox(self.groupBox)
        self.titleComboBox.setGeometry(QtCore.QRect(120, 20, 78, 27))
        self.titleComboBox.setObjectName(_fromUtf8("titleComboBox"))
        self.titleComboBox.addItem(_fromUtf8(""))
        self.titleComboBox.setItemText(0, _fromUtf8(""))
        self.titleComboBox.addItem(_fromUtf8(""))
        self.titleComboBox.addItem(_fromUtf8(""))
        self.titleComboBox.addItem(_fromUtf8(""))
        self.titleComboBox.addItem(_fromUtf8(""))
        self.countyLabel = QtGui.QLabel(self.groupBox)
        self.countyLabel.setGeometry(QtCore.QRect(380, 140, 74, 27))
        self.countyLabel.setObjectName(_fromUtf8("countyLabel"))
        self.forenameLineEdit = QtGui.QLineEdit(self.groupBox)
        self.forenameLineEdit.setGeometry(QtCore.QRect(120, 50, 209, 27))
        self.forenameLineEdit.setObjectName(_fromUtf8("forenameLineEdit"))
        self.address1Label = QtGui.QLabel(self.groupBox)
        self.address1Label.setGeometry(QtCore.QRect(380, 50, 74, 27))
        self.address1Label.setObjectName(_fromUtf8("address1Label"))
        self.emailLabel = QtGui.QLabel(self.groupBox)
        self.emailLabel.setGeometry(QtCore.QRect(20, 110, 74, 27))
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.groupBox_2 = QtGui.QGroupBox(self.userTab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 420, 341, 81))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.delayTypeLabel = QtGui.QLabel(self.groupBox_2)
        self.delayTypeLabel.setGeometry(QtCore.QRect(10, 20, 131, 27))
        self.delayTypeLabel.setObjectName(_fromUtf8("delayTypeLabel"))
        self.delayReason_Label = QtGui.QLabel(self.groupBox_2)
        self.delayReason_Label.setGeometry(QtCore.QRect(10, 50, 131, 27))
        self.delayReason_Label.setObjectName(_fromUtf8("delayReason_Label"))
        self.delayTypeCombo = QtGui.QComboBox(self.groupBox_2)
        self.delayTypeCombo.setGeometry(QtCore.QRect(110, 20, 151, 27))
        self.delayTypeCombo.setObjectName(_fromUtf8("delayTypeCombo"))
        self.delayTypeCombo.addItem(_fromUtf8(""))
        self.delayTypeCombo.setItemText(0, _fromUtf8(""))
        self.delayTypeCombo.addItem(_fromUtf8(""))
        self.delayTypeCombo.addItem(_fromUtf8(""))
        self.delayTypeCombo.addItem(_fromUtf8(""))
        self.delayReason_Combo = QtGui.QComboBox(self.groupBox_2)
        self.delayReason_Combo.setGeometry(QtCore.QRect(110, 50, 151, 27))
        self.delayReason_Combo.setObjectName(_fromUtf8("delayReason_Combo"))
        self.delayReason_Combo.addItem(_fromUtf8(""))
        self.delayReason_Combo.setItemText(0, _fromUtf8(""))
        self.delayReason_Combo.addItem(_fromUtf8(""))
        self.delayReason_Combo.addItem(_fromUtf8(""))
        self.delayReason_Combo.addItem(_fromUtf8(""))
        self.delayReason_Combo.addItem(_fromUtf8(""))
        self.submitCLaimButton = QtGui.QPushButton(self.userTab)
        self.submitCLaimButton.setGeometry(QtCore.QRect(490, 440, 151, 51))
        self.submitCLaimButton.setObjectName(_fromUtf8("submitCLaimButton"))
        self.mainTabWidget.addTab(self.userTab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 25))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuLoad_Settings = QtGui.QMenu(self.menuFile)
        self.menuLoad_Settings.setObjectName(_fromUtf8("menuLoad_Settings"))
        self.menuSave_Settings = QtGui.QMenu(self.menuFile)
        self.menuSave_Settings.setObjectName(_fromUtf8("menuSave_Settings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPassenger_InfoLoad = QtGui.QAction(MainWindow)
        self.actionPassenger_InfoLoad.setObjectName(_fromUtf8("actionPassenger_InfoLoad"))
        self.actionJourney_InfoLoad = QtGui.QAction(MainWindow)
        self.actionJourney_InfoLoad.setObjectName(_fromUtf8("actionJourney_InfoLoad"))
        self.actionTicket_InfoLoad = QtGui.QAction(MainWindow)
        self.actionTicket_InfoLoad.setObjectName(_fromUtf8("actionTicket_InfoLoad"))
        self.actionDelay_InfoLoad = QtGui.QAction(MainWindow)
        self.actionDelay_InfoLoad.setObjectName(_fromUtf8("actionDelay_InfoLoad"))
        self.actionPassenger_InfoSave = QtGui.QAction(MainWindow)
        self.actionPassenger_InfoSave.setObjectName(_fromUtf8("actionPassenger_InfoSave"))
        self.actionJourney_InfoSave = QtGui.QAction(MainWindow)
        self.actionJourney_InfoSave.setObjectName(_fromUtf8("actionJourney_InfoSave"))
        self.actionTicket_InfoSave = QtGui.QAction(MainWindow)
        self.actionTicket_InfoSave.setObjectName(_fromUtf8("actionTicket_InfoSave"))
        self.actionDelay_InfoSave = QtGui.QAction(MainWindow)
        self.actionDelay_InfoSave.setObjectName(_fromUtf8("actionDelay_InfoSave"))
        self.menuLoad_Settings.addSeparator()
        self.menuLoad_Settings.addAction(self.actionPassenger_InfoLoad)
        self.menuLoad_Settings.addAction(self.actionJourney_InfoLoad)
        self.menuLoad_Settings.addAction(self.actionTicket_InfoLoad)
        self.menuLoad_Settings.addAction(self.actionDelay_InfoLoad)
        self.menuSave_Settings.addAction(self.actionPassenger_InfoSave)
        self.menuSave_Settings.addAction(self.actionJourney_InfoSave)
        self.menuSave_Settings.addAction(self.actionTicket_InfoSave)
        self.menuSave_Settings.addAction(self.actionDelay_InfoSave)
        self.menuFile.addAction(self.menuSave_Settings.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuLoad_Settings.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.mainTabWidget.setCurrentIndex(0)
        self.arrivingStationCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Delay Repay - 1.0.0", None))
        self.journeyInfoGroupBox.setTitle(_translate("MainWindow", "Journey Info", None))
        self.journeyDat_label.setText(_translate("MainWindow", "Journey Date", None))
        self.arrivingStationCombo.setItemText(1, _translate("MainWindow", "Merstham", None))
        self.arrivingStationCombo.setItemText(2, _translate("MainWindow", "London Victoria", None))
        self.arrivingStationCombo.setItemText(3, _translate("MainWindow", "London Bridge", None))
        self.arrivingStationCombo.setItemText(4, _translate("MainWindow", "East Croydon", None))
        self.departingStationLabel.setText(_translate("MainWindow", "Departing Station", None))
        self.departureTimeLabel.setText(_translate("MainWindow", "Departure Time", None))
        self.arrivingStation.setText(_translate("MainWindow", "Arriving Station", None))
        self.journeyDate_MonthCombo.setItemText(1, _translate("MainWindow", "Jan", None))
        self.journeyDate_MonthCombo.setItemText(2, _translate("MainWindow", "Feb", None))
        self.journeyDate_MonthCombo.setItemText(3, _translate("MainWindow", "Mar", None))
        self.journeyDate_MonthCombo.setItemText(4, _translate("MainWindow", "Apr", None))
        self.journeyDate_MonthCombo.setItemText(5, _translate("MainWindow", "May", None))
        self.journeyDate_MonthCombo.setItemText(6, _translate("MainWindow", "Jun", None))
        self.journeyDate_MonthCombo.setItemText(7, _translate("MainWindow", "Jul", None))
        self.journeyDate_MonthCombo.setItemText(8, _translate("MainWindow", "Aug", None))
        self.journeyDate_MonthCombo.setItemText(9, _translate("MainWindow", "Sept", None))
        self.journeyDate_MonthCombo.setItemText(10, _translate("MainWindow", "Oct", None))
        self.journeyDate_MonthCombo.setItemText(11, _translate("MainWindow", "Nov", None))
        self.journeyDate_MonthCombo.setItemText(12, _translate("MainWindow", "Dec", None))
        self.departingStationCombo.setItemText(1, _translate("MainWindow", "Merstham", None))
        self.departingStationCombo.setItemText(2, _translate("MainWindow", "London Victoria", None))
        self.departingStationCombo.setItemText(3, _translate("MainWindow", "London Bridge", None))
        self.departingStationCombo.setItemText(4, _translate("MainWindow", "East Croydon", None))
        self.arrivalTimeLabel.setText(_translate("MainWindow", "Arrival Time", None))
        self.TicketInfoGroupBox.setTitle(_translate("MainWindow", "Ticket Info", None))
        self.ticketTypeLabel.setText(_translate("MainWindow", "Ticket Type", None))
        self.firstNameLabel_2.setText(_translate("MainWindow", "Cost", None))
        self.validUntilLabel.setText(_translate("MainWindow", "Valid Until", None))
        self.validFromMonth_Combo.setItemText(1, _translate("MainWindow", "Jan", None))
        self.validFromMonth_Combo.setItemText(2, _translate("MainWindow", "Feb", None))
        self.validFromMonth_Combo.setItemText(3, _translate("MainWindow", "Mar", None))
        self.validFromMonth_Combo.setItemText(4, _translate("MainWindow", "Apr", None))
        self.validFromMonth_Combo.setItemText(5, _translate("MainWindow", "May", None))
        self.validFromMonth_Combo.setItemText(6, _translate("MainWindow", "Jun", None))
        self.validFromMonth_Combo.setItemText(7, _translate("MainWindow", "Jul", None))
        self.validFromMonth_Combo.setItemText(8, _translate("MainWindow", "Aug", None))
        self.validFromMonth_Combo.setItemText(9, _translate("MainWindow", "Sept", None))
        self.validFromMonth_Combo.setItemText(10, _translate("MainWindow", "Oct", None))
        self.validFromMonth_Combo.setItemText(11, _translate("MainWindow", "Nov", None))
        self.validFromMonth_Combo.setItemText(12, _translate("MainWindow", "Dec", None))
        self.validFromLabel.setText(_translate("MainWindow", "Valid From", None))
        self.validUntilMonth_Combo.setItemText(1, _translate("MainWindow", "Jan", None))
        self.validUntilMonth_Combo.setItemText(2, _translate("MainWindow", "Feb", None))
        self.validUntilMonth_Combo.setItemText(3, _translate("MainWindow", "Mar", None))
        self.validUntilMonth_Combo.setItemText(4, _translate("MainWindow", "Apr", None))
        self.validUntilMonth_Combo.setItemText(5, _translate("MainWindow", "May", None))
        self.validUntilMonth_Combo.setItemText(6, _translate("MainWindow", "Jun", None))
        self.validUntilMonth_Combo.setItemText(7, _translate("MainWindow", "Jul", None))
        self.validUntilMonth_Combo.setItemText(8, _translate("MainWindow", "Aug", None))
        self.validUntilMonth_Combo.setItemText(9, _translate("MainWindow", "Sept", None))
        self.validUntilMonth_Combo.setItemText(10, _translate("MainWindow", "Oct", None))
        self.validUntilMonth_Combo.setItemText(11, _translate("MainWindow", "Nov", None))
        self.validUntilMonth_Combo.setItemText(12, _translate("MainWindow", "Dec", None))
        self.ticketTypeCombo.setItemText(1, _translate("MainWindow", "monthly", None))
        self.ticketTypeCombo.setItemText(2, _translate("MainWindow", "yearly", None))
        self.photoBrowseButton.setText(_translate("MainWindow", "Browse Images", None))
        self.firstNameLabel_3.setText(_translate("MainWindow", "Photo Path", None))
        self.groupBox.setTitle(_translate("MainWindow", "Pasenger Info", None))
        self.photocardIdLabel.setText(_translate("MainWindow", "Photocard ID", None))
        self.firstNameLabel.setText(_translate("MainWindow", "First Name", None))
        self.cityLabel.setText(_translate("MainWindow", "City", None))
        self.address2Label.setText(_translate("MainWindow", "Address 2", None))
        self.surnameLabel.setText(_translate("MainWindow", "Surname", None))
        self.phoneLabel.setText(_translate("MainWindow", "Phone No.", None))
        self.titleLabel.setText(_translate("MainWindow", "Title", None))
        self.postCodeLabel.setText(_translate("MainWindow", "PostCode", None))
        self.titleComboBox.setItemText(1, _translate("MainWindow", "Mr", None))
        self.titleComboBox.setItemText(2, _translate("MainWindow", "Mrs", None))
        self.titleComboBox.setItemText(3, _translate("MainWindow", "Ms", None))
        self.titleComboBox.setItemText(4, _translate("MainWindow", "Miss", None))
        self.countyLabel.setText(_translate("MainWindow", "County", None))
        self.address1Label.setText(_translate("MainWindow", "Address 1", None))
        self.emailLabel.setText(_translate("MainWindow", "Email", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Delay Info", None))
        self.delayTypeLabel.setText(_translate("MainWindow", "Delay Length", None))
        self.delayReason_Label.setText(_translate("MainWindow", "Delay Reason", None))
        self.delayTypeCombo.setItemText(1, _translate("MainWindow", "30-59 mins", None))
        self.delayTypeCombo.setItemText(2, _translate("MainWindow", "60-119 mins", None))
        self.delayTypeCombo.setItemText(3, _translate("MainWindow", "120+ mins", None))
        self.delayReason_Combo.setItemText(1, _translate("MainWindow", "Delayed departure", None))
        self.delayReason_Combo.setItemText(2, _translate("MainWindow", "Delayed on route", None))
        self.delayReason_Combo.setItemText(3, _translate("MainWindow", "Train cancelled", None))
        self.delayReason_Combo.setItemText(4, _translate("MainWindow", "Missed connection", None))
        self.submitCLaimButton.setText(_translate("MainWindow", "Submit Claim", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.userTab), _translate("MainWindow", "Delay Repay Info", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuLoad_Settings.setTitle(_translate("MainWindow", "Load Settings", None))
        self.menuSave_Settings.setTitle(_translate("MainWindow", "Save Settings", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionPassenger_InfoLoad.setText(_translate("MainWindow", "Passanger Info", None))
        self.actionJourney_InfoLoad.setText(_translate("MainWindow", "Journey Info", None))
        self.actionTicket_InfoLoad.setText(_translate("MainWindow", "Ticket Info", None))
        self.actionDelay_InfoLoad.setText(_translate("MainWindow", "Delay Info", None))
        self.actionPassenger_InfoSave.setText(_translate("MainWindow", "Passenger Info", None))
        self.actionJourney_InfoSave.setText(_translate("MainWindow", "Journey Info", None))
        self.actionTicket_InfoSave.setText(_translate("MainWindow", "Ticket Info", None))
        self.actionDelay_InfoSave.setText(_translate("MainWindow", "Delay Info", None))

