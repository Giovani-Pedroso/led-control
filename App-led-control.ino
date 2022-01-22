#define RED 3

String data;
bool ledState = false;
int incomingByte = 0;
void setup() {
  Serial.begin(9600);
  pinMode(3, OUTPUT);

}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
  }
}


/*
void loop() {
  if(Serial.available() > 0){
    data = Serial.readString();
    
    Serial.println(data);

    //if(data[0]='T'){
    //  ledState = !ledState;
    //  digitalWrite(RED, ledState);
    //}


  }
  Serial.println("olar");
  delay(600);
}*/
