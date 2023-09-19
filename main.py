#Proyecto 2 Bola Mágica 8 en CodeCademy

import random

#Declaro las Variables
nombre = "Guille"
pregunta = "Como te ves en el Futuro ? "
respuesta = ""

#Declaro la Funcion Random Number
numero_random = random.randint(1, 15)

#Llamo a la Funcion
print(numero_random)

#Declaro Condicionales
if numero_random == 1:
  respuesta = "Hombre poderoso"
elif numero_random == 2:
  respuesta = "Buena salud"
elif numero_random == 3:
  respuesta = "Rico"
elif numero_random == 4:
  respuesta = "Gana un Premio Nobel"
elif numero_random == 5:
  respuesta = "Viaja a Europa"
elif numero_random == 6:
  respuesta = "Mucho Trabajo"
elif numero_random == 7:
  respuesta = "Su familia hereda una fortuna"
elif numero_random == 8:
  respuesta = "Descubre alguna cura"
elif numero_random == 9:
  respuesta = "Se convierte en Diputado"
elif numero_random == 10:
  respuesta = "Se convierte en Senador"
elif numero_random == 11:
  respuesta = "Se convierte en Presidente"
elif numero_random == 12:
  respuesta = "Gana una Batalla de Freestyle"
elif numero_random == 13:
  respuesta = "Es músico"
elif numero_random == 14:
  respuesta = "Se convierte en Streamer"
elif numero_random == 15:
  respuesta = "Gana la loteria"
else:
  respuesta = "Error"

#Imprimo por pantalla la Pregunta
print(nombre + " pregunta: " + pregunta)
#Imprimo por pantalla la Respuesta de la Bola Mágica 8
print("La Bola Mágica 8 te responde: " + respuesta)



