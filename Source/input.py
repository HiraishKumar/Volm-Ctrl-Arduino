from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL     
from pycaw.pycaw import AudioUtilities ,IAudioEndpointVolume

import math

def set_volume_master(level):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(math.log10(level * 9 + 1) / 1, None)
    except:
        None

class AudioController:
    def __init__(self, process_name):
        self.process_name = process_name
        self.volume = self.process_volume()
        self.interface = None
    
    def process_volume(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                print("Volume:", interface.GetMasterVolume())  # debug
                return interface.GetMasterVolume()
    
    def set_volume(self, volume_linear):
        sessions = AudioUtilities.GetAllSessions()
        volume_log = self.linear_to_logarithmic(volume_linear)
        
        if self.interface is None:
            for session in sessions:
                interface = session.SimpleAudioVolume
                if session.Process and session.Process.name() == self.process_name:
                    self.interface = session
                    interface.SetMasterVolume(volume_log, None)
                    print("Volume set to", volume_log)
        else:
            interface = self.interface.SimpleAudioVolume
            interface.SetMasterVolume(volume_log, None)
            print("Volume set to", volume_log)       


    def linear_to_logarithmic(self, volume_linear):
        # Convert linear volume to logarithmic scale
        # Ensure volume is between 0.0 and 1.0
        volume_linear = min(1.0, max(0.0, volume_linear))
        # Convert linear scale (0.0 to 1.0) to logarithmic scale
        # We use a log base 10 here, but other bases could be used
        return math.log10(volume_linear * 9 + 1) / 1  # maps 0.0-1.0 to 0.0-1.0 logarithmically

if __name__ == "__main__":
    process_name = "firefox.exe"  # Replace with the name of the process you want to control
    audio_controller = AudioController(process_name)
    
    # Get current volume
    current_volume = audio_controller.process_volume()
    print(f"Current volume for {process_name}: {current_volume}")
    
    # Set new volume
    new_volume = float(input("enter new volume:"))  # Set desired volume level (0.0 to 1.0) in linear scale
    audio_controller.set_volume(new_volume)
    print(f"New volume for {process_name} set to {new_volume}")
