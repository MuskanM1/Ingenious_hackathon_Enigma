# Video to Audio
"""

import moviepy.editor as mp

clip = mp.VideoFileClip("/content/drive/My Drive/Hackathon_2020_Enigma/Video.mp4")
clip.audio.write_audiofile("/content/drive/My Drive/Hackathon_2020_Enigma/Video.wav")

'''
# convert mp4 to mp3 
audio = AudioSegment.from_file("/content/drive/My Drive/Hackathon_2020_Enigma/Video.mp4", format="mp4")
audio.export("/content/drive/My Drive/Hackathon_2020_Enigma/audio.mp3", format="mp3")

-------------------

import subprocess

command = "ffmpeg -i /content/drive/My Drive/Hackathon_2020_Enigma/Video.mp4 -ab 160k -ac 2 -ar 44100 -vn /content/drive/My Drive/Hackathon_2020_Enigma/audio.wav"

subprocess.call(command, shell=True)
'''

# convert mp3 to wav                                              
sound = AudioSegment.from_mp3("/content/drive/My Drive/Hackathon_2020_Enigma/audio.mp3")
sound.export("/content/drive/My Drive/Hackathon_2020_Enigma/audio.wav", format="wav")

"""# Audio to Text"""

!pip install SpeechRecognition
!pip install pydub

import speech_recognition as sr 

from pydub import AudioSegment 
from pydub.silence import split_on_silence 

r = sr.Recognizer()

with sr.AudioFile('/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio.wav') as source:
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

from pydub.silence import split_on_silence
import speech_recognition as sr 

from pydub import AudioSegment
from pydub.utils import make_chunks

'''
song = AudioSegment.from_wav('/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio.wav') 

fh = open("/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio_text.txt", "w+") 

chunks = split_on_silence(song, 
        min_silence_len = 5000, 
        silence_thresh = -16
    ) 

i=0
# process each chunk 
for chunk in chunks: 
            
    # Create 0.5 seconds silence chunk 
    
    #chunk_silent = AudioSegment.silent(duration = 10) 

    # add 0.5 sec silence to beginning and  
    # end of audio chunk. This is done so that 
    # it doesn't seem abruptly sliced. 
    
    #audio_chunk = chunk_silent + chunk + chunk_silent 
    audio_chunk = chunk

    # export audio chunk and save it in  
    # the current directory. 
    print("saving chunk{0}.wav".format(i)) 
    # specify the bitrate to be 192 k 
    audio_chunk.export("/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio_chunks/chunk{0}.wav".format(i), bitrate ='192k', format ="wav") 

    # the name of the newly created chunk 
    filename = '/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio_chunks/chunk'+str(i)+'.wav'

    print("Processing chunk "+str(i)) 

    # get the name of the newly created chunk 
    # in the AUDIO_FILE variable for later use. 
    file = filename 

    # create a speech recognition object 
    r = sr.Recognizer() 

    # recognize the chunk 
    with sr.AudioFile(file) as source: 
        # remove this if it is not working 
        # correctly. 
        
        #r.adjust_for_ambient_noise(source) 
        audio_listened = r.listen(source) 

    try: 
        # try converting it to text 
        rec = r.recognize_google(audio_listened) 
        print(rec)
        # write the output to the file. 
        fh.write(rec+". ") 

    # catch any errors. 
    except sr.UnknownValueError: 
        print("Could not understand audio") 

    except sr.RequestError as e: 
        print("Could not request results. check your internet connection") 

    i += 1



'''

#-- Audio -> small chunks -> text -> srt -> files
import speech_recognition as sr 

from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio.wav" , "wav") 
chunk_length_ms = 5000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) # Make chunks of five sec

#Export all of the individual chunks as wav files

full_text = ""
srt_text = ""
t_sec = 0
t_min = 0
t_hour = 0

for i, chunk in enumerate(chunks):

    chunk_name = "/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio_chunks/chunk{0}.wav".format(i)
    #print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")

    r = sr.Recognizer()

    with sr.AudioFile(chunk_name) as source:
        audio = r.listen(source)
        try:
            #text = r.recognize_google(audio, language = 'en-UK')
            text = r.recognize_google(audio)
            # print("---------Working...-------------\n")
            # print(text)
            full_text = full_text + text + ' '
            
            #print(srt_text)

        except sr.UnknownValueError: 
            print("----------Could not understand audio----------\n") 
    
        except sr.RequestError as e: 
            print("----------Could not request results. check your internet connection----------\n") 
        except:
            print("----------Sorry...---------\n")

    t_sec = t_sec + 5

print(full_text)
full_text_file = open("/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio_chunks/recognized.txt", "w") 
full_text_file.write(full_text)
full_text_file.close()

"""# Punctuation"""

!pip install punctuator

!gdown https://drive.google.com/uc?id=0B7BsN5f2F1fZd1Q0aXlrUDhDbnM

from punctuator import Punctuator
p = Punctuator('/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/Model/Demo-Europarl-EN.pcl')

punc_full_text = p.punctuate(full_text)

print(punc_full_text)

"""# Translation"""

!pip install googletrans

from googletrans import Translator
translator = Translator()
translated_text = translator.translate(punc_full_text, dest='hi').text
print(translated_text)

"""# Text to speech"""

!pip install pyttsx3==2.7
!pip install talkey
!pip install py-espeak-ng
!pip install gTTS

'''
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()
'''

from gtts import gTTS 

mytext = full_text

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=True)

myobj.save("/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/welcome.wav")

"""# Audio Remove"""

import subprocess
command = 'for file in *.mp4; do ffmpeg -i "$file" -c copy -an "noaudio_$file"; done'
subprocess.call(command)

from google.colab import drive
drive.mount('/content/drive')



