from PyP100 import PyP110

class SmartPlug:
    def __init__(self, ip, email, password):
        self.plug = PyP110.P110(ip, email, password)
    
    def connect(self):
        try:
            self.plug.handshake()
            self.plug.login()
            print("Connected")
        except Exception as e:
            print(f"Could not connect: {e}")
    
    def toggle(self):
        try:
            self.plug.toggleState()
            print("Toggle state")
        except Exception as e:
            print(f"Could not toggle: {e}")
    
    def getEnergyUsage(self):
        try:
            usage = self.plug.getEnergyUsage()
            return usage
        except Exception as e:
            print(f"Could not get Usage values: {e}")
            return None
        
