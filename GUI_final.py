

import tkinter as tk
from tkinter import *
import ttk
from tkinter import filedialog
#import tkFileDialog as filedialog
import os

global input_path
global lan

#r = tk.Tk()

def video_translator(input_path,lan):

	# Video to Audio

	import moviepy.editor as mp

	#input_path = '/home/vaishwi/Documents/Hackathon/test/Video.mp4'
	#lan='gu'

	clip = mp.VideoFileClip(input_path)
	pathList = input_path.split("/")
	fileName = pathList[-1]
	print("---------------fileneme", fileName)
	pathList = pathList[:-1]
	print("---------------pathList", pathList)
	s = "/"
	parent_path = s.join(pathList)
	print("----------------Parent Path:", parent_path)
	clip.audio.write_audiofile(parent_path+"/audio.wav")




	"""# Audio to Text"""

	import speech_recognition as sr 

	from pydub import AudioSegment 
	from pydub.silence import split_on_silence 

	from pydub.silence import split_on_silence
	import speech_recognition as sr 

	from pydub import AudioSegment
	from pydub.utils import make_chunks


	#-- Audio -> small chunks -> text -> srt -> files
	import speech_recognition as sr 

	from pydub import AudioSegment
	from pydub.utils import make_chunks

	import os

	myaudio = AudioSegment.from_file(parent_path+"/audio.wav" , "wav") 
	chunk_length_ms = 5000 # pydub calculates in millisec
	
	'''
	chunks = make_chunks(myaudio, chunk_length_ms) # Make chunks of five sec

	#Export all of the individual chunks as wav files

	#try:
	#	os.makedir('audio_chunks')

	#os.chdir('audio_chunks')


	full_text = ""
	t_sec = 0
	
	for i, chunk in enumerate(chunks):

		 chunk_name = parent_path+"/audio_chunks/chunk{0}.wav".format(i)
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
	full_text_file = open("recognized.txt", "w") 
	full_text_file.write(full_text)
	full_text_file.close()

'''
	full_text = "this free cake insta film thanks marrying me know see you there free cake everyone I likes thanks for clicking and welcome to this person wearing a business or professional email in English this is useful for those who are just starting a corporate charge 1 Yuan exchange you can increase environment where are constant and save I use my email everyday I can tell you 100 that I have used always 14 in my email in career so I sent how can I use these these are phrases that you can you an internal emails between yourself and your colleagues between yourself and someone to work with your company so maybe you know someone who is selling immunotechnology company like maybe someone to surprise paper company and you have to interact with them so you can use these phrases and expressions with them so first start with the we have hello hi hey picture of universe wondering why did you write in to whom it may concern I guess it depends on your own AC compare with formality having volcano in Canada and exchanging emails with people in the United States most people accountable with a hello or a height only user hi for someone you know so these are in love a formality aap abhi history hello would be the most Pune what be there in utero and a is a dairy farm your very informal so only use this with people you know well whether you have a good professional relationship with next so one thing you might do in an email is to introduce a new top what to inform someone or something maybe not just one person may be a group of people maybe Lahore Apartment sofa this is to inform you that very general maybe someone has received a promotion in your company something you might see from your boss over if you are a boss a manager you send this to your team this is to inform you that amino se Roza you have any poem in this is to inform has been promoted to the projection of so you are giving information to your team just like you know now this is very informal so omission is with the people you know well people in your company maybe a friend in the company just let you know Moin formal casual way that you can use in an email instead message to inform you that I am so for example hey just like you know I am not here on Friday if you need anything from me before Friday passive you introducing a topic for informing your company something so good news news Dhaar news now you know I used in excavation news now it's so news you know I just got promoted or good news I am always something like that Varna caring teacher free today bad news make Vansh sorry I can make lunch it doesn't I didn't want you making much means I can't go to so you have this is to inform you that just Now news news news news next if you are all going up on a previous discuss a previous email following up means you have a conversation about the topic before maybe and person email maybe by carrier pigeon and you want to follow up on that email I care you temperate Supreme is so I am you can say as we discussed or as discussed you can obviously at this as discussed yesterday as discussed at the meeting as discussed this morning please remove your shoes when you enter my strange thing Meri you are so next interesting as discussed you can also say to follow meaning of follow-up discussion Samsung a 9 as we discussed ocupol what to give in UP Aandhi information we discussed you can say Innova please come to work on time what we do in the 5 days other people use the festive next recording in regards to you can use either one rupees so it justify how you feel in the moment so I am you know Happy January regarding adding the quality of your deodorants please change everyone can notice everyone notices receiver strong kalona strong the ordinance strong cell having fun with evening ok as per as those so simulated setting recording in regard to you are the topic here so if you are sending an Email about you company budget as per as the budget goes please be careful with you sending as far as I know this week is it going to begin at 11 o'clock you power if you want something if you want to request something many many options are so I'd like to know is how to play any question you can think about I like to know when the meaning and I'd like to know if bring anything next inspecting it now you can also say could you let me know if and how it may be utilised because its roses birthday in our in our department and you can say could you let me know how much money I should presence of browsers gift card next I'm serious can you confirm right to you like 100% Love Me Now confirm when how at Sarai so this is probably serious topic to you could use it to be funny quotes no expression to confirm how much money I should games for how much money I should contribute to confirm if do you know if when how do you know so do you know when when the money will be in my account do you know if the principal need morning you have details any update on a topic so if you are ordering promotion of ethereum company from another company and you been waiting for a long time may be one which is long time in most businesses you have any update on the promotion of material do you have any details any new details on the promotional material and say this hey could you give me an update could you give me about in estimate so I am a quote if you are in charge in dealing with some of the upper and parts in new company we are you dealing with other companies and you want to know how much money does it cost for you to print this promote Taurus 9 how much money does it cost for 5 new computers can you give me a quote basically you here serious I am for you know maybe some company send a physical paper The breakdown everything could you let me know how much cost give me an estimate of this means an idea how much money think your dinner cost so so far we said receive introduce the topic maybe we have followed up on the previous fashion weave are somethings requested somethings and what's next next we have saying thanks so you can write a thanks for getting back to me so you send send email Jason back and answer the question for you and you want to another email is like the email in the chain survey thanks for getting back to me this means thanks for riding back thanks for answering my question I am fine and then you can News 18 real faces have regarding this question right ok confirm thanks for the information if you again if you are in a company the people well thanks for the end is pretty casual and formal only producer with people you know well the information affect the owner of your company information is better for the heads up so this is alamo inform thanks for the heads up is usually thanks for the thanks for the update so for example tips Sanjivani email and essay I am a is going to be new physician opening next week why don't you you know and get ready cuz I think you will be good for this job so you this can be a new position opening next week and company thanks for the thanks for the warning so I know before other people hazard you can see the information maths in the future thanks for the update thanks for the email hey thanks for following up on or sinks for power thanks for basically keeping up to date on getting new information from this person on this topic survey thanks for following up with the accounting department thanks for following up on our contract our country discussion something Micra thanks for your help thanks for your help with something thanks for watching inse uses in if you walk into something it means you I am you know you it take a deeper look at so if I call it as confuse something other asking you to get the details situation or get the details of something and if we can see some any century information se I got information the cost SS $224 224 hours thanks for watching and other discourse changes everything many ways to say thanks many things to be thankful for finally closing your email sending you can say how get back to you as soon as I can answer if someone has asked you for something has made a request I know you send them some information you respond and you can just and was how get back to you if you want to you know the extra polite how get back to you as soon as I can this is very similar to Allah you know as soon as I can swordsman Naino ke I will let you know I'll keep you posted this means if I have new information I would send information to you I will give you an update when I know something the next year you asking for you was the quest and you want a response so you end with please love me now or just let me know at a please you want to deactivate keep you posted keep me posted keep me updated if there is information tell me ok send me an email if there is no information on the topic we have discussed and how should you and your email what's to formal but not for me sincerely I am I really sincerely on Mike government documents things that official from the bank arm if you have a complaint letter to a landlord you know your sincerely word for those official situations in most internal company emails you should be and my wife thanks you could say are you could say all the best so thanks Inferno thanks words for somebody your working with outside the company sincerely I will just keep it to you more official official special situations dealing with government for bank certificate companies are you so understanding of this material as always you can check all the quiz on in with I want to see from you guys is in the comments write neem news Mike as many of these phrases as you can understand sample email to me in the comments that I can read and I can I can office after I gave you today the ending it is have to go in the water like you might just study now saying hey Siri hey Browser thanks for getting back to me this could be the first thing it doesn't have to be introductory fighter jet in the previous board it depends is about of forest and why you want stress Thomas and you the quiz which I already said and done after you the quizup check the comments and all that stuff I could YouTube sorry friends Xperia biolix Cristiano se yeah ok SBI PO information off here subscribe calling bell and check me on Facebook check me on Twitter and talk Himachal promoting cmat so one more thing if you want to forward with you check out the support on inward and you can donate and how much do this for a long long long long time next time thanks for clicking and I am gonna go have that"
	


	"""# Punctuation"""

	from punctuator import Punctuator
	p = Punctuator('Demo-Europarl-EN.pcl')

	punc_full_text = p.punctuate(full_text)

	print(punc_full_text)

	"""# Translation"""

	from googletrans import Translator
	translator = Translator()
	translated_text = translator.translate(punc_full_text, dest=lan).text
	print(translated_text)

	"""# Text to speech"""

	from gtts import gTTS 
	import subprocess

	mytext = translated_text

	# Language in which you want to convert 
	language = lan

	# Passing the text and language to the engine,  
	# here we have marked slow=False. Which tells  
	# the module that the converted audio should  
	# have a high speed 
	myobj = gTTS(text=mytext, lang=language, slow=False)

	myobj.save(parent_path+"/test_output_audio.wav")


	cmd = "ffmpeg -i "+input_path+" -c copy -an "+parent_path+"/_noaudio.mp4"
	subprocess.call(cmd,shell=True)


	cmd1 = "ffmpeg -i "+parent_path+"/_noaudio.mp4 -i "+parent_path+"/test_output_audio.wav -c:v copy -c:a aac -strict experimental "+parent_path+"/output_"+lan+".mp4"
	subprocess.call(cmd1,shell=True)




#----------------------------------------------------------------

#def check_path(input_path,lan):
def check_path():
	
	print(input_path)
	if input_path =="":
		msg = "Please Select a Video"
		print("----------in check if")
	else:
		print("----------in check else")
		video_translator(input_path,lan)
		msg = "Processing Video...."
		print("----------in check")


def c_open_file_old():
	global input_path
	rep = filedialog.askopenfilenames(
	parent=root,
	initialdir='/',
	initialfile='tmp',
	filetypes=[("MP4", "*.mp4")])
	input_path = rep[1]
	print(rep[1])




root = tk.Tk(className='GIYOL') 

root.geometry("500x200")

#set a window in center of page
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))


frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 

selVideobtn = Button(frame, text = 'Select a video', fg ='red',command =c_open_file_old) 
selVideobtn.grid(row=0, column=0,padx=20, pady=20, sticky='ew')


######Create a Drop down
# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Hindi','Gujrati'}
tkvar.set('Gujrati') # set the default option

popupMenu = OptionMenu(frame, tkvar, *choices)
Label(frame, text="Choose a language").grid(row = 1, column = 0)
popupMenu.grid(row = 2, column =0, padx=20, pady=10)

lan = 'gu'  #by default value for dropdown
# on change dropdown value
def change_dropdown(*args):
	if tkvar.get()=='Gujrati':
		lan = 'gu'
	if tkvar.get()=='Hindi':
		lan = 'hi'
	print( tkvar.get())

# link function to change dropdown
tkvar.trace('w', change_dropdown) 



submitbtn = Button(frame, text ='Submit', fg ='green',command = check_path) 
submitbtn.grid(row=3, column=0) 



root.mainloop() 


