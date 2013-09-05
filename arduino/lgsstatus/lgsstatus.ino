/*
Berechnung für die Temperatur:
Temperatur = Input*(5V/1023)/(10mV/K)-273,15
*/


#include<Arduino.h>

void setup() {
    Serial.begin(9600);
}

float temp = .0;
int lumen = 0;

void loop() {
    temp = analogRead(4) * 0.00488759 * 100 - 273.15;
    lumen = analogRead(0);
    Serial.print(temp);
    Serial.print("|");
    Serial.print(lumen);
    Serial.println();
    delay(10);
}
