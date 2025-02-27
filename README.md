# Volm-Ctrl-Arduino
This project is a Python application that requires installing dependencies listed in `requirements.txt` and then running `main.py`.
## Acknowledgments
This application includes code and schematics adapted from the original work by Omri Harel. The original code is licensed under the MIT License.

Orignal Creator -> [Deej](https://github.com/omriharel/deej)

## How it works
### Hardware 
- The Potentiometers are connected to 5 analog pins on an Arduino Nano/Uno  
board each for a separate input.
- They're powered from the board's 5V output from the arduino The board connects via a USB cable to the PC

![alt text](https://github.com/KillyDaviel/Volm-Ctrl-Arduino/blob/main/Assets/schematic.png)

## Software Requirements

- Python 3.x
- pip (Python package installer)

## Hardware Requirments
- An Arduino Nano, Pro Micro or Uno board 
- Slider 10K Ohm variable resistor potentiometers, up to your number of free analog pins
   - **Important**: make sure to get linear sliders, not logarithmic
- Breadboard and some wires 



## Installation On Desktop

1. Clone the repository:

    ```sh
    cd your-root
    git clone https://github.com/KillyDaviel/Volm-Ctrl-Arduino
    ```
2. Go Into SourceFile
    ```sh
    cd Source
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```
## Installation On Arduino 
Flash the Arduino Nano/Uno board with the `Arduino.ino` file inside `Volm-Ctrl-Arduino/Source/Arduino`.
The compilation can be done online on [Arduino's Webiste](https://app.arduino.cc/), or locally by downloading the Arduino IDE.

## Usage

Connect the Flashed Arduino to any USB port and then run the main script:

```sh
python main.py
```
