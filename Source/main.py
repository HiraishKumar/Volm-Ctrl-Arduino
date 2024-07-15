from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
from Source.funcs import Mix,find_port,startReading
from constants import Aud_Ctrl_PROCESSES,BAUD_RATE,COMPORT,SLIDERS


def readSerial():
    print("Started Logging")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            volumes = [int(i)//10 if 0 <= int(i) < 1000 else 100 for i in line.split("|")]
            Mix(Aud_Ctrl_PROCESSES,volumes)    
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
for _ in range(SLIDERS):
    serial_val = IntVar()
    serials.append(serial_val) 

for i in range(1,SLIDERS+1):
    serial_ = ttk.Entry(mainframe,textvariable=serials[i-1],state=DISABLED,width=5)
    serial_.grid(row=2, column=i,pady=10, sticky="")
    
    slider = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
    slider.grid(row=3, column=i)
    sliders.append(slider)
    
    mainframe.columnconfigure(i, weight=1)
    
    ttk.Label(mainframe, text=(f"SER{i}")).grid(row=1, column=i,pady=10, sticky="")
    
for child in mainframe.winfo_children():
    child.grid_configure(padx=20)

ser = serial.Serial(find_port(COMPORT),BAUD_RATE)

startReading(readSerial)

root.mainloop()


