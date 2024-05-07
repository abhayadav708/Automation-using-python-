import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getproperty('voices')
engine.setproperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning yadav ji")
    elif hour >=12 and hour < 18:
        speak("good afternoon yadav ji")
    else:
        speak("good evening yadav ji")
    speak("let me know how can i help you , what are you looking for ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening to you Abhay....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your voice .....")
        query = r.Recognize_google(audio, language='en-in')
        print(f"My dear friend you said : {query}\n")

    except Exception as e:
        print("abahy say that again please .....")
        return "None"

    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('desiboysonfire101@gmail.com','Abhay70844@')
    server.sendmail('desboysonfire101@gmail.com', to , content)
    server.close()



if __name__ == '__main__':
    wishme()

    while true:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipidia","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(result)
            speak(result)

        if 'open notepad' in query:
            npath = "C:\\Window\\system64\\notepad.exe"
            os.startfile(npath)

        elif 'open paint' in query:
            npath = "C:\\Window\\system64\\mspaint.exe"
            os.startfile(npath)

        elif 'open youtube' in webbrowser:
            webbrowser.open('youtube.com')

        elif 'open makaut ' in query:
            webbrowser.open("https://makaut1.ucanapply.com/smartexam/public/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "tell me the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("my dear friend the time is {strTime}")

        elif 'open tere bin song on youtube' in query:
            webbrowser.open("https://youtu.be/gMJFzXZ103Y")
        elif 'open linkedln' in query:
            webbrowser.open("www.linkedln.com")

        elif 'email to other friend' in query:
            try:
                speak("what should I send ?")
                content = takecommand()
                to = "pritam1392003@gmail.com"
                sendEmail(to,content)
                speak("your email has been send successfully")
        

            except Exception as e:
                print(e)
                speak("my dear friend ... I am unable to send the email ....")





        

        

        










