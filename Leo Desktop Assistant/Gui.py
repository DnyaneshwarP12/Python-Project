from tkinter import *
from PIL import ImageTk, Image
from leo_main import speak
from GreetMe import greetMe
import webbrowser
import pyttsx3
import speech_recognition


# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# rate = engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def takeCommand():
#         r = speech_recognition.Recognizer()
#         with speech_recognition.Microphone() as source:
#             print("Listening.....")
#             r.pause_threshold = 1
#             r.energy_threshold = 300
#             audio = r.listen(source,0,4)

#         try:
#             print("Understanding..")
#             query  = r.recognize_google(audio,language='en-in')
#             print(f"You Said: {query}\n")
#         except Exception as e:
#             print("Say that again")
#             return "None"
#         return query


class Widget:
    def __init__(self):

        root= Tk()

        root.title("Leo Desktop Assistant")
        root.geometry("1200x700")
        root.minsize(600,350)



        image= ImageTk.PhotoImage(Image.open(r"C:\Users\Dnyaneshwar\OneDrive\Desktop\mic1.webp"))
        panel =Label(root,image=image)
        panel.pack(side='left',fill='both',expand='no')


        panel = Label(text="Welcome to Leo Desktop Assistant")

        panel.pack(side='top',fill='both',expand='no')



        compText = StringVar()
        userText = StringVar()

        userText.set("Click Run Leo To Give Command")

        userFrame=LabelFrame(root,text="User",font=("Black ops one",10,"bold"))
        userFrame.pack(fill= 'both',expand='yes')

        left=Message(userFrame,textvariable=userText,bg='#000000',fg='white')
        left.config(font=("Century Gothic",24,'bold'))
        left.pack(fill="both",expand="yes",)

        compText.set("Hello I am Leo !!! What can i do for you sir ??")


        compFrame=LabelFrame(root,text="Leo",font=("Black ops one",10,"bold"))
        compFrame.pack(fill='both',expand='yes')

        left2=Message(compFrame,textvariable=compText,bg='#000000',fg='white')
        left2.config(font=("Century Gothic",24,'bold'))
        left2.pack(fill="both",expand="yes",)

        btn=Button(root, text="Run Leo", font=("Black ops one", 14 ,"bold"), bg='#4B4B4B', fg='white', command=()).pack(fill="x",expand="no")
        btn2=Button(root,text='Close!',font=("Arial",16,"bold"),bg='#4B4B4B', fg='white',command=root.destroy).pack(fill="x",expand="no")
                
        root.mainloop()

    # def clicked(self):
    #     print("Working..")
    #     query=takeCommand()
    #     self.userText.set('Listening....')
    #     self.userText.set(query)
    #     query=query.lower()

    #     if 'open youtube' in query:
    #         speak("opening youtube")
    #         url="youtube.com"
    #         chrome_path='"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk%s"'
    #         webbrowser.get(chrome_path).open(url)

    #     elif 'open facebook' in query:
    #         speak("opening facebook")
    #         url="facebook.com"
    #         chrome_path='"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk%s"'
    #         webbrowser.get(chrome_path).open(url)



if __name__=="__main__":
    widget=Widget()

