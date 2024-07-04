// This application uses code adapted from the original work by Omri Harel
// Copyright (c) 2020 Omri Harel
// Licensed under the MIT License (https://opensource.org/licenses/MIT)


const int NUM_SLIDERS = 5;
const int analogInputs[NUM_SLIDERS] = {A0, A1, A2, A3, A4};

int analogSliderValues[NUM_SLIDERS];
int PrevanalogSliderValues[NUM_SLIDERS];

void setup() { 
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }

  Serial.begin(9600);
}

void loop() {
  updateSliderValues();
  sendSliderValues(); // Actually send data (all the time)
  // printSliderValues(); // For debug
  delay(10);
}

void updateSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
     analogSliderValues[i] = analogRead(analogInputs[i]);
  }
}

void sendSliderValues() {
  String builtString = String("");
  bool valuesChanged = false; // Flag to check if any value has changed

  // Check for changes in slider values
  for (int i = 0; i < NUM_SLIDERS; i++) {
    if ( abs(analogSliderValues[i] - PrevanalogSliderValues[i]) >= 5 ) {
      valuesChanged = true;
      break;
    }
  }
  if (valuesChanged){
    for (int i = 0; i < NUM_SLIDERS; i++) {
      builtString += String((int)analogSliderValues[i]);

      if (i < NUM_SLIDERS - 1) {
        builtString += String("|");
      }
    }
    for (int i = 0; i < NUM_SLIDERS; i++) {
      PrevanalogSliderValues[i] = analogSliderValues[i] ;
    }
  Serial.println(builtString);
  }
}

void printSliderValues() {
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