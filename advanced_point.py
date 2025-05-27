from color_point import ColorPoint

class AdvancedPoint(ColorPoint): #inheriting from color point
    COLORS = ["red", "blue", "black", "white", "green"]
    def __init__(self,x,y,color):
        """Magic method to initialize an advanced point with validation for coordinates and color.
        :param x: x value
        :param y: y value
        :param color: color of point"""
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
        """" Gets x-coordinate value as an attribute instead of a method
        :return: x-coordinate value as int/float"""
        return self._x
    @property
    def y(self):
        """ Gets y-coordinate value as an attribute instead of a method
        :return: y-coordinate value as int/float"""
        return self._y


    @property
    def color(self):
        """"Gets point's color
        :return:current color of point as str"""
        return self._color
    @color.setter
    def color(self, new_color):
        """    Sets a new color for the point with validation
        :param new_color:new color to assign to point
        :return:point with new color"""
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of:{AdvancedPoint.COLORS}")
        self._color=new_color

    @classmethod
    def add_color(cls, new_color):
        """  Adds new color to the class' available COLORS list
        :param new_color:new color to add to list
        :return:list appended"""
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1,p2):
        """ Calculates distance between two points
        :param p1:point 1
        :param p2:point 2
        :return: distance between point 1 and point 2"""
        return ((p1._x-p2._x) **2 + (p1._y-p2._y)**2)**0.5

    @staticmethod
    def from_dictionary(dict):# if there is nothing in a given point this values will be set as default
        """Creates an advanced point from a dictionary, point "factory"
        :param dict: dictionary containing x,y and color keys
        :return:advanced point"""
        x=dict.get("x",10)
        y = dict.get("y", 20)
        color=dict.get("color","black")
        return AdvancedPoint(x,y,color)



AdvancedPoint.add_color("Amber")

p2=AdvancedPoint(1,2,"Amber")
p3=AdvancedPoint(-1,-2,"blue")
print(AdvancedPoint.distance_2_points(p2,p3))



