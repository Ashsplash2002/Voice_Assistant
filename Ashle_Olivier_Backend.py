#This excellent code was made by Geeks4Geeks and tweeked for my usage. 
import pyttsx3
import speech_recognition as speechrecogniser
import webbrowser 
import datetime 
import wikipedia

def takeCommand():
 
    recognizer = speechrecogniser.Recognizer()
 
    with speechrecogniser.Microphone() as source:
        print('Listening')         
        
        recognizer.pause_threshold = 0.7
        audio =recognizer.listen(source)         
       
        try:
            print("Recognizing")             
            
            Query = recognizer.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
             
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
         
        return Query

def speak(audio):
     
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')     
    
    engine.setProperty('voice', voices[0].id)     
   
    engine.say(audio)      
    
    engine.runAndWait()

def tellDay():     
    
    day = datetime.datetime.today().weekday() + 1     
   
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)

def tellTime():     
   
    time = str(datetime.datetime.now())     
   
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The current time is" + hour +' ' + min ) 

def Hello():     
   
    speak("hello I am your voice assistant. What can I help you with today")
 
def Take_query(): 
    
    Hello()     
    
    while(True):         
       
        query = takeCommand().lower()
        if "open page" in query:
            speak("Opening geeks4geeks")             
            
            webbrowser.open("www.geeksforgeeks.com")
            continue
         
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
             
        elif "day today" in query:
            tellDay()
            continue
         
        elif "what time is it now" in query:
            tellTime()
            continue         
     
        elif "bye" in query:
            speak("Good bye. Have a nice day")
            exit()
                  
        elif "what is your name" in query:
            speak("I am Luna. Your voice Assistant")

        elif "how were you made" in query:
            speak("Let me show you ")
            webbrowser.open("https://www.geeksforgeeks.org/build-a-virtual-assistant-using-python/")

        elif "i want to play a game" in query:
            speak("What game would you like to play")
            if "I want to play snake":
                speak("Opening snake.io")
            webbrowser.open("https://snake.io/")

        elif "what is the weather forecast" in query:
            speak("Let me take you to a weather forecasting website")
            webbrowser.open("https://www.ventusky.com/?p=52.4;4.9;5&l=temperature-2m")
        else:
            speak("Please repeat I did not understand")

if __name__ == '__main__':
     
    
    Take_query()

 