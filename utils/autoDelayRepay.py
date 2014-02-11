import mechanize
'''

title = "Mr"
firstName = "Adam"
secondName = "Davis"
email = "davisadam10@googlemail.com"
phoneNum = '07756134612'
address1 = "69 Albury Road"
address2 = "Merstham"
city = "Redhill"
county = "Surrey"
postcode = "RH1 3LP"
photocard_id = "MJD2214"

ticket_type_1 = "monthly"
cost = 285.70
day = 7
month = str(02).zfill(2)
year = 2014


departingStation = "Merstham"
arrivingStation = "London Victoria"
startTime = 08.22
arivingTime = 09.30

delay = "30-59 mins"
delayReason = "Train cancelled"



compensation = "National Rail Vouchers"





br = mechanize.Browser()
url = 'http://www.southernrailway.com/your-journey/customer-services/delay-repay/delay-repay-form'
br.open(url)

forms = []

for form in br.forms():
	forms.append(form)

timeForm = forms[1]

mainForm = forms[4]
br.form = list(br.forms())[4]

title = [title,]
mainForm['title'] = title
forename = firstName
mainForm['forename'] = firstName
surname = secondName
mainForm['surname'] = secondName
email = email
mainForm['email'] = email
email_confirmation = email
mainForm['email_confirmation'] = email
phone = str(phoneNum)
mainForm['phone'] = str(phoneNum)
address1 = address1
mainForm['address1'] = address1
address2 = address2
mainForm['address2'] = address2
city = city
mainForm['city'] = city
mainForm['county'] = county
mainForm['postcode'] = postcode

ticket_type_1 = [ticket_type_1,]
mainForm['ticket_type_1'] = ticket_type_1

cost_pounds_1 = str(cost).split('.')[0]
mainForm['cost_pounds_1'] = str(cost).split('.')[0]

cost_pence_1 = str(cost).split('.')[1]
mainForm['cost_pence_1'] = str(cost).split('.')[1]

journey_date_day_1 = [str(day),]
mainForm['journey_date_day_1'] = journey_date_day_1
journey_date_month_1 = [month,]
mainForm['journey_date_month_1'] = journey_date_month_1
journey_date_year_1 = [str(year),]
mainForm['journey_date_year_1'] = journey_date_year_1

scheduleddeparturehours_1 = [str(startTime).split('.')[0].zfill(2),]
mainForm['scheduleddeparturehours_1'] = scheduleddeparturehours_1
scheduleddeparturemins_1 = [str(startTime).split('.')[1].zfill(2),]
mainForm['scheduleddeparturemins_1'] = scheduleddeparturemins_1

scheduledarrivalhours_1 = [str(arivingTime).split('.')[0].zfill(2),]
mainForm['scheduledarrivalhours_1'] = scheduledarrivalhours_1

scheduledarrivalmins_1 = [str(arivingTime).split('.')[1].zfill(2),]
mainForm['scheduledarrivalmins_1'] = scheduledarrivalmins_1

departing_station_1 = departingStation
mainForm['departing_station_1'] = departing_station_1
arriving_station_1 = arrivingStation
mainForm['arriving_station_1'] = arriving_station_1

delayReason_1 = [delayReason,]
mainForm['delayReason_1'] = delayReason_1
delay_1 = [delay,]
mainForm['delay_1'] = delay_1

control = mainForm.find_control("uploadedfile_1")
control.add_file(open("/home/adam/railticketimages/feb_2014_ticket.jpeg"), 'text/plain', "/home/adam/railticketimages/feb_2014_ticket.jpeg")

compensation = [compensation,]
mainForm['compensation'] = compensation
photocard_id_1 = photocard_id
mainForm['photocard_id_1'] = photocard_id_1





response = br.submit()
text = response.read()
tempFile = open("/home/adam/temp.html", "w")
tempFile.write(text)
tempFile.close()

'''