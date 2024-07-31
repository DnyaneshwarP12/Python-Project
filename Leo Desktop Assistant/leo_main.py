import pyttsx3
import speech_recognition 
import datetime
import os
import webbrowser
import random
import mixer
import notification
import speedtest
import game
import smtplib
import playsound

from tkinter import *
from PIL import ImageTk, Image
# from leo_main import takeCommand, speak
# from GreetMe import greetMe
import webbrowser
import pyttsx3
import speech_recognition
import leo_main 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init()
class Widget:
    def __init__(self):
        root = Tk()

        root.title("Leo Desktop Assistant")
        root.geometry("1200x700")
        root.minsize(600, 350)

        image = ImageTk.PhotoImage(Image.open(r"C:\Users\Dnyaneshwar\OneDrive\Desktop\mic1.webp"))
        panel = Label(root, image=image)
        panel.pack(side='left', fill='both', expand='no')

        panel = Label(text="Welcome to Leo Desktop Assistant")
        panel.pack(side='top', fill='both', expand='no')

        # compText = StringVar()
        # userText = StringVar()

        # userText.set("Click Run Leo To Give Command")

        # userFrame = LabelFrame(root, text="User", font=("Black ops one", 10, "bold"))
        # userFrame.pack(fill='both', expand='yes')

        # left = Message(userFrame, textvariable=userText, bg='#000000', fg='white')
        # left.config(font=("Century Gothic", 24, 'bold'))
        # left.pack(fill="both", expand="yes", )

        # compText.set("Hello I am Leo !!! What can i do for you sir ??")

        # compFrame = LabelFrame(root, text="Leo", font=("Black ops one", 10, "bold"))
        # compFrame.pack(fill='both', expand='yes')

        # left2 = Message(compFrame, textvariable=compText, bg='#000000', fg='white')
        # left2.config(font=("Century Gothic", 24, 'bold'))
        # left2.pack(fill="both", expand="yes", )

        # Terminal Screen
        terminalFrame = Frame(root, bg="black")
        terminalFrame.pack(fill="both", expand="yes")

        self.terminal = Text(terminalFrame, bg="black", fg="white")
        self.terminal.pack(fill="both", expand="yes")

        btn = Button(root, text="Run Leo", font=("Black ops one", 14, "bold"), bg='#4B4B4B', fg='white', command=self.takeCommand())
        btn.pack(fill="x", expand="no")
        btn2 = Button(root, text='Close!', font=("Arial", 16, "bold"), bg='#4B4B4B', fg='white', command=root.destroy)
        btn2.pack(fill="x", expand="no")

        root.mainloop()

    def print_to_terminal(self, message):
        self.terminal.insert(END, message + "\n")
        self.terminal.see(END)  # Scroll to the bottom



    def takeCommand():
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source,0,4)

        try:
            print("Understanding..")
            query  = r.recognize_google(audio,language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query


    def alarm(query):
        timehere = open("Alarmtext.txt","a")
        timehere.write(query)
        timehere.close()
        os.startfile("alarm.py")


    if __name__ == "__main__":
        while True:
            query = takeCommand().lower()
            if "wake up" in query:
                from GreetMe import greetMe
                greetMe()

                while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir , You can me call anytime")
                        break 

                    elif "hello" in query:
                        speak("Hello sir, how are you ?")
                    elif "i am fine" in query:
                        speak("that's great, sir")
                    elif "how are you" in query:
                        speak("Perfect, sir")
                    elif "thank you" in query:
                        speak("you are welcome, sir")

                    elif "google" in query:
                        from SearchNow import searchGoogle
                        searchGoogle(query)
                    elif "youtube" in query:
                        from SearchNow import searchYoutube
                        searchYoutube(query)
                    elif "wikipedia" in query:
                        from SearchNow import searchWikipedia
                        searchWikipedia(query)

                    elif "the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")    
                        speak(f"Sir, the time is {strTime}")

                    elif "finally sleep" in query:
                        speak("Going to sleep,sir")
                        exit()

                    elif "open" in query:
                        from Dictapp import openappweb
                        openappweb(query)
                    elif "close" in query:
                        from Dictapp import closeappweb
                        closeappweb(query)

                    elif "set an alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")

                    elif "pause" in query:
                        pyautogui.press("k")
                        speak("video paused")
                    elif "play" in query:
                        pyautogui.press("k")
                        speak("video played")
                    elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted")

                    elif "volume up" in query:
                        from keyboard import volumeup
                        speak("Turning volume up,sir")
                        volumeup()
                    elif "volume down" in query:
                        from keyboard import volumedown
                        speak("Turning volume down, sir")
                        volumedown()

                    elif "remember that" in query:
                        rememberMessage = query.replace("remember that","")
                        rememberMessage = query.replace("Leo","")
                        speak("You told me to remember that"+rememberMessage)
                        remember = open("Remember.txt","a")
                        remember.write(rememberMessage)
                        remember.close()
                    elif "what do you remember" in query:
                        remember = open("Remember.txt","r")
                        speak("You told me to remember that" + remember.read())

                    elif "tired" in query:
                        speak("Playing your favourite songs, sir")
                        a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                        b = random.choice(a)
                        if b==1:
                            webbrowser.open()#Here put the link of your video)

                    elif "whatsapp" in query:
                        from Whatsapp import sendMessage
                        sendMessage()

                    # elif "change password" in query:
                    #     speak("What's the new password")
                    #     new_pw = input("Enter the new password\n")
                    #     new_password = open("password.txt","w")
                    #     new_password.write(new_pw)
                    #     new_password.close()
                    #     speak("Done sir")
                    #     speak(f"Your new password is{new_pw}")

                    elif "schedule my day" in query:
                        tasks = [] #Empty list 
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = takeCommand().lower()
                        if "yes" in query:
                            file = open("tasks.txt","w")
                            file.write(f"")
                            file.close()
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in query:
                            i = 0
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()

                    elif "show my schedule" in query:
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notification.mp3")
                        mixer.music.play()
                        notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )

                    elif "open" in query:   #EASY METHOD
                        query = query.replace("open","")
                        query = query.replace("Leo","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter") 

                    elif "internet speed" in query:
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                        download_net = wifi.download()/1048576
                        print("Wifi Upload Speed is", upload_net)
                        print("Wifi download speed is ",download_net)
                        speak(f"Wifi download speed is {download_net}")
                        speak(f"Wifi Upload speed is {upload_net}")

                    elif "play a game" in query:
                        from game import game_play
                        game_play()

                    elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")

                    elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")

                    elif "focus mode" in query:
                        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                        if (a==1):
                            speak("Entering the focus mode....")
                            os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
                            exit()

                        
                        else:
                            pass

                    elif "show my focus" in query:
                        from FocusGraph import focus_graph
                        focus_graph()


                    elif "translate" in query:
                        from Translator import translategl
                        query = query.replace("jarvis","")
                        query = query.replace("translate","")
                        translategl(query)

                    