from tkinter import *
from tkinter import ttk
##################
# Library for Recognition
import speech_recognition as spr
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import googletrans
import time
import random

def RecognizeAndSpeech(sound1='th',sound2='zh-cn'):

	time.sleep(2)
	print('Recognizing..')
	#print(googletrans.LANGUAGES)
	##### RECOGNITION ######
	rec = spr.Recognizer()

	with spr.Microphone() as speak:
		audio = rec.listen(speak)

	try:
		result = rec.recognize_google(audio,language=sound1)
		print('Stop...')
		print(result)
	except:
		print('Error We can not recognize your sound')
		result = 'ERROR'

	##### TRANSLATOR ######

	LAM = Translator()
	word = LAM.translate(result,dest=sound2)
	print('Meaning: ',word.text)

	##### TEXT TO SPEECH ######

	tts = gTTS(text=word.text, lang=sound2)

	number = random.randint(0,20)

	tts.save('result{}.mp3'.format(number))

	playsound('result{}.mp3'.format(number))

##################

GUI = Tk()
GUI.geometry('500x500')
GUI.title('AMA SHOP')


def SpeakThai():
	print('อาม่ากำลังพูด...')
	RecognizeAndSpeech('th','ja')

def SpeakOther():
	print('ลูกค้ากำลังพูด...')
	RecognizeAndSpeech('ja','th')

##############
F1 = Frame(GUI)
F1.place(x=50,y=370)

B1 = ttk.Button(F1,text='Speak Thai', command=SpeakThai)
B1.pack(ipadx=20,ipady=10)

##############
F2 = Frame(GUI)
F2.place(x=300,y=370)

B2 = ttk.Button(F2,text='Speak Your Language', command=SpeakOther)
B2.pack(ipadx=20,ipady=10)

GUI.mainloop()