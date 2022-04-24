import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" i  am  Desktop assistant!,a virtual artificial inteligence , I am here to asist you with variety of tasks,       system now fully operational")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saplekaushal@gmail.com', 'kaushal@1142')
    server.sendmail('saplekaushal@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    this_program = True
    while this_program:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'food'in query:
            speak("what would you like to eat ")
            restaurant=takeCommand().lower()
            if 'dominos' in restaurant:
                speak("opening dominos")
                webbrowser.open("https://www.dominos.co.in")
            elif 'zomato' in restaurant:
                speak("opening zomato")
                webbrowser.open("https://www.zomato.com/india")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\kaushal saple\\OneDrive\\Desktop\\final project\\Song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\kaushal saple\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)
        elif 'nice' in query:
            speak("i m happy u like it")
        elif 'buy ' in query:
            speak("order online on amazon ")
            webbrowser.open("https://www.amazon.in")
        elif 'project' in query:
            speak("everything you need to know about the project")
            speak("Far from a being a fad, the overwhelming success of speech-enabled products like Amazon Alexa has proven that some degree of speech support will be an essential aspect of household tech for the foreseeable future. If you think about it, the reasons why are pretty obvious. Incorporating speech re`cognition into your Python application offers a level of interactivity and accessibility that few technologies can match.")
            speak("The accessibility improvements alone are worth considering. Speech recognition allows the elderly and the physically and visually impaired to interact with state-of-the-art products and services quickly and naturally no G U I needed!")
        elif 'good' in query:
            speak("always happy to help")
        elif 'working' in query:
          
            speak("To decode the speech into text, groups of vectors are matched to one or more phonemes—a fundamental unit of speech. This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.")
        elif 'history' in query:
            speak("Speech recognition has its roots in research done at Bell Labs in the early 1950s. Early systems were limited to a single speaker and had limited vocabularies of about a dozen words. Modern speech recognition systems have come a long way since their ancient counterparts. They can recognize speech from multiple speakers and have enormous vocabularies in numerous languages.")
        elif 'desktop assistant' in query:
            speak("Hi     How are you?")
        elif 'what can you do' in query:                                                 
            speak("I know everything and     i can do anything you desire")
        elif 'who created' in query:
            speak("i   was     created by kaushal and mayur")
        elif 'open d drive' in  query:
            speak("accessing h drive")
            codePath = "D:\\"
            os.startfile(codePath)
        elif 'open c drive' in  query:
            speak("accessing OS drive")
            codePath = "C:\\"
            os.startfile(codePath)
        

        elif 'email to mayur' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mayurshekade2001@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")    
        elif "stop" in query:
            this_program = False