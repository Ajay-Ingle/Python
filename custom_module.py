"""
here arg value is set to zero so that when the value is not passed to the function it will be zero by default
"""
def area_of_triangle(base=0,height=0):
    area = 1/2 *base * height
    return area

def area_of_square(len=0):
    area = len*len
    return area