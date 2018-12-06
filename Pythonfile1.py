import os,mysql.connector,smtplib,datetime,random
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


mydb = mysql.connector.connect(host="mysql",user="root",passwd="",port="3306")
mycursor = mydb.cursor() 
mycursor.execute("CREATE DATABASE Birthday")
mycursor.execute("CREATE TABLE Birthday.Employees (id INTEGER, name VARCHAR(255), gmail VARCHAR(255), birthdate VARCHAR(10))")

sql = "INSERT INTO Birthday.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
val = ("1", "sabarish", "kramsabarish1234@gmail.com", "6/12")
mycursor.execute(sql, val)



#sql2 = "INSERT INTO Birthday.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val2 = ("3", "Madhu", "vmadhu435@gmail.com", "2018-11-2")
#mycursor.execute(sql2, val2)

#sql3 = "INSERT INTO Birthday.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val3 = ("4", "Rohini", "rohini10waghmare@gmail.com", "10/1")   #--10/01/1996
#mycursor.execute(sql3, val3)

#sql4 = "INSERT INTO Birthday.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val4 = ("5", "Rohini", "vanaparthy1312@gmail.com", "17/6")     #---17/06/1997
#mycursor.execute(sql4, val4)

#sql4 = "INSERT INTO Birthday.Employees (id, name, gmail, birthdate) VALUES (%s, %s, %s, %s)"
#val4 = ("5", "Rohini", "rangaashaaa@gmail.com", "6/11")     #---17/06/1997
#mycursor.execute(sql4, val4)



mydb.commit()
mycursor.execute("SELECT * FROM Birthday.Employees")
myresult = mycursor.fetchall()
print("hello dude")
print(myresult)
today = datetime.datetime.now()

print(today)

fromaddr = "kramsabarish1234@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Subject'] = "Happy Birthday"

wishes_list=['Wishing you the most joyous Bday!. May this and every day of the year be special, magical and unforgettable!',
			  'Let yourself do everything that you like most in life, may your Big Day be cheerful and happy!',
			  'May the angels watch over you and bring you peace on your special day and every day',
			  'Congratulations on your bday! Wishing you joy, success and happiness in life! Hoping you make the most of your big day today!']
body = random.choice(wishes_list)

print(body)

msg.attach(MIMEText(body, 'plain'))
image_list = ['HappyBirthday.jpg', 'HappieBirthday.jpg', 'HapyBirthday.jpg', 'BirthdayWishes.jpg', 'BirthdayWish.jpg','Wishes.jpg','wish.jpg','happyWishes.jpg']

filename = random.choice(image_list)

print(filename)

attachment = open("./"+filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(part)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(fromaddr, "Sudharani@123")

formatdate=str(today.day)+"/"+str(today.month)
print(formatdate)

for x in myresult:
	print(x[3])
	if(x[3]==formatdate):
		msg['To'] = x[2]
		server.sendmail(fromaddr,x[2], msg.as_string())
		print(x[3])
server.quit()



