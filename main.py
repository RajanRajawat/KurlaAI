import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclib
from openai import OpenAI

kurla_brain = pyttsx3.init()
kurla_brain.setProperty('rate', 170)
kurla_true = "Ho gaya bacchi"
kurla_false = "ye toh billa shot ho rha hai baa"

def speak(text):
    kurla_brain.say(text)
    kurla_brain.runAndWait()

def aiProcess(d):
    client = OpenAI(
    api_key = "Insert_your_API_here", #<<<Replace API KEY HERE
    base_url = "https://api.kluster.ai/v1"
    )
    completion = client.chat.completions.create(
    model = "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages = [
        { "role": "system", "content": "You are a Kurla boy virtual assistant named KurlaAI, just like Alexa and Siri, from Mumbai India who is uneducated and speaks like tapori"},
        { "role": "user", "content": d }
    ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content
    

def processCommand(c):
    if 'open youtube' in c.lower():
        webbrowser.open('https://www.youtube.com/')
        speak(kurla_true)
    elif 'open instagram' in c.lower():
        webbrowser.open('https://www.instagram.com/')
        speak(kurla_true)
    elif 'open reddit' in c.lower():
        webbrowser.open('https://www.reddit.com/')
        speak(kurla_true)
    elif 'open linkedin' in c.lower():
        webbrowser.open('https://www.linkedIn.com/')
        speak(kurla_true)
    elif c.lower().startswith("play"):
        song = c.lower().split(' ')[1]
        song_link = musiclib.music[song]
        webbrowser.open(song_link)
    elif c.lower() == "bye bantai":
        kurla_brain.stop()
    else: 
        aiOut = aiProcess(c)
        speak(aiOut)

        
if __name__ == "__main__":
    speak('Setting Up KurlaAI.!')
    availableCommands = {
        "Bantai" : "Launch Command",
        "bye bantai" : "Exit Command",
        "Play Kurla" : "Will Play Kurla Song on Browser",
        "Play Bandra" : "Will Play Bandra Song on Browser",
        "Open Instagram" : "Will Open Instagram on Browser",
        "Open YouTube" : "Will Open Youtube on Browser",
        "Open LinkedIn" : "Will Open LinkedIn on Browser",
        "Open Reddit" : "Will Open Reddit on Browser",        
        "Work with AI API too" : 'kluster.ai API Used'

    }
    print(availableCommands)
    
    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Bol na bacchi kya scene...")
                audio = r.listen(source, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("Bhai thinks you said : " + word)
            if(word.lower() == 'bantai'):
                speak("bol naa bhamai kya scene...")
                with sr.Microphone() as source:
                    print("Bol na bacchi kya scene...")
                    audio = r.listen(source, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    processCommand(command)
            
            print("Kya bolta...")
        except sr.UnknownValueError:
            print("Apne ko samjh nhi aaya baa")
        except sr.RequestError as e:
            print("Baa L lagele kya; {0}".format(e))
            
