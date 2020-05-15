import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os
import smtplib
import calendar
import quickstart
import subprocess
import pyautogui
import sqlite3
import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 

s=1


#for voice in voices: 
    # to get the info. about various voices in our PC  


converter = pyttsx3.init('sapi5') 
voices = converter.getProperty('voices') 
voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
converter.setProperty('voice', voice_id) 
converter.runAndWait() 
#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[0].id)


def speak(text):
    converter.say (text)
    converter.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 6:
        speak("Good Afternnon" + MASTER)

    else:
         speak("Good Evening" + MASTER)

    speak("I am RAN... How may I help you?")

def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"User said : {query}\n")

        except Exception as e:
            print("Say that again ,Please.")
            query = None

        return query

def reminder():
        speak("What shall I remind you about?")
        reminder = takeCommand()
        speak("In how many minutes?")
        local_time = int(takeCommand())
        local_time = local_time * 60
        time.sleep(local_time)
        speak(reminder)
    
speak("Initializing RAN...")
speak("Hello.... I'm RAN. Whats your name?")
MASTER = takeCommand()
wishMe()
query = takeCommand()

while(s==1):
    if "wikipedia" in query.lower():
        speak("Searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif "reminder" in query.lower():
        reminder()

    elif "open youtube" in query.lower():
        webbrowser.open("youtube.com")
        #url = "youtube.com"
        #chrome_path ='C:\\Users\ADITI SAWANT\\AppData\Local\\Google\\Chrome\\Application\\chrome.exe %s'
        #webbrowser.get(chrome_path).open(url)

    elif "open google" in query.lower():
        webbrowser.open("google.com")

    elif "play music" in query.lower():
        music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif "email" in query.lower():
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("aditisawant.test@gmail.com", "aditi1910")
            speak("What do I send? Please give the message")
            message = takeCommand()
            s.sendmail("aditisawant.test@gmail.com", "sawant.aditi18@siesgst.ac.in",message)
            print("Mail has been sent")
            s.quit()
        except Exception as e:
            print(e)

    elif "calendar" in query.lower():
        c = calendar.TextCalendar(calendar.SUNDAY)
        speak("Which year?")
        yyyy = int(takeCommand())
        speak("Which month in number")
        mm = int(takeCommand())
        st = c.formatmonth(yyyy, mm, 0, 0)
        print(st)

    elif "date" in query.lower():
        current_date = datetime.date.today()
        speak(current_date)

    elif "classroom" in query.lower():
        speak("Which class?")
        a = takeCommand()
        if "python" in a.lower():
                webbrowser.open("https://classroom.google.com/u/0/c/NTAwMTM4MTQzMDRa")
        elif "unix" in a.lower():
                webbrowser.open("https://classroom.google.com/u/0/c/NDg3NTIwMzgzOTBa")
               


    elif "event" in query.lower():
        subprocess.Popen("python quickstart.py", shell=True)

    elif "screenshot" in query.lower():
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

    elif "corona" in query.lower():
        extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
        URL = 'https://www.mohfw.gov.in/'

        SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed', 
                        'Foreign-Confirmed','Cured','Death'] 

        response = requests.get(URL).content 
        soup = BeautifulSoup(response, 'html.parser') 
        header = extract_contents(soup.tr.find_all('th')) 

        stats = [] 
        all_rows = soup.find_all('tr') 

        for row in all_rows: 
            stat = extract_contents(row.find_all('td')) 
            if stat: 
                if len(stat) == 5: 
                    # last row 
                    stat = ['', *stat] 
                    stats.append(stat) 
                elif len(stat) == 6: 
                    stats.append(stat) 

        stats[-1][1] = "Total Cases"

        stats.remove(stats[-1]) 

        objects = [] 
        for row in stats : 
            objects.append(row[1]) 

        y_pos = np.arange(len(objects)) 

        # performance = [] 
        # for row in stats : 
        #   performance.append(int(row[2]) + int(row[3])) 

        table = tabulate(stats, headers=SHORT_HEADERS) 
        print(table) 

        # plt.barh(y_pos, performance, align='center', alpha=0.5, 
        #               color=(234/256.0, 128/256.0, 252/256.0), 
        #               edgecolor=(106/256.0, 27/256.0, 154/256.0)) 

        # plt.yticks(y_pos, objects) 
        # plt.xlim(1,80) 
        # plt.xlabel('Number of Cases') 
        # plt.title('Corona Virus Cases') 
        # plt.show() 


    elif "attendance" in query.lower():
        c = sqlite3.connect('test12.db')
        cursor=c.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS ATTENDANCE
        (DATESTAMP TEXT, ROLL_NO INT , ATTENDANCE TEXT);''')

        speak("What is the strength of class?")
        n = int(takeCommand())

        
        for i in range (1,n+1):
            speak(i)
            
            datestamp = datetime.datetime.now()
            rno = i
            a_p = takeCommand()
            cursor.execute('''INSERT INTO ATTENDANCE (DATESTAMP, ROLL_NO, ATTENDANCE) VALUES(?, ?, ?)''',(datestamp, rno, a_p))
        
        cursor1 = c.execute('''SELECT * from ATTENDANCE''')
        print("SE IT")
        for row in cursor1.fetchall():
            print("DATE AND TIME =", row[0])
            print("ROLL_NO =", row[1])
            print("ATTENDANCE =",row[2])
            print("\n")

        c.commit()

    elif "marks" in query.lower():
        c = sqlite3.connect('test12.db')
        cursor=c.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS MARKSS
        (ROLL_NO INT, AM_4 INT, OPERATING_SYSTEM INT, COMPUTER_NETWORKS INT, COA INT, AUTOMATA_THEORY INT, TOTAL_MARKS INT);''')
        
        s=1
        while(s==1):
            speak("What is your Roll number?")
            rno = int(takeCommand())
            speak("What are your marks in A.M.4?")
            m1=int(takeCommand())
            speak("What are your marks in OPERATING SYSTEM?")
            m2=int(takeCommand())
            speak("What are your marks in COMPUTER NETWORKS ?")
            m3=int(takeCommand())
            speak("What are your marks in C.O.A.?")
            m4=int(takeCommand())
            speak("What are your marks in AUTOMATA THEORY ?")
            m5=int(takeCommand())

            total=int(m1+m2+m3+m4+m5)

            cursor.execute('''INSERT INTO MARKSS (ROLL_NO, AM_4, OPERATING_SYSTEM, COMPUTER_NETWORKS, COA, AUTOMATA_THEORY, TOTAL_MARKS) VALUES(?, ?, ?, ?, ?, ? ,?)''',(rno, m1, m2, m3, m4, m5, total))
            
            cursor1 = c.execute('''SELECT * from MARKSS''')
            print("SE IT")
            for row in cursor1.fetchall():
                print("ROLL_NO =", row[0])
                print("AM 4=", row[1])
                print("OPERATING SYSTEM =",row[2])
                print("COMPUTER NETWORKS =",row[3])
                print("C.O.A =",row[4])
                print("AUTOMATA THEORY =",row[5])
                print("TOTAL MARKS =",row[6])
                print("\n")

            c.commit()

            speak("Any more entries to be made?")
            ans = takeCommand()
            if "yes" in ans.lower():
                s=1
            else:
                s=0


    speak("Heyy.... Do you need any more help??")
    ans = takeCommand()
    if "yes" in ans.lower():
        speak("How may I help you?")
        s=1
        query=takeCommand()
    else:
        s=0


quickstart.py

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = ddatetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    main()
