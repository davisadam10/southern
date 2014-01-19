import mechanize

title = "Mr"
firstName = "Adam"
secondName = "Davis"
email = "davisadam10@googlemail.com"
phoneNum = 07756134612
address1 = "69 Albury Road"
address2 = "Merstham"
city = "Redhill"
county = "Surrey"
postcode = "RH1 3LP"
ticket_type_1 = "monthly"
cost = 285.70
day = 13
month = str(01).zfill(2)
year = 2014

startTime = 19.10
arivingTime = 19.53

delay = "60-119 mins"
delayReason = "Delayed departure"

arrivingStation = "Merstham"
departingStation = "London Victoria"

compensation = "National Rail Vouchers"

photocard_id = "MJD2214"



br = mechanize.Browser()
url = 'http://www.southernrailway.com/your-journey/customer-services/delay-repay/delay-repay-form'
br.open(url)

forms = []

for form in br.forms():
	forms.append(form)

timeForm = forms[1]

mainForm = forms[4]
br.form = list(br.forms())[4]

mainForm['title'] = [title,]
mainForm['forename'] = firstName
mainForm['surname'] = secondName
mainForm['email'] = email
mainForm['email_confirmation'] = email
mainForm['phone'] = str(phoneNum)
mainForm['address1'] = address1
mainForm['address2'] = address2
mainForm['city'] = city
mainForm['county'] = county
mainForm['postcode'] = postcode
mainForm['ticket_type_1'] = [ticket_type_1,]
mainForm['cost_pounds_1'] = str(cost).split('.')[0]
mainForm['cost_pence_1'] = str(cost).split('.')[1]

mainForm['journey_date_day_1'] = [str(day),]
mainForm['journey_date_month_1'] = [month,]
mainForm['journey_date_year_1'] = [str(year),]

mainForm['scheduleddeparturehours_1'] = [str(startTime).split('.')[0].zfill(2),]
mainForm['scheduleddeparturemins_1'] = [str(startTime).split('.')[1].zfill(2),]

mainForm['scheduledarrivalhours_1'] = [str(arivingTime).split('.')[0].zfill(2),]
mainForm['scheduledarrivalmins_1'] = [str(arivingTime).split('.')[1].zfill(2),]

mainForm['departing_station_1'] = departingStation
mainForm['arriving_station_1'] = arrivingStation

mainForm['delayReason_1'] = [delayReason,]
mainForm['delay_1'] = [delay,]

control = mainForm.find_control("uploadedfile_1")
control.add_file(open("/home/adam/image.jpeg"), 'text/plain', "/home/adam/image.jpeg")

mainForm['compensation'] = [compensation,]
mainForm['photocard_id_1'] = photocard_id




response = br.submit()
text = response.read()
tempFile = open("/home/adam/temp.html", "w")
tempFile.write(text)
tempFile.close()
