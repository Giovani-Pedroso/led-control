#!/usr/bin/env python3
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
import serial.tools.list_ports
import serial
import time

class mainScreen(MDBoxLayout):

    #link the objecs on kivy to the objects in python
    serialPorts = ObjectProperty()
    redSlider = ObjectProperty()
    greenSlider = ObjectProperty()
    blueSlider = ObjectProperty()



    def searchArduino(self):

        #clean the spinner
        self.serialPorts.values = []


        for i in  serial.tools.list_ports.comports():
            #print(i)
            self.serialPorts.values.append(str(i))

        #Add the option to desconect the arduino
        self.serialPorts.values.append("Disconnect")

    def connectArduino(self):

        if self.serialPorts.text == "Disconnect":
            #if the arduino is disconnectes the code will block
            #the sliders
            self.redSlider.disabled = True
            self.greenSlider.disabled = True
            self.blueSlider.disabled = True
           # self,serialPorts.text = "Disconnected"

        else:
            #filter the unnecessary data
            port = self.serialPorts.text.split(' ')
            #connec the arduino to the PC
            #/dev/ttyACM0

            self.arduinoSerial = serial.Serial(port[0],
                                          baudrate=9600,
                                          timeout= 1)

           # print(arduinoSerial)
            #activate the sliders
            self.redSlider.disabled = False
            self.greenSlider.disabled = False
            self.blueSlider.disabled = False

    def sendArduino(self, slider, value):
        #send the data to arduino
        val = chr(value)
        #the encone must be latin-1, because values > 128 in
        #utf-8 are 2 bytes long
        self.arduinoSerial.write(slider.encode('latin-1'))
        time.sleep(0.01)
        print(f"slider {slider} value {val.encode('latin-1')}")
        self.arduinoSerial.write(val.encode('latin-1'))

class app(MDApp):
  ...



app().run()
