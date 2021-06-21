import pyttsx3
import datetime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
voice = engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",135)


#Base module to return a string output via speech a.k.a. Audio output
def speak(args):
    engine.say(args)
    engine.runAndWait()

def func():
    month =int(now.strftime("%m"))
    ml = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    m = (ml[month-1])
    str = now.strftime(f" The date is %dth of {m}%Y")
    speak(str)

def func2():
    h = 0
    hour =int(now.strftime("%H"))
    suffix =""
    if hour>12:
        hour = hour - 12
        str = "The time is ",hour,now.strftime("%M")+"PM"
        speak(str)
    else:
        str = "The time is ",hour,now.strftime("%M")+"AM"
        speak(str)
now = datetime.datetime.now()
print ("Current date and time : ")
str = now.strftime("%d-%m-%Y")
print (now.strftime("%d-%m-%Y"))

func2()