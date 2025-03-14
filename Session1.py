import random

class Point:
    """
    Class Modeling a real life 2D point
    """
    def __init__(self,x,y):
        """
        Initialize the point instance
        :param x: x axis coordinate value
        :param y: y axis coordinate value
        """
        self.x=x
        self.y=y
    def __str__(self):
        """Magic Method that defines how a point is printed
        """
        return f"<{self.x},{self.y}>"
    def __repr__(self):
        return self.__str__()
    def distance_origin(self):
        return (self.x**2+self.y**2)**0.5
    def __gt__(self, other):
        """
        self>other
        :param other: the other point
        :return: True/False
        """
        return self.distance_origin()>other.distance_origin()
    def __eq__(self, other):
        return self.distance_origin()==other.distance_orig()

points=[]
for i in range (5):
    p=Point(
        random.randint(-100,100),
        random.randint (-100, 100)
    )
    points.append(p)

print(points)



p1=Point(1,2)
p2=Point(3,4)
p3=Point("MARK","JANE")
print(p1.x,p1.y)
print(p1)
print(po)













