# STEPS TO BUILDING THE U.S. STATES GAME
# 1. Convert the guess to Title case
# 2. Check if the guess is among the 50 states
# 3. Write correct guesses onto the map
# 4. Use a loop to allow the user to keep guessing
# 5. Record the correct guesses in a list
# 6. Keep track of the score
# 7. If user exits, save the missing states to csv file

import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(height=700, width=800)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = list(data.state)
guessed_states = []


def game_over():
  message = turtle.Turtle()
  message.hideturtle()
  message.penup()
  message.goto(x=0, y=260)
  message.color('red')
  message.write("Congratulations! You've named all states!", align='center', font=('Ariel', 30, 'normal'))


def print_state_name(name):
  state_data = data[data.state == name]
  s_name = turtle.Turtle()
  s_name.hideturtle()
  s_name.penup()
  s_name.goto(int(state_data.x), int(state_data.y))
  s_name.write(name, True, align='center', font=('Ariel', 12, 'normal'))


game_is_on = True
while game_is_on:
  answer = turtle.textinput(
    title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state name?").title()
  if answer == "Exit":
    # Save the missing states to a .csv file
    missing_states = []
    for state in states:
      if state not in guessed_states:
        missing_states.append(state)

    data_dict = {
      "Missed States": missing_states
    }
    pandas.DataFrame(data_dict).to_csv("missed_states.csv")
    break
  if answer in states and answer not in guessed_states:
    guessed_states.append(answer)
    print_state_name(answer)
  if len(guessed_states) == 50:
    game_is_on = False
    game_over()
    screen.exitonclick()
