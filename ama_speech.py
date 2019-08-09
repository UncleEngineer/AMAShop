#ama_speech.py
import speech_recognition as spr
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import googletrans
import time


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
	tts.save('result.mp3')

	playsound('result.mp3')

RecognizeAndSpeech('th','zh-cn')
RecognizeAndSpeech('th','de')
