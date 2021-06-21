import datetime
import os
import random
import webbrowser

import pyttsx3
import pywhatkit
import wikipedia as wiki
from pyttsx3 import engine
from wikipedia import exceptions

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
voice = engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",135)


#Base module to return a string output via speech a.k.a. Audio output
def speak(args):
    engine.say(args)
    engine.runAndWait()

#Function not yet created anyways it would be useful only for voice recog and stuff
def takecommand():
    pass

#Works as a complementary method with Init to toggle voices between Jarvis and Friday..provides toggle condition data to its complement
def Setvoice():
    speak("Do you want a  male voice or female voice for your program?")
    koe = input().lower()
    if koe == "female":
        return 1
    else:
        return 0

#Complementary method for Setvoice after receiving data from the other half it does the voice setting part
def Init():
    koe = Setvoice()
    speak("Setting up voice for your program")
    engine.setProperty("voice",voices[koe].id)
    speak("Here is a sample voice")
    speak("U can change my voice later by using change voice or change your voice command")
    if koe == 1:
        speak("Friday online")
    elif koe == 0:
        speak("Jarvis online")

def setspeed():
    speak("Enter the speech rate , minimum value can be 100 and maximum value is 150")
    speak("If a value is out of the range then it will be set to default speed of 135")
    speed =int(input())
    if speed >= 100 and speed<=150:
        engine.setProperty('rate',speed)
        speak("Speech has been set to your given rate.")
    else:
        engine.setProperty('rate',135)
        speak("Sorry value out of bounds.")

def cypher(args):
    w = ""
    for i in args:
        w = i + w
    return w

#Random blabbering to make Jarvis sound cool
def starting_Actinium():
    speak("Starting the Actinium Program...all functions are being initialized")
    speak("Initialization of all internal elements have started , proceeding to user data collection")
    
#Takes and stores userdata in the form of a .txt aka text file and provides it when asked
def userdata():
    speak("New user authentication is now Beginning, please cooperate and provide the details as requested")
    speak("Enter your name")
    username = input()
    speak("Set a password")
    temp = input()
    password = cypher(temp)
    speak("Enter your age")
    userage = input()
    speak("Enter your gender as  either male ,  female or other if any other input is received the gender will be set as private")
    usersex = input().lower()
    if usersex == "male" or usersex == "female" or usersex == "other" or usersex == "others":
        pass
    else:
        usersex = "not set by user"
    return username,userage,usersex,password
#Complementary function for user userdata...used to store user details in a file
def userinfo():
    userdetails = userdata()
    userinfo.name = userdetails[0]
    userinfo.age = userdetails[1]
    userinfo.gender = userdetails[2]
    userinfo.password = userdetails[3]
    with open ("datafile","w") as df:
        df.write(userdetails[0]+"\n"+userdetails[1]+"\n"+userdetails[2]+"\n"+userdetails[3])
        df.close()
    speak("Your username password age and gender has benn set sucessfully. User Authentication complete")

#Displays the info of the current user whenever asked only if the correct password is entereed
def display_User_info():
    with open("datafile","r") as df:
        lines = df.readlines()
        pd = lines[3]
        pd = cypher(pd)
        speak("Enter password")
        q = input()
        if pd == q:
            speak("Password matched , user has been authenticated")
            speak("User info are as follows")
            speak("username is "+lines[0])
            speak("age of user is"+lines[1]+"Years")
            speak("gender is"+lines[2])
        else:
            speak("User could not be authenticated , sorry user information thereby can not be displayed")

#If command has been given to terminate Jarvis or Friday it automatically destroys the user info including password so that it can not be acessed by anyone else.
def terminator():
    os.remove("datafile")
    os.remove("pywhatkit_dbs.txt")
    speak("Termination complete")
    speak("Shutting down in 3, 2, 1")

#searches a topic in wikipedia as per user request.
def wikipedia(query):
   try: 
    speak("Searching wikipedia as per your request")
    query = query.replace("wikipedia","")
    results = wiki.summary(query,sentences = 3)
    speak("According to wikipedia")
    speak(results)
   except exceptions as e:
       print(e)
       speak("Uhh sorry, this topic is not available in wikipedia. Make sure you have given correct data.")


#Function to speak the time
def time():
    now = datetime.datetime.now()
    hour =int(now.strftime("%H"))
    if hour>12:
        hour = hour - 12
        str = "The time is ",hour,now.strftime("%M")+"PM"
        speak(str)
    else:
        str = "The time is ",hour,now.strftime("%M")+"AM"
        speak(str)
    
#Function to speak both dateand time
def datentime():
    time()

def wishme():#Function to wish user according to current time 
    hour = int(datetime.datetime.now().hour) #Taking the current hour(0-23)
    if hour>=0 and hour<12:
        speak("Good morning, have a nice day")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    elif hour>= 18 and hour<21:
        speak("Good Evening , maybe you wanna get some coffee")
    else: speak("Good Night , it's pretty late.")

#Function to play a random song from the music directory of your local terminal
def playrandom():
     music ="D:\\Jarvis gamma\\Music directory"
     n = 0
     songs = os.listdir(music)
     n = random.randint(0,(len(songs)-1))
     speak("playing"+songs[n])
     print("playing"+songs[n])
     os.startfile(os.path.join(music,songs[n]))

#Plays a particular song as per user request from local music directory
def playParticular():
     speak("Presenting your list of musics from your directory. Select the serial number of the music to choose it as your music of choice")
     music = "D:\\Jarvis gamma\\Music directory"
     songs = os.listdir(music)
     speak("The musics present in your directory are")
     for i in range(len(songs)):
        print(i+1,songs[i])
     n = int(input())
     k = n - 1
     speak("Playing song as per request . It has been set to "+songs[k])
     os.startfile(os.path.join(music, songs[k]))

def whatsapp():
    speak("enter phone number with a plus sign and country code in the beginning")
    num = input()
    speak("Enter the content that you want to send")
    content = input()
    pywhatkit.sendwhatmsg_instantly(num,content)



if __name__ == "__main__":
#All logics and condition based work will happen here
    starting_Actinium()
    Init()
    userinfo()
    wishme()
    while 1:
       speak("Awaiting user command")
       query = input().lower()
      #  if "what is the date" in query or "what's the date in query" or query == "today's date" or query == "date":
      #     dat()
       if "what is the time" in query or "what's the time" in query or query == "time now" or query =="time":
           time()
       if "tell me the date and time" in query or "date and time" in query:
           datentime()
       if "change voice" in query or "change your voice" in query:
           Init()
       if  "wish me" in query or "greet me" in query:
           wishme()
       if "send whatsapp message" in query or query == "text" or  "send message" in query :
           whatsapp()
       if "open facebook" in query:
           speak("Openning facebook")
           webbrowser.open('http://www.facebook.com')
       if "open google" in query:
           speak("Openning Google")
           webbrowser.open('http://www.google.com')
       if "open instagram" in query:
           speak("Openning Instagram")
           webbrowser.open("http://www.instagram.com")
       if "open stackoverflow" in query:
           speak("Openning Stack Overflow")
           webbrowser.open("http://stackoverflow.com")
       if "open twitter" in query:
           speak("Openning Twitter")
           webbrowser.open("http://www.twitter.com")
       if "open youtube" in query:
           speak("Opening youtube")
           webbrowser.open("http://www.youtube.com")
       if "send mail" in query or "send a mail" in query or "open gmail" in query:
           speak("Opening gmail")
           webbrowser.open("http://www.gmail.com")      
       if "wikipedia" in query or "search up" in query or "search" in query:
           wikipedia(query)
       if "play a song" in query or "play music" in query or "play song" in query or "play song" in query or "play me a song"in query:
           playParticular()
       if "shuffle" in query:
           playrandom()
       if "display my data" in query or "display user information" in query or "display info" in query or "display user info" in query or "display user data" in query:
           display_User_info()
       if "change speed" in query or "change your speed" in query or "change speech rate" in query:
           setspeed() 
      # if "date" == query:
       #    dat() 
       if "quit" == query or "terminate actinium" == query:
           terminator()
           break
