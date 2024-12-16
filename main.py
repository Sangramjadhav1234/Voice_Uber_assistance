"""
Author:- Sangram
Discription:- This code is written for project on Uber Simulation with voice Assistance
Date:- Jan 23, 2024
"""

import sys
import random
from text_to_speech import save
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email_send_passwd

title = ' === Welcome To Uber === '
print (title.center(50,'*'))
save("welcome to uber")

save("input your details for proceed further")
try:
    class User :
        # class attributes -
        user_name : str = ""
        user_mobile_no : str = ""
        user_email : str = ""

        def __init__(self, name:str, mob_no:str, email:str):
            # instance attributes -
            self.user_name = name
            self.user_mobile_no = mob_no
            self.user_email = email
        
        def showUserDetails(self):
            # Details -
            print(f"Name of User = {self.user_name}\n\
            Contact No of user = {self.user_mobile_no}\n\
            Email ID of user = {self.user_email}\n")

    # taking user input -
    name = input("Enter your name = ")
    mob_no = input("Enter your mobile no. = ")
    email = input("Enter your email address = ")

    # object create user -
    user = User(name,mob_no,email)      # instantiating object
    user.showUserDetails()              # invoke the details
    print("-"*40)

    save(f"ok {name}, these are available rotes please select your route ")

    routes = {'deccan-karvenagar':'4.2','deccan-swargate':'4.4','deccan-hadpsar':'8.7',
                'deccan-nda':'7.5','swargate-katraj':'4.5','deccan-shivajinagar':'4'}

    print("*** Available Routes ***")
    list_routes = routes.keys()
    for r in list_routes:
        print(r)
        
    print("-"*40)

    save("please enter your source and destination to proceed further")

    source = input ("Enter your pick up point = ")
    source = source.lower()
    destination = input ("Enter your dropping point = ")
    destination = destination.lower()

    route_to_find = source + "-" + destination

    print('-'*40)

    if route_to_find in routes.keys():
        print(f"*** entered source {source}-{destination} = {routes[route_to_find]} kms ***\n")
        print('-'*40)
        save(f"selected route is {source}-{destination} = {routes[route_to_find]} kilometer ")
    else:
        print('-'*40)
        print(f"entered route {source}-{destination} is not available in routes list.....plz try it with available routes.")
        print('-'*40)
        save(f"entered route {source}-{destination} is not available....try with available routes")
        sys.exit()

    save("Do you want to proceed further")
    choice = input('"Do you want to proceed further" [Yes/No] : ')
    print('-'*40)

    while choice.casefold()=='yes':
        txt = (' Select Your Ride ')
        print(txt.center(50,'*'))
        save("select your ride from available options")

        class Ride :
            def __init__(self,type,capacity,bags,rate):
                self.type = type
                self.capacity = capacity
                self.bags = bags
                self.rate = rate

            def ShowRide(self):
                print(f"You are selected {self.type}\n\
                It's passenger carrying capacity is {self.capacity}\n\
                It Has luggage carrying capacity is upto {self.bags}\n\
                Charges per kilometer will be {self.rate}")
        
        # Polymorpism 
        class UberPrime(Ride):
            def __init__(self, type, capacity, bags, rate):
                super().__init__(type, capacity, bags, rate)

        class Uber(Ride):
            def __init__(self, type, capacity, bags, rate):
                super().__init__(type, capacity, bags, rate)

        class Auto(Ride):
            def __init__(self, type, capacity, bags, rate):
                super().__init__(type, capacity, bags, rate)
        
        class Bike(Ride):
            def __init__(self, type, capacity, bags, rate):
                super().__init__(type, capacity, bags, rate)

        # creating objects -
        uberPr = UberPrime('UBER PRIME','5','4','30 Rs.')  # instantiating object
        uberPr.ShowRide()                                  # invoke details

        uber = Uber('UBER','4','3','25 Rs.')
        uber.ShowRide()

        auto = Auto('AUTO','3','2','15 Rs.')
        auto.ShowRide()

        bike = Bike('BIKE','1','1','10 Rs')
        bike.ShowRide()

        print('-'*40)
        sel_ride = input('Enter selected ride:')
        sel_ride = sel_ride.upper()


        rate = { 'UBER PRIME': 30,'UBER': 25,'AUTO': 15,'BIKE': 10 }

        if sel_ride in rate.keys():
            base_amt = float(routes[route_to_find]) * float(rate[sel_ride])
            print(f'Base fare for ride will be Rs. {base_amt} INR')
            print('-'*40)
            save(f"Base fare for ride will be {int(base_amt)} INR")
            save("Do you want to book ride with us")
            chc = input('Do you want to book ride with us? [Yes/No] : ')
            print('-'*40)

            while chc.casefold() == 'yes':
                alpha= ['MY','AS','RN','GH']
                i= random.randint(0,3)
                state = (alpha[i])
                time = random.randint(10,40)
                veh_num = 'MH12 ' + state + ' ' + str(random.randint(0000,9999))
                print(f'Ride booked successfully!!!\n\
                Vehicle Type = {sel_ride}\n\
                Vehicle Number = {veh_num}\n\
                time to reach = {time} mins')

                cgst = base_amt * 0.09
                sgst = base_amt * 0.09
                total_fare = base_amt + cgst + sgst
                print('-'*40)
                txt_2=( '*** BILL OF RIDE ***')
                print(txt_2)
                print(f"total fare for ride will be Rs. {total_fare} INR")
                save(f"total fare for ride will be {int(total_fare)} INR")

                data = (('Customer','fare'),(name , str(base_amt) ),(mob_no, str(cgst )),(email ,str(sgst)),
                        ('total__amt',str(total_fare)))
                
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Times", size=10)
                line_height = pdf.font_size * 3
                col_width = pdf.epw /5
                for row in data:
                    for datum in row:
                        pdf.multi_cell(col_width, line_height, datum, border=1,
                                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
                    pdf.ln(line_height)
                pdf.output('uber.pdf')

                fromaddr = email_send_passwd.mail
                toaddr = email
                msg = MIMEMultipart() 
                msg['From'] = fromaddr 
                msg['To'] = toaddr
                msg['Subject'] = "Regarding bill for the ride"
                body = "Body_of_the_mail"
                msg.attach(MIMEText(body, 'plain'))
                filename = "uber.pdf"
                attachment = open("C:/Users/hp/Desktop/python/python_cw/uber.pdf", "rb")

                # instance of MIMEBase and named as p
                p = MIMEBase('application', 'octet-stream')

                # To change the payload into encoded form
                p.set_payload((attachment).read()) 
                encoders.encode_base64(p)   
                p.add_header('Content-Disposition', "attachment; filename= %s" %filename)
                msg.attach(p)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                mail_id = email_send_passwd.mail
                pwd =  email_send_passwd.password
                s.login(mail_id,pwd) 
                text = msg.as_string()
                s.sendmail(mail_id, email, text)
                s.quit()
                print(f"Ride booked successfully.total bill of ride including cgst and sgst will be {int(total_fare)}")
                save(f"Ride booked successfully.total bill of ride including cgst and sgst will be {int(total_fare)} \n \
                copy of the bill is sent to your registerd email ....driver will arrive shortly \n \
                THANK YOU for choosing Your ride with UBER")
                break

            while chc.casefold() == 'No':
                print("Try available routes")
                save("entered details are not correct.... please check details once ..")
            print('Exit from uber')
            save('EXIT')
            break

except Exception as ex:
    print(f"Error Occured = {ex}")
    