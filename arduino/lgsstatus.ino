void setup(){
  Serial.begin(9600);
}

float temp = 0; int hell = 0; int i = 0;


void loop(){
  if(Serial.available()>0){
    while(i < 10){
      temp += analogRead(4)*0.004882812*100-273.15;
      hell += analogRead(0);
      i++;
    }
    temp /= 10;
    hell /= 10;
    
    Serial.print(int(temp));
    Serial.print(",");
    Serial.print(hell);
    Serial.println();
    Serial.read();
  }
  
}
