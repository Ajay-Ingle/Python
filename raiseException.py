class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def print_Exception(self):
        print("User defined exception: ",self.msg)

try:
    raise Accident("Crash between cars. ")
except Accident as e:
    e.print_Exception()
    