#include <iarduino_DHT.h>

iarduino_DHT sensor(2);

void setup() {
  Serial.begin(9600);
  delay(1000);
}

void send_sensor_data() {
  switch (sensor.read()) {
    Serial.print("CEHCOP B KOMHATE: ");
    case DHT_OK:
      Serial.println((String)sensor.hum + "% - " + sensor.tem + "°C");
      break;
    case DHT_ERROR_CHECKSUM:
      Serial.println("HE PABEHCTBO KC");
      break;
    case DHT_ERROR_DATA:
      Serial.println("OTBET HE СООТВЕТСТВУЕТ CEHCOPAM 'DHT'");
      break;
    case DHT_ERROR_NO_REPLY:
      Serial.println("HET OTBETA");
      break;
    default:
      Serial.println("ERROR");
      break;
  }
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readString();
    input.trim();
    if (input == "request_information") {
      send_sensor_data();
    }
  }
  delay(2000);
}