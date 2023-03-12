from tkinter import *  
import datetime as dt  
import time  
import winsound as ws  
  
# function for alarm clock
def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            ws.PlaySound("sound.wav", ws.SND_ASYNC)  
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime)  
  
# GUI for the application  
guiWindow = Tk()  
guiWindow.title("The Alarm Clock")  
guiWindow.geometry("500x250")  
guiWindow.config(bg = "darkseagreen1")  
guiWindow.resizable(width = False, height = False)  
   
timeFormat = Label(  
    guiWindow,  
    text = "Set time in 24-hour format!",  
    fg = "white",  
    bg = "darkseagreen4",  
    font = ("Arial", 15)  
    ).place(  
        x = 0,  
        y = 160  
        )  
   
add_time = Label(  
    guiWindow,  
    text = "Hour     Minute     Second",  
    font = 60,  
    fg = "white",  
    bg = "midnightblue"  
    ).place(  
        x = 220,  
        y = 10  
        )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "midnightblue",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 10,  
        y = 50  
        )  
   
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
   
hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 220,  
        y = 53  
        )  
minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 53  
        )  
secondTime = Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 53  
        )  
   
submit = Button(  
    guiWindow,  
    text = "Set Alarm",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 246,  
        y = 100  
        )  
   
guiWindow.mainloop()  