import pyttsx3
import speech_recognition as sr
import datetime
import  wikipedia
import webbrowser
import os
import smtplib
# sapi5 use to excess voices
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()    #Without this command- speech will not be audible to us
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour >=12 and hour <18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Anna. Mam please tell me how may I help you")
def takeCommand():
    #It takes microphone input from user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        #print(e)
        speak("Can you please say that again?")
        return "None"
    return query
'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('charmeegandhi0@gmail.com', 'uour password')
    server.sendmail('charmeegandhi0@gmail.com', to, content)
    server.close()
 '''
if __name__ == "__main__":
    #speak("Charmee is a good girl")
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'play music' in query:
            music_dir= "C:\\Users\\Charmee Gandhi\\Music\\favourite_songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
        elif 'open SQL' in query:
            codePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\MySQL\\MySQL Workbench 8.0 CE.lnk"
            os.startfile(codePath)
        elif 'open calendar' in query:
            webbrowser.open("https://www.timeanddate.com/calendar/")
        elif 'open pycharm' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2021.2.2.lnk"
            os.startfile(codePath)
        '''elif 'email to Charmee' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "charmeecharmeegandhi0@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry dear Charmee. I am not able to send this email")'''
        if 'stop' in query:
            exit()

