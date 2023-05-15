#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

class TV:
    #Constructor
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.on = True
    #Turns ON this TV
    def turnOn(self):
        self.on = True
    #Turns OFF this TV
    def turnOff(self):
        self.off = False
    #Get Channel
    def getChannel(self):
        return self.getChannel
    #Set Channel
    def setChannel(self, newChannel):
        self.setChannel = newChannel
    #Get Volume
    def getVolume(self):
        return self.getVolume
    #Set Volume
    def setVolume(self, newVolume):
        self.setVolume = newVolume
    #Channel Up
    #Channel Down
    #Go to Channel
    #Volume Up
    def volumeUp(self, amount):
        self.volume += amount
    #Volume Down
    def volumeDown(self, amount):
        self.volume -= amount