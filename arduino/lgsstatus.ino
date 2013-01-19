#include<Arduino.h>

void setup() {
    Serial.begin(9600);
}

float temp[] = {0, 0, 0, 0, 0, 0};
int hell = 0;
int i = 0;
int n = 0;
int l =0;


void loop() {

    if(Serial.available()>0) {
        if(n > 4)
        {
            n = 0;
            l = 1;
        }
        while(i < 10) {
            temp[n] += analogRead(4)*0.004882812*100-273.15;
            hell += analogRead(0);
            delay(10);
            i++;
        }
        temp[n] /= 10;
        hell /= 10;
        if(l == 1) {
            temp[5] = temp[0] + temp[1] + temp[2] + temp[3] + temp[4];
            temp[5] /= 5;
        }
        else {
            temp[5] = temp[n];
        }
        Serial.print(int(temp[5]));
        Serial.print(",");
        Serial.print(hell);
        Serial.println();
        Serial.read();
        n++;
    }

}
