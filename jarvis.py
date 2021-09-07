import pyttsx3
import datetime
import time
initial = time.time()


localtime = time.asctime(time.localtime(time.time()))
print(localtime)
  


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am Jarvis Sir, Please tell me how may I help you!")
    print("I am Jarvis Sir, Please tell me how may i help you!")


if __name__ == "__main__":
    wishMe()
