import pandas
from turtle import Turtle
from turtle import Screen
from addprovince import AddProvince

data = pandas.read_csv("provinces_data.csv")

screen = Screen()
tim = Turtle()
tim.hideturtle()

screen.bgpic("ecuador_blank_map.gif")
screen.title("Ecuador Provinces Guessing Game")
screen.setup(width=725, height=491)

all_provinces = data.provinces.tolist()
correct_provinces = []

while len(correct_provinces) < 24:
    user_guess = screen.textinput(title=f"{len(correct_provinces)} / {len(all_provinces)} Provinces",
                                  prompt="Type 'exit' to give up.\nGuess a Province:").title()

    if user_guess in all_provinces and user_guess not in correct_provinces:
        selected_row = data[data.provinces == user_guess]
        selected_x = int(selected_row.x_positions)
        selected_y = int(selected_row.y_positions)
        add_state = AddProvince(user_guess, selected_x, selected_y)
        correct_provinces.append(user_guess)

    if user_guess == "Exit":
        missing_provinces = [province for province in all_provinces if province not in correct_provinces]
        print(f"You got {len(correct_provinces)}/{len(all_provinces)} provinces correctly.\n"
              f"You missed {missing_provinces}")
        break

if len(correct_provinces) == 24:
    print("You Win! You know all 24 provinces of Ecuador!")

screen.bye()
