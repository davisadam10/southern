__author__ = 'adam'


def get_browser():
    br = mechanize.Browser()
    url = 'http://www.southernrailway.com/your-journey/customer-services/delay-repay/delay-repay-form'
    br.open(url)
    return br


def complete_form( browser, user, journey, ticket):
    forms = []
    for form in browser.forms():
        forms.append(form)

    mainForm = forms[4]

    mainForm['title'] = [user.get_title(),]
    mainForm['forename'] = user.get_forename()
    mainForm['surname'] = user.get_surname()
    mainForm['email'] = user.get_email()
    mainForm['email_confirmation'] = user.get_email()
    mainForm['phone'] = str(user.get_phone_number())
    mainForm['address1'] = user.get_address1()
    mainForm['address2'] = user.get_address2()
    mainForm['city'] = user.get_city()
    mainForm['county'] = user.get_county()
    mainForm['postcode'] = user.get_county()

    mainForm['ticket_type_1'] = [ticket.get_ticket_type(),]

    pounds, pence = str(ticket.get_ticket_cost()).split('.')
    mainForm['cost_pounds_1'] = pounds
    mainForm['cost_pence_1'] = pence

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


def submit_form(browser):
    response = browser.submit()
    text = response.read()
    temp_file = open("/home/adam/temp.html", "w")
    temp_file.write(text)
    temp_file.close()
