# this code was used to generate the csv file used on main.py

from turtle import Turtle
from turtle import Screen
import pandas

tim = Turtle()
screen = Screen()

x_positions = []
y_positions = []

provinces = ["Santa Elena", "Manabi", "Esmeraldas", "Guayas", "Los Rios", "Santo Domingo",
                  "Loja", "El Oro", "Azuay", "Canar", "Chimborazo", "Bolivar", "Tungurahua",
                  "Cotopaxi", "Napo", "Pichincha", "Imbabura", "Carchi", "Zamora Chinchipe",
                  "Morona Santiago", "Pastaza", "Orellana", "Sucumbios", "Galapagos"]
print(len(provinces))

def get_coordinates(x, y):
    print(x, y)
    x_positions.append(x)
    y_positions.append(y)

    if len(provinces) == len(x_positions):
        dict = {
            "provinces": provinces,
            "x_positions": x_positions,
            "y_positions": y_positions
        }

        data = pandas.DataFrame(dict)
        data.to_csv("provinces_data.csv")
        print(data)


screen.bgpic("ecuador_blank_map.gif")
screen.setup(width=537, height=550)

screen.onscreenclick(get_coordinates)

screen.mainloop()


