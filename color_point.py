from Session1 import Point # point is the file, Point is the class
import random

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Defines a color point x, y, color
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
         Magic method that defines the format on how a color point is printed
        :return:the point as a string containing x, y and color
        """
        return f"<{self.x},{self.y}>({self.color})"
if __name__=="__main__":
    color_points = []
    colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
    for _ in range(5):
        p = ColorPoint(
            random.randint(-100, 100),
            random.randint(-100, 100),
            random.choice(colors))
        color_points.append(p)
    print("random color points:")
    print(color_points)
    color_points.sort()
    print("color points in order:")
    print(color_points)