import tkinter as tk
from PIL import ImageTk, Image
from leo_main import speak  # Assuming leo_main.py provides speak functionality
from GreetMe import greetMe  # Assuming GreetMe.py provides greetMe functionality
import webbrowser
import pyttsx3
import speech_recognition
import os  # For file operations
import notification  # Assuming notification.py provides notification functionality
import mixer  # Assuming mixer.py provides music playback functionality
import random
import speedtest  # For internet speed testing functionality
import datetime
import alarm

# Initialize text-to-speech engineclass Widget:

engine = pyttsx3.init()

class LeoGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Leo Desktop Assistant")
        self.geometry("1200x700")
        self.minsize(600, 350)

        try:
            # Load image with error handling
            image = Image.open("C:/Users/Dnyaneshwar/OneDrive/Desktop/mic1.webp")
            self.image = ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print("Error loading image: Please check the path.")
            self.image = None

        if self.image:
            panel = tk.Label(self, image=self.image)
            panel.pack(side='left', fill='both', expand='no')

        panel = tk.Label(self, text="Welcome to Leo Desktop Assistant")
        panel.pack(side='top', fill='both', expand='no')
        
        
        userText = tk.StringVar()

        userText.set("Step1:Click Run Leo To Give Command\nStep2:Enter Password to open LEO\nStep3:User Said Wakeup then assistant will start")

        userFrame=tk.LabelFrame(self,text="User",font=("Black ops one",10,"bold"))
        userFrame.pack(fill= 'both',expand='yes',)

        left=tk.Message(userFrame,textvariable=userText,bg='#000000',fg='white')
        left.config(font=("Times new Roman",15,'bold'))
        left.pack(fill="both",expand="yes",)

        
       
        # Terminal text box
        terminal_frame = tk.Frame(self, bg="black")
        terminal_frame.pack(fill="both", expand="yes")

        self.terminal = tk.Text(terminal_frame, bg="black", fg="white", font=("Arial", 12))
        self.terminal.pack(fill="both", expand="yes")

        # Run Leo button
        btn = tk.Button(self, text="Run Leo", font=("Arial", 14, "bold"), bg='#4B4B4B', fg='white', command=self.run_leo)
        btn.pack(fill="x", expand="no")

        # Close button
        btn2 = tk.Button(self, text='Close!', font=("Arial", 14, "bold"), bg='#4B4B4B', fg='white', command=self.destroy)
        btn2.pack(fill="x", expand="no")

    def print_to_terminal(self, message):
        """Prints a message to the terminal text box."""
        self.terminal.insert(tk.END, message + "\n")
        self.terminal.see(tk.END)  # Scroll to the bottom

    def take_command(self):
        """Listens for user input using speech recognition."""
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            self.print_to_terminal("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source)

        try:
            self.print_to_terminal("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            self.print_to_terminal(f"You Said: {query}\n")
            return query.lower()  # Convert to lowercase for case-insensitive matching
        except Exception as e:
            self.print_to_terminal("Say that again please.")
            return None

    def run_leo(self):
        """Main loop for handling user queries."""
        while True:
            query = self.take_command()

            if query in ["wake up", "start"]:
                greetMe()
                break

            elif query == "go to sleep":
                speak("Ok sir, You can call me anytime")
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


            # ... (Add logic for other commands like in previous responses)

            else:
                self.print_to_terminal("Sorry, I can't assist you with that yet. Still under development!")

if __name__ == "__main__":
    widget = LeoGUI()
    widget.mainloop()


