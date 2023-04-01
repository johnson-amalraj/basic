#Rocket Animation - www.101computing.net/text-based-animations/
import os
import time

def animate_Rocket():
  distanceFromTop = 20
  while True:
    print("\n" * distanceFromTop)
    print("          /\        ")
    print("          ||        ")
    print("          ||        ")
    print("         /||\        ")
    time.sleep(0.2)
    os.system('clear')  
    distanceFromTop -= 1
    if distanceFromTop <0:
      distanceFromTop = 20
  
  
#Main Program Starts Here....
animate_Rocket()
