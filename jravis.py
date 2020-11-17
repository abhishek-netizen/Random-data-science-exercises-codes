import pyttsx3 #importing text to speech library works fine in both python 3 and in 2
import datetime
import pyjokes
import webbrowser
import wikipedia #pip install wikipedia
import speech_recognition as sr #pip install speechRecognition

engine = pyttsx3.init('sapi5') #https://en.wikipedia.org/wiki/Microsoft_Speech_API
voices = engine.getProperty('voices')
#print(voices[0].id) #Lets print the voice
engine.setProperty('voices',voices[0].id) #setting david as our voices


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak(" I am Ironman sir, Please tell me how may i help you")

def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . .")
        r.pause_threshold = 1 #wait for a second
        audio = r.listen(source)

    try:
        print("Recognising . . .")
        query = r.recognize_google(audio, language='en-in')
        #print(f"User said: {query}")
        print("User said {}.".format(query))

    except Exception as e:
        print("Please say that again please . . .")
        return "None"
    return query










if __name__ == "__main__":
    wishMe()
    #takeCommand()
    while True:
        query = takeCommand().lower()

        #Logic to executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia . . .")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif ' tell me jokes' in query:
            joke = print(get_joke())
            Speak(joke)
