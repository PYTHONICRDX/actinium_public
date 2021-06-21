import pyttsx3
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
voice = engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",135)


#Base module to return a string output via speech a.k.a. Audio output
def speak(args):
    engine.say(args)
    engine.runAndWait()

def whatsapp():
    speak("enter phone number with a plus sign and country code in the beginning")
    num = input()
    speak("Enter the content that you want to send")
    content = input()
    pywhatkit.sendwhatmsg_instantly(num,content)

whatsapp()