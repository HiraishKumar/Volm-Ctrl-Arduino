import serial
import threading
from AudioCtrl import AudioController
    
def find_port(COMPORT=None):
    '''Finds the COMPORT connecting to the arduino. if this dosent work, try manually placing a value in the config file   '''
    # Get a list of all available serial ports.
    if COMPORT:
        return COMPORT
    ports = serial.tools.list_ports.comports()
    try:
        for port in ports:
            if port.description.find("CH340") != -1 or port.description.find("Arduino") != -1:
                # print(f"the port connected to {port.device}")                                     #debug
                return port.device
    except:
        raise KeyError("The Port was Not Found, Try manually configuring a port the config file ")
        
def startReading(function):
    '''starts a thread separate to mainloop from tkinter for reading the serial data function'''
    thread =threading.Thread(target=function)
    thread.daemon=True
    thread.start()


def Mix(Aud_Ctrl_PROCESSES:list[AudioController],volumes:list[int])->None:
    '''mixer Function that changes the volume of processes based on the array, [volumes], made of int values between 0 and 100'''
    for i in range (len(Aud_Ctrl_PROCESSES)):
        actual_volume = float(volumes[i]/100)
        Aud_Ctrl_PROCESSES[i].set_volume(actual_volume)
