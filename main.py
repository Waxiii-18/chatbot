import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import cohere
import time


r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def client(command):
    co = cohere.ClientV2("PvmXPk5ceL3PkVZzvangUMBPdI3Jx3TT3iQ7Zsva") 
    response = co.chat(
    model="command-r-plus-08-2024",
    messages=[{"role": "system", "content":"you are virtual assitant pretends to be a named waxy who helps with short responses and has great humor,also gives proper response"},
              {"role": "user", "content": command}],
    # max_tokens=50,
    # temperature=0.3  # Lower value makes responses more direc t
    )
    return (response.message.content[0].text)
    
def processcommand(c):
    print(f"Your command :{c}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music.get(song)
        webbrowser.open(link)
    else:
       output = client(command)
       speak(output)

if __name__ == "__main__":
    speak("Intializing waxy.......")
    speak("intialized")
    speak("say the word when you need me")
   
    while True:
        
        print("processing.....")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("listening....")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)
            if (word.lower()=="surya"):
                speak("cheppandi sir")
                with sr.Microphone() as source: 
                    r.adjust_for_ambient_noise(source)
                    print("activate....")
                    print("listening for command......")
                    audio = r.listen(source,timeout=10,phrase_time_limit=5)
                command = r.recognize_google(audio)
                processcommand(command)
        except Exception as e:
            print("Error:{0}".format(e))
            
            
