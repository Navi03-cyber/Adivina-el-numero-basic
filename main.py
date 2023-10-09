#Importamos la librería random
import random
#asignamos "false" a la variable adivinado para controlar el while
adivinado=False
#generamos el aleatorio, ENTRE EL 1 Y EL 10
numero_aleatorio=random.randint(1, 10)
#el bucle se repetira mientras adivinado sea false
while(adivinado==False):
    #se le pregunta al usuario el numero, guardandose en la variable respuesta
    respuesta=int(input("Cual numero crees que estoy pensando?"))
    
    if(respuesta == numero_aleatorio):#Si respuesta tiene el mismo numero que nuestro aleatorio el usuario ha ganado
        
        print("genial me has pillado, el numero era " + str(numero_aleatorio))#str()sirve para convertir el dato int a string
        adivinado=True
    
    else:

        print("vamos a probar de nuevo")#si no, el bucle sigue hasta que se adivine ya que adivinado sigue en false
        
