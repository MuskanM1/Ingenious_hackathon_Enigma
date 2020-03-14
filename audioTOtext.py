
#-- Audio -> small chunks -> text -> srt -> files
import speech_recognition as sr 

from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("/content/drive/My Drive/Hackathon_2020_Enigma/Video-Text/audio.wav" , "wav") 
chunk_length_ms = 5000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

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
            print("---------Working...-------------\n")
            print(text)
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

