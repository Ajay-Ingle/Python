class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def print_Exception(self):
        print("User defined exception: ",self.msg)

try:
    raise Accident("Crash between cars. ")
except Accident as e:
    e.print_Exception()

"""
finally after the except is necessary to handle the exception and execution necessatiy of the code that is necessary for the program.

Suppose dealing with program of the file were the final statment i.e. f.close()
is necessary to execute the release operation for resources if not executed becasue of some random errors then it will be unusual so we can use this statment for closing the file resources we can use it in the finally: block which makes us sure to execute at all.
"""
    