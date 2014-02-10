__author__ = 'adam'
import mechanize
import pickle

def load_setting(file_path):
    tmp_file = open(file_path, 'r')
    settings = pickle.load(tmp_file)
    tmp_file.close()
    return settings



def get_browser():
    br = mechanize.Browser()
    url = 'http://www.southernrailway.com/your-journey/customer-services/delay-repay/delay-repay-form'
    br.open(url)
    return br


def complete_form( browser, user, journey, ticket, delay):
    forms = []
    for form in browser.forms():
        forms.append(form)

    main_form = forms[4]

    main_form['title'] = [user.get_title(), ]
    main_form['forename'] = user.get_forename()
    main_form['surname'] = user.get_surname()
    main_form['email'] = user.get_email()
    main_form['email_confirmation'] = user.get_email()
    main_form['phone'] = str(user.get_phone_number())
    main_form['address1'] = user.get_address1()
    main_form['address2'] = user.get_address2()
    main_form['city'] = user.get_city()
    main_form['county'] = user.get_county()
    main_form['postcode'] = user.get_county()

    main_form['ticket_type_1'] = [ticket.get_ticket_type(), ]

    pounds, pence = str(ticket.get_ticket_cost()).split('.')
    main_form['cost_pounds_1'] = pounds
    main_form['cost_pence_1'] = pence

    main_form['journey_date_day_1'] = [str(journey.get_day()), ]
    main_form['journey_date_month_1'] = [journey.get_month(), ]
    main_form['journey_date_year_1'] = [str(journey.get_year()), ]

    main_form['scheduleddeparturehours_1'] = [str(journey.get_start_time_hour()).zfill(2), ]
    main_form['scheduleddeparturemins_1'] = [str(journey.get_start_time_min()).zfill(2), ]

    main_form['scheduledarrivalhours_1'] = [str(journey.get_end_time_hour()).zfill(2), ]
    main_form['scheduledarrivalmins_1'] = [str(journey.get_end_time_min()).zfill(2), ]

    main_form['departing_station_1'] = journey.get_depart_station()
    main_form['arriving_station_1'] = journey.get_arriving_station()

    main_form['delayReason_1'] = [delay.get_delay_reason(), ]
    main_form['delay_1'] = [delay.get_delay_type(), ]

    control = main_form.find_control("uploadedfile_1")
    control.add_file(open(ticket.get_ticket_photo_path()), 'text/plain', ticket.get_ticket_photo_path())

    compensation = "National Rail Vouchers"
    main_form['compensation'] = [compensation, ]
    main_form['photocard_id_1'] = user.get_photocard_id()


def submit_form(browser, debug=True):
    if not debug:
        response = browser.submit()
        text = response.read()
        temp_file = open("/home/adam/temp.html", "w")
        temp_file.write(text)
        temp_file.close()
