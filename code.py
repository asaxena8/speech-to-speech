from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import speech_recognition as spr
from gtts import gTTS
import os

root = Tk()  # Initialize the Tkinter window
root.geometry('1080x400')  # Set window size
root.resizable(0, 0)  # Disable window resizing
root.config(bg='#eeebdd')  # Set background color
root.title("SPEECH TRANSLATOR")  # Set window title

# Adding labels to the window
Label(root, text=" SPEECH TRANSLATOR", fg="#1b1717", font="century 20 italic", bg='#eeebdd', width=20).pack()
Label(root, text="MINI PROJECT", fg="#800000", font="Lucida 20 roman", width='20', bg='#eeebdd').pack(side='bottom')
Label(root, text="->Click on translate ", font='calibari 14 italic', fg='#1b1717', bg='#eeebdd').place(x=10, y=175)
Label(root, text="->Say hello to initiate the Translation", font='calibari 14 italic', fg='#1b1717', bg='#eeebdd').place(x=10, y=220)
Label(root, text="->Select your language to translate", font='calibari 14 italic', fg="#1b1717", bg='#eeebdd').place(x=10, y=130)

# Text widget to display translated text
Output_text = Text(root, font='Times 20 italic', height=7, wrap=WORD, padx=5, pady=5, width=32, borderwidth=3, relief="solid")
Output_text.place(x=600, y=100)

# Get the list of available languages for translation
language = list(LANGUAGES.values())

# Dropdown for selecting the input language
src_lang = ttk.Combobox(root, values=language, width=21, font="Verdana 12 bold")
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

# Dropdown for selecting the output language
dest_lang = ttk.Combobox(root, values=language, width=21, font="Verdana 12 bold")
dest_lang.place(x=790, y=60)
dest_lang.set('choose output language')


def Translate():
    # Initialize speech recognizer and microphone
    recog1 = spr.Recognizer()
    mc = spr.Microphone()

    # Recognize speech input for 'hello' to initiate translation
    with mc as source:
        print("Speak 'hello' to initiate the Translation !")
        print("~~")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        MyText = recog1.recognize_google(audio)
        MyText = MyText.lower()

    if 'hello' in MyText:
        translator = Translator()  # Initialize translator

        # Recognize speech input for translation
        with mc as source:
            print("Speak a sentence...")
            recog1.adjust_for_ambient_noise(source, duration=0.2)
            audio = recog1.listen(source)
            get_sentence = recog1.recognize_google(audio)
            try:
                print("Phase to be Translated :" + get_sentence)
                # Translate the recognized sentence
                text_to_translate = translator.translate(get_sentence, src=src_lang.get(), dest=dest_lang.get())
                text = text_to_translate.text
                print(text)
                # Convert translated text to speech and save as an audio file
                speak = gTTS(text=text, lang="en", slow=False)
                speak.save("captured_voice.mp3")
                os.system("start captured_voice.mp3")  # Play the audio file
            except spr.UnknownValueError:
                print("Unable to Understand the Input")
            except spr.RequestError as e:
                print("Unable to provide Required Output".format(e))

        # Display translated text in the output text box
        translated = translator.translate(text=text, src=src_lang.get(), dest=dest_lang.get())
        Output_text.insert(END, translated.text)


# Button to trigger the translation function
trans_btn = Button(root, text='Translate', font='monaco 10 normal', pady=5, command=Translate, fg='#FFFFFF',
                   activebackground='#FFD700', bg='#810000', borderwidth=3, relief="solid")
trans_btn.place(x=500, y=180)

root.mainloop()  # Start the main event loop
