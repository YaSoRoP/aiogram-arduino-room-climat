#include <iarduino_DHT.h>

iarduino_DHT sensor(2);

void setup() {
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  switch(sensor.read()) {
    case DHT_OK:
      Serial.println((String) sensor.hum + "% - " + sensor.tem + "°C");
      break;
    case DHT_ERROR_CHECKSUM:
      Serial.println("HE PABEHCTBO KC");
      break;
    case DHT_ERROR_DATA:
      Serial.println("OTBET HE COOTBETCTBЕТСТВУЕТ CEHCOPAM 'DHT'");
      break;
    case DHT_ERROR_NO_REPLY:
      Serial.println("HET OTBETA");
      break;
    default:
      Serial.println("ERROR");
      break;
  }
  delay(1500);
}