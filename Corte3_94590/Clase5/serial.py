import serial     #instalar dicha libreria
                  #cmd=> -m pip install pyserial
import time

puerto=serial.Serial('COM1',baudrate=9600,timeout=3)
while 1:
    dato=input('Ingrese un valor: ')
    puerto.write(dato.encode('utf-8'))
    line=puerto.readline().decode('ascii')
    if str(line).rstrip('\r\n')=='Dato incorrecto':
        print('Error en los datos')
        break
    print(str(line).rstrip('\r\n'))
    time.sleep(0.3)

'''
//---------Codigo de arduino----------
long randomNumber;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, LOW);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0) {
    char incoming = Serial.read();
    if (incoming == 'y') {
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      randomNumber=random(0,100);
      Serial.println(randomNumber);
      delay(200);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(200);                       // wait for a second
    }else{
      Serial.println("Dato incorrecto");
    }
  }
}'''
  

    
