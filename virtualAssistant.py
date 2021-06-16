# A mini Virtual Assistant
# Named it Honey. Start saying Honey, and some text

# Importing all the required libraries
import speech_recognition as speech
import pyttsx3
import pywhatkit as kit
from datetime import datetime
import wikipedia
import pyjokes

__author = "Charitha Sree Jayaramireddy"

# starting the engines
listener = speech.Recognizer()
engine = pyttsx3.init()
# To set the voice to female - 0:male, 1 - female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    """ Used to say the text to us that was found by the system on our command"""
    engine.say(text)
    engine.runAndWait()
def take_input():
    """This function is used to recognize our commands and take them as input"""
    try:
        with speech.Microphone() as source:
            print("Listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command =command.lower()
            if 'honey' in command:
                print(command)
                command = command.replace('honey', '')
            return command
    except:
        pass



def run_command():
    """This function is used to perform actions based on our command """

    command = take_input()
    if 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing' + song)
        kit.playonyt(song)
    elif 'stop' in command:
        exit()
    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        talk("It is" + time)
    elif 'google' in command:
        command = command.replace('google', '')
        kit.search(command)
    elif 'wiki' or 'wikipedia' in command:
        wiki_list = ['wiki', 'wikipedia']
        for item in wiki_list:
            command = command.replace(item, '')
        wiki_info = wikipedia.summary(command, 1)
        talk(wiki_info)
    elif 'joke' or 'jokes' in command:
        talk(pyjokes.get_jokes())
    else:
        talk("Is there anything I can help you with?")
        #kit.search(command)


talk("Hello, I'm honey. How can I help you?")

#Honey takes commands from user for 3 times before exit.
for total in range(3):
        run_command()
