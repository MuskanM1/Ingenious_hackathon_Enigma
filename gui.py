'''
#only button click
import Tkinter as tk
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack() 
r.mainloop() 
'''

'''
#open file browser

import os
import Tkinter as tk
import ttk
import tkFileDialog as filedialog

root = tk.Tk()

style = ttk.Style(root)
style.theme_use("clam")
	

def c_open_file_old():
	rep = filedialog.askopenfilenames(
	parent=root,
	initialdir='/',
	initialfile='tmp',
	filetypes=[("MP4", "*.mp4")])
	print(rep[1])
	
	#try:
	#	os.startfile(rep[1])
	#except IndexError:
	#	print("No file selected")
	

ttk.Button(root, text="Open files", command=c_open_file_old).grid(row=1, column=0, padx=4, pady=4, sticky='ew')

root.mainloop()
'''

#play a video in gui


#to install gst(GStreamer)
#sudo apt-get install -y python-gobject
import os
import sys
import Tkinter as tkinter

import gobject
import Gst

def on_sync_message(bus, message, window_id):
	if not message.structure is None:
		if message.structure.get_name() == 'prepare-xwindow-id':
			image_sink = message.src
			image_sink.set_property('force-aspect-ratio', True)
			image_sink.set_xwindow_id(window_id)

gobject.threads_init()

window = tkinter.Tk()
window.geometry('500x400')

video = tkinter.Frame(window, bg='#000000')
video.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)

window_id = video.winfo_id()

player = gst.element_factory_make('playbin2', 'player')
player.set_property('output', None)
player.set_property('uri', 'file://%s' % (os.path.abspath(sys.argv[1])))
player.set_state(gst.STATE_PLAYING)

bus = player.get_bus()
bus.add_signal_watch()
bus.enable_sync_message_emission()
bus.connect('sync-message::element', on_sync_message, window_id)

window.mainloop()



