from tkinter import *
from tkinter import messagebox
from pytube import YouTube


root=Tk()
root.title("VidPy")
root.minsize(width=300,height=450)
# root.maxsize(width=644,height=850)


def download(event):
	url=urlvalue.get()
	yobj=YouTube(url)
	ch = messagebox.askyesno("Video Title",f"Download\n{yobj.title}")
	if ch==True:
		quality=strm.get()
		qual=yobj.streams.all()
		vid=list(enumerate(qual))
		qual[quality].download()
	else:
		import sys
		sys.exit()
	
		
intro=Label(text="VidPy",font="lucida 12 bold",fg="white",bg="blue",borderwidth=12,relief="ridge",padx=30,pady=15)
intro.pack(pady=20)

Label(text="Paste URL of video, \nwhich you wan't to download\n↓",font="comicsansms 8 italic bold",fg="brown",bg="pink").pack()

urlvalue=StringVar()

urlentry=Entry(root,textvariable=urlvalue,font="comicsansms 13 italic")
urlentry.pack(pady=8)

strm=IntVar()

Label(text="» Select Video Quality «",font="comicsansms 8 italic bold",fg="blue").pack(pady=20)

radio=Radiobutton(root,text="144p",value=0,variable=strm,fg="black",bg="pink")
radio.pack(anchor="w")
radio=Radiobutton(root,text="360p",value=1,variable=strm,fg="blue",bg="yellow")
radio.pack(anchor="w")
radio=Radiobutton(root,text="720p",value=2,variable=strm,fg="green",bg="skyblue")
radio.pack(anchor="w")

#Label(text="» Click on download",font="comicsansms 8 italic bold").pack(pady=20)

button=Button(root,text="Download",fg="white",bg="green",borderwidth=5,relief="sunken",font="lucida 8 bold")
button.pack(pady=20)
button.bind("<Button-1>",download)

Button(root,text="Exit",command=quit,bg="red",fg="white",font="comicsansms 7 bold",relief="groove",borderwidth=5).pack(pady=20)

root.mainloop()