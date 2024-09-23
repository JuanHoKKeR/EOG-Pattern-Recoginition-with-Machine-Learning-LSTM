// void setup() {
//   Serial.begin(115200);
// }

// void loop() {
//   // Lee el valor analógico en el pin GPIO 2
//   float valorPin2 = analogRead(2);
//   // Convierte el valor a voltaje (suponiendo una referencia de 3.3V)
//   float voltajePin2 = (valorPin2 / 4095.0) * 3.3;

//   // Lee el valor analógico en el pin GPIO 15
//   float valorPin15 = analogRead(15);
//   // Convierte el valor a voltaje (suponiendo una referencia de 3.3V)
//   float voltajePin15 = (valorPin15 / 4095.0) * 3.3;

//   // Muestra los voltajes en el monitor serial
//   Serial.print(voltajePin2);Serial.print(",");Serial.println(voltajePin15);
//  delay(5);

// }

#define TAMANO_VENTANA 5

float bufferPin2[TAMANO_VENTANA];
float bufferPin15[TAMANO_VENTANA];
int indice = 0;

void setup() {
  Serial.begin(115200);
  // Inicializa los buffers
  for(int i = 0; i < TAMANO_VENTANA; i++) {
    bufferPin2[i] = 0.0;
    bufferPin15[i] = 0.0;
  }
}

void loop() {
  // Lee los valores analógicos
  float valorPin2 = analogRead(2);
  float valorPin15 = analogRead(15);

  // Agrega los valores al buffer, sobrescribiendo los más antiguos
  bufferPin2[indice] = valorPin2;
  bufferPin15[indice] = valorPin15;

  // Calcula la media móvil
  float promedioPin2 = 0.0;
  float promedioPin15 = 0.0;
  for(int i = 0; i < TAMANO_VENTANA; i++) {
    promedioPin2 += bufferPin2[i];
    promedioPin15 += bufferPin15[i];
  }
  promedioPin2 /= TAMANO_VENTANA;
  promedioPin15 /= TAMANO_VENTANA;

  // Convierte el promedio a voltaje
  float voltajePin2 = (promedioPin2 / 4095.0) * 3.3;
  float voltajePin15 = (promedioPin15 / 4095.0) * 3.3;

  // Muestra los voltajes en el monitor serial
  Serial.print(voltajePin2); Serial.print(", "); Serial.println(voltajePin15);

  // Actualiza el índice para la próxima lectura
  indice = (indice + 1) % TAMANO_VENTANA;

  delay(5);
}