#include<Servo.h>
const int pingPin = 7;
int servoPin = 8;

Servo servo1;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  servo1.attach(servoPin);
  pinMode(9,OUTPUT);
  pinMode(A0,INPUT);
  digitalWrite(9,LOW);
    
}

void loop() {
  
  long duration, inches, cm;

  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);

  // convert the time into a distance
  inches = microsecondsToInches(duration);
  cm = microsecondsToCentimeters(duration);
  
  Serial.println("distance");
  Serial.println(cm);
  
    
  servo1.write(0);
  
  if(cm < 30)
  {
    servo1.write(90);
    delay(2000);
  }
  else
  {
    servo1.write(0);
  }
  
   
  //temp with buzzer
  float value=analogRead(A0);
  float temperature=value*0.48;
  
  Serial.println("temperature");
  Serial.println(temperature);
  
  if(temperature > 28)
  {
    digitalWrite(9,HIGH);
  }
  else
  {
    digitalWrite(9,LOW);
  }
}

long microsecondsToInches(long microseconds) {
  return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}