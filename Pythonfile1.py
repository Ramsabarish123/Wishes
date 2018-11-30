import os
import mysql.connector
import smtplib
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import random

mydb = mysql.connector.connect(host="mysql",user="root",passwd="",port="3306")
mycursor = mydb.cursor() 
mycursor.execute("CREATE DATABASE ram12345")
mycursor.execute("CREATE TABLE ram12345.Employees (id INTEGER, name VARCHAR(255), gmail VARCHAR(255), birthdate DATE)")

sql = "INSERT INTO ram12345.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
val = ("1", "sabarish", "kramsabarish1234@gmail.com", "2018-11-30")
mycursor.execute(sql, val)

#sql1 = "INSERT INTO ram12345.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val1 = ("2", "ram", "kramsabarish1234@gmail.com", "2018-11-2")
#mycursor.execute(sql1, val1)

#sql2 = "INSERT INTO ram12345.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val2 = ("3", "Madhu", "vmadhu435@gmail.com", "2018-11-2")
#mycursor.execute(sql2, val2)

#sql3 = "INSERT INTO ram12345.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val3 = ("4", "Rohini", "rohini10waghmare@gmail.com", "2018-11-29")   #--10/01/1996
#mycursor.execute(sql3, val3)

#sql4 = "INSERT INTO ram12345.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val4 = ("5", "Rohini", "vanaparthy1312@gmail.com", "2018-11-29")     #---17/06/1997
#mycursor.execute(sql4, val4)


mydb.commit()
mycursor.execute("SELECT * FROM ram12345.Employees")
myresult = mycursor.fetchall()
print("hello dude")
today = datetime.date.today()



fromaddr = "kramsabarish1234@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Subject'] = "Happy Birthday"

wishes_list=['Wishing you the most joyous Bday!. May this and every day of the year be special, magical and unforgettable!',
			  'Let yourself do everything that you like most in life, may your Big Day be cheerful and happy!',
			  'May the angels watch over you and bring you peace on your special day and every day',
			  'Congratulations on your bday! Wishing you joy, success and happiness in life! Hoping you make the most of your big day today!']
body = random.choice(wishes_list)
msg.attach(MIMEText(body, 'plain'))
image_list = ['HappyBirthday.jpg', 'HappieBirthday.jpg', 'HapyBirthday.jpg', 'BirthdayWishes.jpg', 'BirthdayWish.jpg','Wishes.jpg','wish.jpg','happyWishes.jpg']

filename = random.choice(image_list)
attachment = open("./"+filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(part)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(fromaddr, "Sudharani@123")

for x in myresult:
	if(x[3]==today):
		msg['To'] = x[2]
		text = msg.as_string()
		server.sendmail(fromaddr,x[2], text)
		print(x[3])
server.quit()



