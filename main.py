import speech_recognition as sr #helps to recognize 
import webbrowser #connecting to webbrowser
import pyttsx3 #text to speech library
import music_library#for music reference
import requests



recognizer=sr.Recognizer()
engine=pyttsx3.init()
news_api="e6f883b573c84c88b40f63cef7540e3f"

#speech 
def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(' ')[1]
        link =music_library.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=e6f883b573c84c88b40f63cef7540e3f")
        if r.status_code == 200:
            #parse the json response
            data=r.json()
            #extract the articles
            articles=data.get('articles', [])
            
            #print the headlines
            for article in articles:
                speak(article['title'])
    else:
        speak("Not found")
        
                
                
if __name__=="__main__":
    speak("Initializing Jarvis .....")
    while True:
        #listen to word jarvis and then do the tasks
        #obtain audio from microphone
        r=sr.Recognizer()
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source, timeout=2, phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yaa")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
        
        except Exception as e:
            print("Sphinx Error: {0}".format(e))