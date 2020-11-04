try:
	from tkinter import *
	import time
	import pyttsx3
	from tkinter import messagebox
	from langdetect import detect
	from googletrans import Translator
	translator = Translator()
	import speech_recognition as sr
except ModuleNotFoundError as e:
    print(e)	
    exit()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?",icon="warning"):
        root.destroy()

r = sr.Recognizer()
def record():
	try:
		with sr.Microphone() as source2:
			r.adjust_for_ambient_noise(source2, duration=0.2)  
			print("Talk")
			audio2 = r.listen(source2)
			print("Time over, thanks")
	
			MyText = r.recognize_google(audio2) 
			MyText = MyText.lower() 
	
			print("Did you say "+MyText) 
			Fact = MyText
			scrollbar = Scrollbar(root)
			scrollbar.pack(side=RIGHT, fill=Y)
			T = Text(root, height = 14, width = 43)
			T.config(yscrollcommand=scrollbar.set)
			scrollbar.config(command=T.yview) 
			T.pack() 
			T.insert(INSERT, MyText)

			button = Button(root, text = "Clear", 
					width = "15", pady = 2, 
					font = "bold, 15", 
					command = T.destroy, bg='orange') 
			button.place(x = 250,  
        				 y = 0) 
	
	except:
		print("error")	
			
		


def speechtotext():
	halfwin2.destroy()
	halfwin.destroy()
	btnchange.destroy()
	

	halfwin3 = Frame(root, 

				bg = "lightPink",
				height = "190") 
	halfwin3.pack(fill = X) 
	label = Label(halfwin3, text = "speech to Text", 
			font = "bold, 30",) 
	label.place(x = 180, y = 70) 
	halfwin4 = Frame(root, 
				bg = "yellow", 
				height = "750") 
	halfwin4.pack(fill=X) 
	messagebox.showinfo("showinfo", "Plz preass clear after recording the 1st time[if want to record again]") 
  	
	btn = Button(halfwin4, text = 'Voice!!', bd = '60',
					command = record)
	btn.pack(side = 'bottom')
	
root = Tk() 
root.resizable(0, 0) 
	
btnchange = Button(text = "Speech to Text", 
			width = "15", pady = 10, 
			font = "bold, 8", 
			command = speechtotext,bg='orange') 
btnchange.pack(side = 'top')

halfwin = Frame(root, 
			bg = "lightPink", 
			height = "150") 

halfwin.pack(fill = X) 
			
halfwin2 = Frame(root, 
			bg = "yellow", 
			height = "750") 
halfwin2.pack(fill=X) 

label = Label(halfwin, text = "Text to Speech", 
			font = "bold, 30",) 
		
	
label.place(x = 180, y = 70) 

label = Label(halfwin, text = "Any Languaget to English and speak", 
			font = "bold, 7",) 
			
		
label.place(x = 18, y = 125) 
label = Label(halfwin, text = "Made by Harsh", 
			font = "bold, 7",) 
		

label.place(x = 450, y = 45) 

harsh = Entry(halfwin2, width = 55, 
			bd = 10, font = ("Times New Roman", 12, "bold")) 
harsh.place(x = 130, y = 52,width=400,height=60,) 
harsh.insert(0, "") 
 
def mainfu(): 
	try:
		check = harsh.get()
		h=detect(check)
		if h != 'en':
			print("not eng...coverting\nit is",h,"for more info about List of ISO 639-1 codes... go to https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes ")
     
			translatedd = translator.translate(check)
			engine = pyttsx3.init()
			engine.say(translatedd.text)
			engine.runAndWait()
	    
	
		else:
        		engine = pyttsx3.init()
        		engine.say(harsh.get())
        		engine.runAndWait()
        		print(harsh.get())
	except:
		print("Try again i was starting up")
	    
	
	
button = Button(halfwin2, text = "Continue", 
			width = "15", pady = 10, 
			font = "bold, 15", 
	
			command = mainfu, bg='orange') 
button.place(x = 250,  
         y = 130) 
		
 
root.title("text to speech by Harsh") 

h = 550
w = 700
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop() 



