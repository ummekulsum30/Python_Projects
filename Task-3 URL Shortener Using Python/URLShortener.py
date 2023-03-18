from tkinter import *
import pyshorteners
 # Function for shortening the URL and to set value in textbox
def convert():                                                                                   
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
root = Tk()
root.title(" URL Shortener")
root.geometry("400x370")
root.resizable(False, False)
root.config(background="#FFBBFF")
# Declare variables
url = StringVar()                                                                                  
shorturl = StringVar()
# Design labels
Label(root, text="URL Shortener", bg="#FFBBFF", fg="#1E1E1E", font="Arial 24 ").place(x=80, y=10)
Label(root, text="-------------------------------------------------", bg="#FFBBFF", fg="#1E1E1E",
       font="verdana 12 ").place(x=15, y=50)
  # Accepting URL as a Input
Label(root, text="Enter your URL:", bg="#000080", fg="#EAECEE", font="Times 15 bold"
            , padx=2, pady=2).place(x=7, y=90)
Entry(root, textvariable=url, font="verdana 14", width=27).place(x=7, y=120)
# Creating button to give a call for convert function
Button(root, text="Shorten", bg="#FFF68F", fg="#000", font="Arial 14 "
        , command=convert, relief=GROOVE).place(x=140, y=180)
# Displaying shortened URL
Label(root, text="Shortened URL:", bg="#000080", fg="#EAECEE"
            , font="Times 15 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=27, font="verdana 14").place(x=7, y=280)
Label(root, text="Copy & Paste in Browser.", bg="#FFBBFF", fg="#1E1E1E", font="Arial 10 " ).place(x=8, y=310)
root.mainloop()