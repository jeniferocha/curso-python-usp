carga = int(input())     

while True:  
    if carga <= 5:
      print("recarregar: ",carga) 
      break
    sensor1 = str(input())
    sensor2 = str(input())
    if sensor1 == "L" and sensor2 == "A":
        carga -= 5
        print("virar:" ,carga)
    elif sensor1 == "L":
        carga -= 1
        print("avançar:" ,carga)
    elif sensor1 == "B":
        carga -= 5
        print("virar:" ,carga)