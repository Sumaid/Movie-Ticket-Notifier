    #!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import subprocess
import time
import requests
from bs4 import BeautifulSoup
import smtplib
from gi.repository import Notify
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Gmail account", "Pass word")
msg = MIMEText("""Dear reciever,
  If you're reading this then it means Infinity war tickets are out!!!!!This is an automated mail...I sent this on 24th April 1:30 pm...If I'm still alive contact me somehow and make me book tickets and if I'm not alive then you book tickets and enjoy<3....Fast! You don't have much time.............
  Yours sincerely,
  name(of past)""")
sender = ""
recipients = ['']
msg['Subject'] = "Infinity War Tickets out....Tell Me"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
count = 0

while (count!=1):
  res = requests.get('https://in.bookmyshow.com/buytickets/avengers-infinity-war-hyderabad/movie-hyd-ET00053419-MT/20180427')
  print(res.status_code)

  text_data = res.text
  soup = BeautifulSoup(text_data)

  #dude = soup.select('a')
  dude = soup.find_all( attrs={"data-name" : "Prasads: Large Screen"} )
  count = len(dude)  
  if len(dude)==1:
      print("Book your ticket! Book your ticket!")
      Notify.init("start")
      notification = Notify.Notification.new("Book your ticket, Book your ticket!")
      notification.set_app_name("BvsS")
      notification.show()
      s.sendmail(sender, recipients, msg.as_string())
      subprocess.call(['play', 'siren2.wav'])
      break
  time.sleep(1)
