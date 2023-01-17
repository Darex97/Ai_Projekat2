import os
import speech_recognition as sr
from gtts import gTTS
from translate import Translator
from tkinter import *

root = Tk()

def Text_to_speech():
    translator= Translator(to_lang="sr")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)


    text=r.recognize_google(audio)

    textNaEngleskom=gTTS(text)
    textNaEngleskom.save('Engleski.mp3')

    
    translation = translator.translate(text)
    textZaIZgovor=gTTS(translation, lang='sr')
    textZaIZgovor.save('Srpski.mp3')



def Exit():
    root.destroy()

def PlayTranslation():
    os.system("Srpski.mp3")



root.geometry("350x300") 
root.configure(bg='ghost white')
root.title("CurryPy - TRANSLATOR")

Label(root, text = "TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="CurryPy", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Label(root,text ="Press record and start talking", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)


Button(root, text = "Record", font = 'arial 15 bold' , command = Text_to_speech ,width = '7' , bg = 'Yellow').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'Translation', width = '9' , command = PlayTranslation, bg = 'Green').place(x=130 , y = 140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x= 260, y = 140)


root.mainloop()