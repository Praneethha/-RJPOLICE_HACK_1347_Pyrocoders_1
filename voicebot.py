import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
     machine.say(text)
     machine.runAndWait()

def get_instruction():
    try:
       with sr.Microphone(device_index=0) as source:
          talk("Welcome, I am Alex, may I know your name?")
          print("Alex is Listening...")
          r.adjust_for_ambient_noise(source)
          speech = r.listen(source)
          instruction = r.recognize_google(speech)
          instruction = instruction.lower()
          if "alex" in instruction:
             instruction = instruction.replace('alex', "")
             print(instruction)
             return instruction
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None

def play_instruction():
    if os.path.exists('input.txt'):
    with open('input.txt', 'r') as file:
        data = file.read().replace('\n', '')
        instruction = get_instruction(data)
    else:
    instruction = get_instruction()  
        if instruction is not None and "play" in instruction:
        song = instruction.replace('play', "") 
        talk("Playing " + song)   
        pywhatkit.playonyt(song)
        elif instruction is not None and 'time' in instruction:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('The current time is ' + time)
        elif instruction is not None and 'my name is' in instruction:
            myname = instruction.replace('my name is', "")
            talk("Hello "+ myname + ".How can I help you?")
        elif instruction is not None and 'I am' in instruction:
            mynamewillbe = instruction.replace('I am', "")
            talk("Hello "+ mynamewillbe + ".How can I help you?")
        elif instruction is not None and  'date' in instruction:
            date = datetime.datetime.now().strftime('%D /%m /%Y')
            talk("date is"+ date)
        elif instruction is not None and  'how are you' in instruction:
            talk("I am fine, how about you?")
        elif instruction is not None and  'what is your name' in instruction:
            talk("I am alex, What can i do for you?")
        elif instruction is not None and  'who is ' in instruction:
            human = instruction.replace('who is', "")
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
play_instruction()
