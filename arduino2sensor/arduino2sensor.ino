/*
 * 
* By Ben Bament
* Multiple ultrasonic parking sensors. Based on:
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
* Crated by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/

// defines pins numbers
const int trigPin = 13;
const int echoPin = 12;
const int trigPin1 = 11;
const int echoPin1 = 10;

// defines variables
long duration;
long duration1;
int distance;
int distance1;

void setup() {
pinMode(trigPin, OUTPUT);// Sets the trigPin as an Output
pinMode(trigPin1, OUTPUT);
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(echoPin1, INPUT);
Serial.begin(9600); // Starts the serial communication
}

void loop() {
// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;

// Clears the trigPin
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration1 = pulseIn(echoPin1, HIGH);

// Calculating the distance
distance1= duration1*0.034/2;

// Prints the distance on the Serial Monitor
Serial.print("Distance sensor 1: ");
Serial.println(distance);
Serial.print("Distance sensor 2: ");
Serial.println(distance1);
}
