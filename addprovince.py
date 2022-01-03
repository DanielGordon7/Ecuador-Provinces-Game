from turtle import Turtle


class AddProvince(Turtle):
    def __init__(self, province_name, x_position, y_position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x_position, y_position)
        self.write(arg=province_name, align="center", font=("Arial", 10, "normal"))