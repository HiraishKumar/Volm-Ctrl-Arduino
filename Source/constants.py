from yaml import load , Loader
from AudioCtrl import AudioController
document = load(open("config.yaml","r"),Loader=Loader)                                          #Load in the Config file as document


DEFAULT_ITEMS = ['master', 'firefox.exe', 'Spotify.exe', 'Discord.exe']

PROCESSES = [value for key,value in document["processes"].items() if value != None ] if "processes" in document and document["processes"] else DEFAULT_ITEMS

Aud_Ctrl_PROCESSES = [AudioController(process) for process in PROCESSES ] 
                           
BAUD_RATE = document["BAUD_RATE"] if "BAUD_RATE" in document and document["BAUD_RATE"] else 9600.

COMPORT = document["COMPORT"] if "COMPORT" in document and document["COMPORT"] else None

SLIDERS = document["SLIDERS"] if "SLIDERS" in document and document["SLIDERS"] else len(PROCESSES)