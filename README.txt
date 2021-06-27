# actinium_public
                                         Documentation for  PROJECT  ACTINIUM:

Overview : Actinium featuring Jarvis and Friday, whatever the  user  wants to call it, is a UI that interacts with the user through voice and command lines. It  is a simple version of Google assistant. The origin of it's name comes from the famous character of MCU(Marvel Cinematic Universe) Iron Man's personal A.I. assistants Jarvis and Friday. Although movie contains a lot of exaggerations, it serves an inspiration for all developers nationwide and worldwide.

In this project of Jarvis X Friday I, Rohan Dey , a student of class XI of Lions Calcutta Greater Vidya Mandir, have tried to imitate and the idea of Jarvis in my own version through Python (Currently the world's number 1) programming language. The program does simple tasks in within your local terminal. What makes it interesting is that it interacts with the user through voice output, thus making the user feel more interested in it. However unlike the real google assistant it can not do just anything and everything that the user asks for. For an instance it is made to carry out simple tasks within your local terminal, as a result, it can perform only a few web related actions and no cloud based actions.


The build of ACTINIUM:
As told earlier it is a simple beginner implementation of Python programming language. However it uses some advanced open source modules of Python to a basic extent.
                                                            


                                                                MODULES USED  and  their DOMAINS:

1. pyttsx3 : Open source voice module of python that allows python to use the in-built voice API of Microsoft(Since I am on windows) called "SAPI5" in order to produce voice output from the terminal via internal or external audio output devices.
2. datetime : Used to generate current date and time and display that as per user input
3. os : Allows python to make changes , modify and interact with the system.
4. engnie : assists pyttsx3 module to produce voice output
5. webbrowser : For Web Browser related actions
6. wikipedia : for searching up major topics on the web
7. exceptions : to handle wikipedia related exceptions
8. random : To generated random numbers within a given range, used in several fields
8. pywhatkit : To send instant messages on whatsapp.


LOGIC : Since this program has been kept as simple as possible, so no advanced concepts like Machine Learning, Deep Learning, Data Science and Artificial intelligece have not been used at all. Any beginner with basic knowledge of python programming can read , modify or reproduce this code.

The main concept used in this program was the implementation of basic Object Oriented Programming. Each every different task that Jarvis performs have been separated into different modules, called functions in the language of programming.
These modules can not be executed until they are called. So a main has been created where a never ending loop is created that ends only if the user gives the  termination command , until then it keeps on taking input from the user for as long as the user wants it to.

FUNCTIONS IT CAN PERFORM: This program performs basic takes on your terminal which are as follows: 
1. Plays a song as per user request.
2. Plays a random song
3. Opens major websites like google, instagram, facebook, twitter and stack overflow.
4. Can change the voice of Jarvis from male to female or vice versa as per the request made by the user.
5. Stores user given data including name, age, gender and password.
6. Cyphers the user data when it is stored in a file so that it can not be decrypted just by anyone seeing it.
7. Destroys the file storing the user data so that it can not be seen or accessed by anyone else.
8. Asks for password from the user when he wants to view the user information and displays it only if the password matches.
9. Allows user to search up any topic on the Wikipedia.
10. Says aloud the date and time if asked for.
11. Can send an instant message to any number in your contact via whatsapp web.
12. Wishes the user according to the time like, good morning, good evening, etc.


COMMANDS FOR ACTINIUM :
Refer to command list to learn about and use all the commands of Jarvis.
SOURCE CODE:
You may find the source code in my git hub repository, it is free for public viewing and anyone may work with a clone of it , enhance it, modify it and do anything.
The git hub repository link goes here :
                                                    COMMAND LIST FOR ACTINIUM
*IMPORTANT REGULATIONS:
1. ps:( This means that the command allows the user to use prefixes or suffixes after the certain command phrase but must be separated by a space on both ends or else the commands will not be identified). For instance if you want to check the time, then, Tell me the date and time, which has already been defined as the particular command will have the same value as “Hey Jarvis please tell me the date and time” will have the same value. However commands which do not have ps written in braces with them will not have the same effect. The exact word/command needs to be entered to make them work.
2. Commands must be given carefully without spelling mistakes to avoid malfunctioning.
3. Termination command must be given exiting the program or else the user data resource might be leaked as the termination command destroys the user information that also includes the user password.
4. All commands separated by commas(,) have the same use / purpose.
5. Punctuation signs other than in-command punctuations are not allowed.
6. Case insensitive in case of commands but not in case of storing data or sending a whatsapp message.
COMMANDS for ACTINIUM : 
1.	What is the time(ps), what’s the time(ps),time now, time : all these commands serve the purpose of displaying the current time.
2.	Tell me the date and time(ps), date and time(ps): Displays the current date and time to the user.
3.	Change voice(ps), change your voice(ps) : Allows user to toggle between Jarvis and Friday(Male and Female voices).
4.	Wish me(ps), greet me(ps) : Wishes/ greets the user according to the current time
5.	Date : Displays current date.
6.	Send whatsapp message(ps) , send message(ps), text : allows user to send an instant whatsapp message to a selected contact.
7.	Open youtube/ facebook/instagram/stackoverflow/google/gmail/twitter(ps for all) : The open command along with any of these sites opens them up in your default browsers.
8.	Wikipedia(ps) , search up(ps) , search(ps) : These commands accompanied by the topic of search after them search up a topic(if it has an existence in wikipedia) and displays the topic summary to the user
9.	Play a song(ps) , Play music(ps), play song(ps) , play me a song(ps) : Plays a song selected by the user from his list of directory.
10.	Shuffle(ps): plays a random song from user’s music directory.
11.	Quit, Terminate Actinium, exit : Closes the program and destroys data to prevent resource leak.




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
