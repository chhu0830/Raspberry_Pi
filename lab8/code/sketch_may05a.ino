// Example testing sketch for various DHT humidity/temperature sensors
// Written by ladyada, public domain

#include "DHT.h"
#include <Wire.h>

#define DHTPIN 7     // what pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302)
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

// Communicate RPi through I2C
int SLAVE_ADDRESS = 0x04;
int ledPin = 13;
int analogPin = A0;
boolean ledOn = false;
int sw = 0;
float h, t;
int m;


void setup() {
  pinMode(ledPin, OUTPUT);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(processMessage);
  Wire.onRequest(sendAnalogReading);
  Serial.begin(9600);
  Serial.println("DHTxx test!");

  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  t = dht.readTemperature();

  m = analogRead(A0);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temp: ");
  Serial.print(t);
  Serial.print(", ");
  Serial.print("Humi: ");
  Serial.print(h);
  Serial.print(", ");
  Serial.print("Mois: ");
  Serial.print(m);
  Serial.println();
}

void processMessage(int n) {
  Serial.println("In processMessage");
  char ch = Wire.read();
  if (ch == 'l') {
    toggleLED(true);
  }
  else {
    toggleLED(false);
  }
}

void toggleLED(boolean ledSw) {
  digitalWrite(ledPin, ledSw);
}

void sendAnalogReading() {
  Serial.println("In sendAnalogReading");
  delay(2000);
  float msg;
  switch(sw) {
    case 0:
      msg = t;
      break;
    case 1:
      msg = h;
      break;
    case 2:
      msg = float(m);
      break;
  }
  Wire.write(byte(msg));
  sw = (sw + 1) % 3;
}

