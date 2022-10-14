import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listening = sr.Recognizer()
my_mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with my_mic as source:
            print("Listening...!!")
            listening.adjust_for_ambient_noise(source) #reduce noise
            voice = listening.listen(source) #take voice input from the microphone
            command=listening.recognize_google(voice) #to print voice into text
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)

    except:
        pass
    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play'  in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("The Current Time is" + time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("sorry,I am already taken")
    elif 'hello' in command:
        talk('Heyyy Om')
    elif 'who created you'  in command:
        talk(' om ahir,my boss')
    elif 'are you single' in command:
        talk('taken for others,single for you')
    elif 'where is nandura located' in command:
        talk('In Everyones Heart')
    elif 'birthday' in command:
        talk('I celebrate birthday with my boss on thirty october')
    elif 'find girlfriend for me' in command:
        talk('Go get some sleeeeeeeep brother')
    elif 'how much you love me' in command:
        talk('I love you next to my creator')
    elif 'who created you' in  command:
        talk('Mr.Om Ahir')
    elif "cricket score" in command:
        talk("Opening cricbuzz ")
        webbrowser.open("www.cricbuzz.com")
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Can you please repeat the command')

while True:
    run_alexa()