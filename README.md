# Elgato-Light-Ghost
Send push requests to Elgato Light 

Contains three methods:
1: GhostLight - an infinite loop which causes the light to increment the brightness
   from 0 to 100 and from 100 to 0
  
2: Turn-Off - will simply shut off the light

3: Turn-On -  will turn the light on

Flags:
"-ip", "--sourceaddress", help="Elgato Ip", default = '192.168.1.43'
"-o", "--onoroff", help="Elgato On or Off", default = 1
"-b", "--brightness", help="Elgato Brightness", default = 100
"-t", "--temperature", help= "Elgato Temperature", default = 321
"-w", "--todo", help="1 for GhostLight, 2 for TurnOff, 3 for TurnOn", default = 1


