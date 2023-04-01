#Lighthouse Animation Challenge - www.101computing.net/lighthouse-animation-challenge/
from processing import *

angle = 0
lighthouseX = 150
lighthouseY = 150  

def setup():
    frameRate(20)
    size(400,400)
    strokeWeight(1)

def animateLighthouse():
    global angle, lighhouseX,lighhouseY
    
    background(50,140,180)
    fill(255,0,0)
    
    #Draw the lighthouse
    stroke(0,0,0)    
    ellipse(lighthouseX,lighthouseY,30,30)
    
    #Draw the boat
    translate(20,40)
    fill(255,0,0)
    beginShape()
    vertex(0, 15)
    vertex(70, 15)
    vertex(60, 30)
    vertex(10, 30)
    vertex(0, 15)
    vertex(10, 15)
    vertex(10, 0)
    vertex(30, 0)
    vertex(30, 15)
    endShape()
    translate(-20,-40) #Cancel translation so that it does not apply to the lightbeam
    
    #Draw the light beam
    stroke(255,255,0)  
    fill(255,255,0)
    
    angle+=0.5
    if angle>=360:
      angle=0
    #Center of rotation is (0,0)
    #By using a translation we create a rotation effect from (lighthouseX,lighhouseY)
    translate(lighthouseX,lighthouseY)
    rotate(radians(angle))
    triangle(0,0,400,0,400,90)

draw = animateLighthouse

run()
