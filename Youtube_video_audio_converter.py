#pip install youtube_dl
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# define create widgets functions to create necessary tkinter widgets
def CreateWidgets():
    linkLabel = Label(root, text=" Youtube link :", bg="turquoise4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable=videoLink)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    destinationLabel = Label(root, text="Destination :", bg="turquoise4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=38, textvariable=downloadPath)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)

    browseButton = Button(root, text="Browse :", command=Browse, width=15)
    browseButton.grid(row=2, column=2, pady=5, padx=5)

    downloadButton = Button(root, text="Download Audio :", command=Download, width=20)
    downloadButton.grid(row=3, column=1, pady=5, padx=5)

    downloadVideo = Button (root, text= "Download Video:", command= Download_Video, width= 20)
    downloadVideo.grid(row=3, column= 2, pady=5, padx=5)    

#Define Browse function to select a destination folder to save the audio fiole
def Browse():
    #pop directory to choose destination folder
    downloadDirectory = filedialog.askdirectory(initialdir="/Users")
    downloadPath.set(downloadDirectory)

# define download function to download video as audio file
def Download_Video():
    youtube_link = videoLink.get()
    downloadFolder = downloadPath.get()
    video_Download_options = {
        # video format {best, worst, better} / audio formats
        'format':'bestvideo+bestaudio/best',
        'outtmpl':downloadFolder+"/%(title)s.%(ext)s",
        # Amount of time to retry a download not working in the meantime throwing up an error.
        # 'retries': 'infinite',
        # "progress_hooks": [Log.my_hook]
       
        #creating a playlist or not
        # noplaylist':True,
        # whether to extract the audio or not
        # 'extract-audio':True,
        #include subtitles if u want to include
        'sub-format':'ass/srt/best',
        'preferredcodec':'mkv',
        # Naming style of the video
        'metadatafromtitle': '%(artist)s - %(title)s',
        #'preferredquality':'720'
    }  
    #video file  download using the youtubedl.download[] whereby the link is the argument. 
    with youtube_dl.YoutubeDL(video_Download_options) as video_download:
        video_download.download([youtube_link])
    # Success message display
    messagebox.showinfo("Success", "video downloaded successfully")

def Download():
    #fetch user input youtube link and store it in yt_link variable
    yt_link = videoLink.get()
    
    #fetch destination directory and storing it in downloadfolder variables
    downloadFolder = downloadPath.get()

    #configurations options for downloading the file
    audio_Download_options = {
        #specify to download audio in best format
        'format':'bestaudio/best',
        #destination to save the audio file with the title as the name
        'outtmpl':downloadFolder+"/%(title)s.%(ext)s",

        #video to audio conversion
        'postprocessors': [{
            #audio from video extraction
            'key': 'FFmpegExtractAudio',
            #audio saving format(mps,wav)
            'preferredcodec':'mp3',
            #audio quality always measured in bitrate format (320, 280)
            'preferredquality': '320'
        }],
    }

    #audio file  download using the youtubedl.download[] whereby the link is the argument. 
    with youtube_dl.YoutubeDL(audio_Download_options) as audio_download:
        audio_download.download([yt_link])

    #Success message display
    messagebox.showinfo("Success", "video converted to audio successfully")


# an object of the tk class
root = tk.Tk()

# The title, background color and size of the tkinter window and disablement of the
# resizing property
root.geometry("650x120")
root.resizable(False, False)
root.title("Youtube_Video_Audio_Downloader")
root.config(background="turquoise4")

# The tkinter Variables
videoLink = StringVar()
downloadPath = StringVar()

# CreateWidgets() function
CreateWidgets()

# An infinite loop to coorditionally run the application
root.mainloop()




