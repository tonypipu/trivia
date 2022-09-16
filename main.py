import os
import time 
import random

def pantalla():
  print("****************************************")
  print("*                                      *")
  print("*    ¡Bienvenidos a mi Trivia!         *")
  print("*                                      *")
  print("****************************************")
  time.sleep(2)
  os.system ("clear")
  print('Trivia de preguntas random de futbol')
pantalla()

def preguntas():
  #lista de pregunta
  
  lpreguntas=list()
  lpreguntas=['¿cuantos equipos jugaran el mundial?',' ¿Cuantos balones de oro tiene messi ?',' ¿Que edad tiene Cristiano ronaldo ?',' ¿Cuantos balones de oro tiene Cristiano ronaldo?',' ¿Cuantas champions tiene el real madrid?',' ¿Cuantos mundiales tiene brazil?']

  #lista de respuestas
  lrespuestas=list()
  lrespuestas=[32,7,37,5,13,5]
  
  
  npre = random.randint(0, 5)
  pre=lpreguntas[int(npre)]
  x=input(pre+' :')
  if int(x)==lrespuestas[int(npre)] :
    print('correcto')
    preguntas()
    
  else:
    print('Incorrecto')
    print('Termino el juego')
  
  #if(list(pre))

preguntas()


   
  