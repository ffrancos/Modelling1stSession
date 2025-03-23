from color_point import ColorPoint

class AdvancedPoint(ColorPoint): #inheriting from color point
    COLORS = ["red", "blue", "black", "white", "green"]
    def __init__(self,x,y,color):
        if not isinstance(x,(int,float)):
            raise TypeError("X must be an number")
        if not isinstance(y,(int,float)):
            raise TypeError("Y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"COLOR MUST BE one of:{self.COLORS}")
        #super().__init__(x,y,color) #super is a function that calls the parent class
        self._x = x
        self._y = y
        self._color = color
    @property
    def x(self):
        return self._x
    def y(self):
        return self._y


    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of:{AdvancedPoint.COLORS}")
        self._color=new_color

    @classmethod
    def add_color(cls, new_color):
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1,p2):
        return ((p1._x-p2._x) **2 + (p1._y-p2._y)**2)**0.5

    @staticmethod
    def from_dictionary(dict):# if there is nothing in a given point this values will be set as default
        x=dict.get("x",10)
        y = dict.get("y", 20)
        color=dict.get("color","black")
        return AdvancedPoint(x,y,color)



AdvancedPoint.add_color("Amber")

p2=AdvancedPoint(1,2,"Amber")
p3=AdvancedPoint(-1,-2,"blue")
print(AdvancedPoint.distance_2_points(p2,p3))



