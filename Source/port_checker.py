# import serial.tools.list_ports
# import serial.tools.miniterm

# def main():
#     # Get a list of serial port names.
#     ports = serial.tools.list_ports.comports()
#     test = serial.tools.list_ports.

#     print("The following serial ports were found:")

#     # Display each port name to the console.
#     for port in ports:
#         print(port.device)

# if __name__ == "__main__":
#     main()

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################

import serial.tools.list_ports
import threading
from pycaw.pycaw import AudioUtilities
import serial



def find_port():
    # Get a list of all available serial ports.
    ports = serial.tools.list_ports.comports()

    # print("The following serial ports were found:")
    for port in ports:
        if port.description.find("CH340") != -1 or port.description.find("Arduino") != -1:
            # print(f"Device: {port.device}, Description: {port.description}")
            print(f"the port connected to {port.device}")
            return port.device

def readSerial(ser,serials,sliders,process_name,audio_controller):
    print("Started Logging")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            test = [int(i)//10 if 0 <= int(i) < 1000 else 100 for i in line.split("|")]
            # print(test)
            new_volume = float(test[0]/100 )
            audio_controller.set_volume(new_volume)
            print(f"New volume for {process_name} set to {new_volume}")
            for num,item in enumerate(serials):
                item.set(test[num])
            
            for num,item in enumerate(sliders):
                item.set(value=test[num])

def startReading():
    thread =threading.Thread(target=readSerial)
    thread.daemon=True
    thread.start()
               