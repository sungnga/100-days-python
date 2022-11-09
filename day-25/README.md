# DAY 25 - Working with CSV Data and the Pandas Library

### Today's lessons:
- Reading and writing CVS data
- Introduction to the Pandas framework

### Functions:
- .readlines()
- .to_dict()
- .to_list()
- pandas.DataFrame()
- .to_csv()

### Reading CSV data
#### Option 1: Using .readlines() method
  - This method of reading CVS data requires additional cleanup before it's ready to be used
  ```py
  with open("./weather_data.csv") as file:
    data = file.readlines()
    print(data)
  ```
#### Option 2: Using built-in cvs library
  ```py
  import csv

  with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
      if row[1] != "temp":
        temperatures.append(int(row[1]))
    print(temperatures)
  ```
#### Option 3: Using Pandas external library
  - Pandas docs: https://pandas.pydata.org/docs/
  - Install Pandas library: In pyCharm, type `import pandas`, hover over the text and click on "Install package pandas"
  ```py
  import pandas

  data = pandas.read_csv("weather_data.csv")
  print(data['temp'])
  ```

### DataFrames & series: working with rows and columns
- Two primary data structures of pandas:
  - DataFrame - 2-dimensional dataset. Is equivalent to a table
  - Series - 1-dimensional dataset. Is equivalent to a single column in a table
```py
import pandas

# Reading a csv file
data = pandas.read_csv("weather_data.csv")
# Identifying a dataframe and a series
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(type(data['temp']))  # <class 'pandas.core.series.Series'>

# Converting DataFrame into a dictionary
data_dict = data.to_dict()
print(data_dict)

# Converting a column into a list
temp_list = data["temp"].to_list()
print(temp_list)

# Calculate the average temperature
print(data["temp"].mean())

# Get the highest temp value in temp series
print(data["temp"].max())

# Get data in columns
print(data['condition'])  # using the bracket notation. Treat it like a dictionary, calling it by the key
print(data.condition)  # using it as an object, calling by its attribute

# Get data in row
print(data[data.day == 'Monday'])  # get the data for the rest of that row
# Print the row of data which had the highest temp
print(data[data.temp == data['temp'].max()])
# get weather condition on Monday row
monday = data[data.day == 'Monday']
print(monday.condition)
# convert Monday's temp to fahrenheit
monday_temp = int(monday.temp)
monday_temp_F = (monday_temp * 9/5) + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
	"students": ['Amy', 'James', 'Nga'],
	"scores": [88, 76, 94]
}
data = pandas.DataFrame(data_dict)
print(data)
# convert the dataframe to a csv file
data.to_csv("new_data.csv")
```

### The Great Squirrels census data analysis (with Pandas)
```py
import pandas

# Read cvs data file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

unique_fur_colors = data['Primary Fur Color'].unique()
# print(unique_fur_colors)
count = list(data['Primary Fur Color'].value_counts())
# print(count)

data_dict = {
	"Fur Color": [],
	"Count": []
}

for color in unique_fur_colors:
  if color == 'Gray':
    data_dict["Fur Color"].append('grey')
  elif color == 'Cinnamon':
    data_dict["Fur Color"].append('red')
  elif color == 'Black':
    data_dict["Fur Color"].append('black')
data_dict["Count"] = count
# print(data_dict)

# Create squirrel count dataframe
squirrel_count = pandas.DataFrame(data_dict)
# print(squirrel_count)

# Convert squirrel count dataframe to cvs file
squirrel_count.to_csv("squirrel_count.csv")
```

### Day 15 project: U.S. States Game
##### STEPS TO BUILDING THE U.S. STATES GAME
##### 1. Convert the guess to Title case
##### 2. Check if the guess is among the 50 states
##### 3. Write correct guesses onto the map
##### 4. Use a loop to allow the user to keep guessing
##### 5. Record the correct guesses in a list
##### 6. Keep track of the score
##### 7. If user exits, save the missing states to csv file
- File: us-states-game/main.py
  ```py
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
  ```
