# -*- coding: utf-8 -*-
"""Ingenious_hackathon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CXY5l48YoyeWhrpjlBAbvqnIDsxKBJgs

# Video to Audio
"""

import moviepy.editor as mp
clip = mp.VideoFileClip("/content/drive/My Drive/Hackathon_2020_Enigma/Video.mp4")
clip.audio.write_audiofile("/content/drive/My Drive/Hackathon_2020_Enigma/Video.wav")

"""# Audio to Text"""

!pip install SpeechRecognition
!pip install pydub

import speech_recognition as sr 

from pydub import AudioSegment 
from pydub.silence import split_on_silence 

r = sr.Recognizer()

with sr.AudioFile('/content/drive/My Drive/Hackathon_2020_Enigma/Video.wav') as source:
	audio = r.listen(source)
	try:
		#text = r.recognize_google(audio, language = 'en-UK')
		text = r.recognize_google(audio)
		print("Working...")
		print(text)
	except sr.UnknownValueError: 
		print("Could not understand audio") 
  
	except sr.RequestError as e: 
		print("Could not request results. check your internet connection") 
	except:
		print("Sorry...")
