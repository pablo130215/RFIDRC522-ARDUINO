//URL : https://www.youtube.com/watch?v=LvRfxGTUEpE

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);      // Initialize serial communications with the PC
  SPI.begin();             // Init SPI bus
  mfrc522.PCD_Init();      // Init MFRC522

}

void loop() {
  //Para escribir el uid de la tarjeta leida en la computadora
  escritura_serial();
  delay(5);
  //Para recibir información de la computadora al arduino
  String comando = lectura_serial();
  Serial.print(comando); 
  
}

void escritura_serial(){
    // put your main code here, to run repeatedly:
    // Look for new cards
    if ( ! mfrc522.PICC_IsNewCardPresent()) {
      return;
    }
  
    // Select one of the cards
    if ( ! mfrc522.PICC_ReadCardSerial()) {
      return;
    }
    //Serial.print("UID:");
    for(byte i=0; i<mfrc522.uid.size;i++){
     if(mfrc522.uid.uidByte[i] < 0x10){
        Serial.print("0"); 
     }
     Serial.print(mfrc522.uid.uidByte[i],HEX);
    }
    Serial.println();
    mfrc522.PICC_HaltA();
}

String lectura_serial(){
   String cadena_leida;
   char caracter_leido;
    while(!Serial.available()==0){
      caracter_leido = Serial.read();
      cadena_leida += caracter_leido;
      delay(5);
    }
    return cadena_leida;
}
