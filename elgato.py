import requests
import argparse
from itertools import cycle, chain

class ghost:
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--sourceaddress", help="Elgato Ip", default = '192.168.1.43')
    parser.add_argument("-o", "--onoroff", help="Elgato On or Off", default = 1)
    parser.add_argument("-b", "--brightness", help="Elgato Brightness", default = 100)
    parser.add_argument("-t", "--temperature", help= "Elgato Temperature", default = 321)
    parser.add_argument("-w", "--todo", help="1 for GhostLight, 2 for TurnOff, 3 for TurnOn",
                         default = 1)

    def __init__(self):
        args = self.parser.parse_args()
        toRun = args.todo
        print(toRun)       
        if toRun == 1:
            run_1 = self.ghostlight()
        elif toRun == 2:
            run_2 = self.turnOff()
        elif toRun == 3:
            run_3 = self.turnOn()
        else:
            return "invalid action"
    
    
    def ghostlight(self):
        
        args = self.parser.parse_args()
        
        
        for n in cycle(chain(range(0, 100, 1), range(100, 0, -1))):
            
            print(args.sourceaddress)
            r = requests.put('http://'+args.sourceaddress+':9123/elgato/lights',
                             json={"numberOfLights":1,"lights":[{"on":args.onoroff,
                                    "brightness":n, "temperature":args.temperature}]})

            print(r)
            print(r.content)
            
        
            
            
    def turnOff(self):
        
        args = self.parser.parse_args()
        r = requests.put('http://'+args.sourceaddress+':9123/elgato/lights',
                             json={"numberOfLights":1,"lights":[{"on":0,"brightness":0,
                                                                 "temperature":0}]})
        
        print("Turning Off...")
        print(r)
        print(r.content)
    
           
    
    def turnOn(self):
        
        args = self.parser.parse_args()
        r = requests.put('http://'+args.sourceaddress+':9123/elgato/lights',
                             json={"numberOfLights":1,"lights":[{"on":1,"brightness":100,
                                                                 "temperature":321}]})
        
        print("Turning On...")
        print(r)
        print(r.content)
        
        


run = ghost()
