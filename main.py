#!/bin/python3
#from Tkinter import *
import json
import turtle
import urllib.request


url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url).read()
result = json.loads(response.decode())

print('People in Space: ', result['number'])

people = result['people']
for p in people:
  print(p)
  
url2 = 'http://api.open-notify.org/iss-now.json'
response2 = urllib.request.urlopen(url2).read()
result2 = json.loads(response2.decode())

location = result2['iss_position']
lat =float (location['latitude'])
lon =float (location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon,lat)
key=input("Enter q to quit")
if (key=='q'):
	quit()

