// This application uses code adapted from the original work by Omri Harel
// Copyright (c) 2020 Omri Harel
// Licensed under the MIT License (https://opensource.org/licenses/MIT)

const int NUM_SLIDERS = 5;                                    // set up the number of sliders that are to be used 
const int analogInputs[NUM_SLIDERS] = {A0, A1, A2, A3, A4};   // set up the associated analog pins on the arduino 
const int maxDiff = 5;                                        // set up the max change in analog input before the new value is sent to serial

int PrevanalogSliderValues[NUM_SLIDERS];                      // create an array to store the last sent value to compare with the latest value
int analogSliderValues[NUM_SLIDERS];                          // create an array to store the latest value of the analog input

void setup() { 
  for (int i = 0; i < NUM_SLIDERS; i++) {                     // setup the all the analogInputs in INPUT mode
    pinMode(analogInputs[i], INPUT);
  }
  Serial.begin(9600);                                         // setup the serial for comm with the computer
}

void loop() {
  updateSliderValues();
  sendSliderValues();                                         // Actually send data when difference between previous and latest reading is greater than maxDiff
  // printSliderValues();                                     // For debug
  delay(10);
}

void updateSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {                      
     analogSliderValues[i] = analogRead(analogInputs[i]);     // reads all the analog inputs and stores them in analogSliderValues
  }
}

void sendSliderValues() {
  String builtString = String("");
  bool valuesChanged = false;                                 // Flag to check if any value has changed

  // Check for changes in slider values
  for (int i = 0; i < NUM_SLIDERS; i++) {                     // Checks if the new value is greater than the previously sent value by maxDiff
    if ( abs(analogSliderValues[i] - PrevanalogSliderValues[i]) >= maxDiff ) {
      valuesChanged = true;                                   // if even a single value is changed the loop breaks and proceeds to sending the data
      break;
    }
  }
  if (valuesChanged){                                         // checks if the values have changed
    for (int i = 0; i < NUM_SLIDERS; i++) {                   // builds the string that is to be sent
      builtString += String((int)analogSliderValues[i]);

      if (i < NUM_SLIDERS - 1) {
        builtString += String("|");
      }
    }
    for (int i = 0; i < NUM_SLIDERS; i++) {                   // updates PrevanalogSliderValues with analogSliderValues
      PrevanalogSliderValues[i] = analogSliderValues[i] ;
    }
  Serial.println(builtString);                                // send the string 
  }
}

void printSliderValues() {                                    //debugging function to print the slider value in arduino IDE terminal
  for (int i = 0; i < NUM_SLIDERS; i++) {
    String printedString = String("Slider #") + String(i + 1) + String(": ") + String(analogSliderValues[i]) + String(" mV");
    Serial.write(printedString.c_str());

    if (i < NUM_SLIDERS - 1) {
      Serial.write(" | ");
    } else {
      Serial.write("\n");
    }
  }
}