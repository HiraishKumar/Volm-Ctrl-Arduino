from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
from input import AudioController,Mix,find_port,startReading
from yaml import load , Loader


document = load(open("config.yaml","r"),Loader=Loader)
DEFAULT_ITEMS = ['master', 'firefox.exe', 'Spotify.exe', 'Discord.exe']
PROCESSES = [value for key,value in document["processes"].items() if value != None ] if "processes" in document and document["processes"] else DEFAULT_ITEMS
BAUD_RATE = document["BAUD_RATE"] if "BAUD_RATE" in document and document["BAUD_RATE"] else 9600


def readSerial():
    print("Started Logging")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            volumes = [int(i)//10 if 0 <= int(i) < 1000 else 100 for i in line.split("|")]
            Mix(PROCESSES,volumes)    
            for num,item in enumerate(serials):
                item.set(volumes[num])          
                
            for num,item in enumerate(sliders):
                item.set(value=volumes[num])
               
root = Tk()
root.title("Serial Reader")
root.geometry("500x500")

mainframe = ttk.Frame(root,padding=("3 3 12 12"))
mainframe.grid(row=1,column=1,sticky="nsew")

root.columnconfigure(1,weight=1)
root.rowconfigure(1,weight=1)

serials =[]
sliders = []
for _ in range(5):
    serial_val = IntVar()
    serials.append(serial_val) 

for i in range(1,6):
    serial_ = ttk.Entry(mainframe,textvariable=serials[i-1],state=DISABLED,width=5)
    serial_.grid(row=2, column=i,pady=10, sticky="")
    
    slider = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
    slider.grid(row=3, column=i)
    sliders.append(slider)
    
    mainframe.columnconfigure(i, weight=1)
    
    ttk.Label(mainframe, text=(f"SER{i}")).grid(row=1, column=i,pady=10, sticky="")
    
for child in mainframe.winfo_children():
    child.grid_configure(padx=20)

ser = serial.Serial(find_port(),BAUD_RATE)

startReading(readSerial)

root.mainloop()


