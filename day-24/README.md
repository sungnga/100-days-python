# DAY 24 - Files, Directories, and Path

### Today's lessons:
- File I/O reading and writing to local files
- File directories
- Reading and writing to CSV

### Functions:
- open()
- read()
- close()
- write()
- strip()
- replace()


### Add a high score to the Snake Game
- The Snake Game project from day 20-21
- Let's add the functionality to keep track of high score
- File: scoreboard.py
  - In the Scoreboard class, add a high_score attribute and set it to 0
  - Replace the game_over method with a new method called reset_scoreboard. Instead of writing "GAME OVER", we're going to reset the scoreboard and save the high score in the high_score attribute
  - In the update_scoreboard() method, call the self.clear() method because we've saved the high score in the high_score attribute. Lastly, display the high_score value
  ```py
  from turtle import Turtle

  ALIGNMENT = 'center'
  FONT = ('Courier', 20, 'normal')


  class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.score = 0
      self.high_score = 0
      self.color('white')
      self.penup()
      self.goto(0, 270)
      self.hideturtle()
      self.update_scoreboard()

    def update_scoreboard(self):
      self.clear()
      self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
      if self.score > self.high_score:
        self.high_score = self.score
      self.score = 0
      self.update_scoreboard()

    # def game_over(self):
    #   self.goto(0, 0)
    #   self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
      self.score += 1
      self.update_scoreboard()
  ```
- File: snake.py
  - Currently, when the snake collides with the wall or its tail, the scoreboard is reset but the snake segments have gone off the screen. We also need to reset the snake for the next round
  - In the Snake class, write a reset_snake() method to reset the snake segments. We perform the following operations:
    - First, call the .clear() method to clear the items in the segments list
    - Second, we call the self.create_snake() method to create a new three-segment snake body at the starting position
    - Lastly, set the snake head to the first segment in the segments list
  ```py
  from turtle import Turtle

  STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
  MOVE_DISTANCE = 20
  UP = 90
  LEFT = 180
  DOWN = 270
  RIGHT = 0


  class Snake:
    def __init__(self):
      self.segments = []
      self.create_snake()
      self.head = self.segments[0]

    def create_snake(self):
      for position in STARTING_POSITIONS:
        self.add_segment(position)

    def add_segment(self, position):
      new_segment = Turtle(shape='square')
      new_segment.penup()
      new_segment.color('white')
      new_segment.goto(position)
      self.segments.append(new_segment)

    def reset_snake(self):
      self.segments.clear()
      self.create_snake()
      self.head = self.segments[0]

    def extend(self):
      # Get the position of the last segment
      # This is the position we use to add a new segment
      self.add_segment(self.segments[-1].position())

    def move(self):
      # Move the last segment to second to last segment and so on
      # seg_num starts at last segment
      for seg_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
      self.head.forward(MOVE_DISTANCE)

    def up(self):
      if self.head.heading() != DOWN:
        self.head.setheading(UP)

    def down(self):
      if self.head.heading() != UP:
        self.head.setheading(DOWN)

    def left(self):
      if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)

    def right(self):
      if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)
  ```
- File: snake.py
  - The last issue we have with our current code is when the scoreboard and the snake have been reset, the old snake body still lingers on the screen. We want to clear the old snake body as well
  - In the reset_snake() method, loop through the segments list and for each segment call the .reset() method on it
  ```py
  def reset_snake(self):
    for seg in self.segments:
      seg.reset()
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]
  ```
- File: main.py
  - When the snake collides with the wall or with the tail, we want to call the reset_scoreboard method on the scoreboard to reset th scoreboard and call the reset_snake method on snaky to reset the snake object
  ```py
  game_is_on = True
  while game_is_on:
    screen.update()
    time.sleep(.4)
    snaky.move()

    # Detect collision with food
    if snaky.head.distance(food) < 15:
      food.refresh()
      snaky.extend()
      scoreboard.increase_score()

    # Detect collision with wall
    if snaky.head.xcor() > 280 or snaky.head.xcor() < -280 or snaky.head.ycor() > 280 or snaky.head.ycor() < -280:
      scoreboard.reset_scoreboard()
      snaky.reset_snake()

    # Detect collision with tail
    for segment in snaky.segments[1:]:
      # If head collides with any segment in the tail
      if snaky.head.distance(segment) < 10:
        scoreboard.reset_scoreboard()
        snaky.reset_snake()
  ```
- Our Snake Game is working and it keeps track of the high score. However, when we manually stop the game and restart again, our high score is set to 0 again. We currently don't have a way to save our high score and retrieve it when we restart the game

### How to open, read, and write to files using the "with" keyword
- Built-in **open() function**: `open(file, mode)`
- To open a file and save it to a variable: call the open() function and pass in the name of the file
  - `file = open("my_file.txt")`
- The **.read()** method reads the file and returns the content of the file as a string
  ```py
  file = open("my_file.txt")
  contents = file.read()
  print(contents)
  ```
- The **.close()** method closes down the file manually. Because opening a file takes up memory
- Using the ***with*** keyword to open, read, and write files
  ```py
  # Open a file and save it to a variable called file
  with open("my_file.txt") as file:
    contents = file.read()
    # Read the file and save the contents to a variable called contents
    print(contents)
  ```
  - The ***with*** keyword will automatically closes the file when we no longer need it
- Open file **modes**:
  - `open("file_name", mode)`
  - The open file mode allows us to decide what we want to do when we open a file
  - File mode options:
    - Read - By default, the open file mode is "read"
    - Write - In "write" mode, if the file doesn't exist, it will create one. If the file exists and there's content in it, it will overwrite the existing content
    - Append - The "append" mode, will append new content to the end of the file and will not overwrite existing content
  ```py
  with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
  ```
- The **.write()** method writes contents to a specified file and depending on the ****mode**** of the file, it can overwrite the existing contents or append the new contents to the file

### Read and write the high score to a file in Snake Game
- In the Snake Game project directory, create a text file called high_score.txt. In it, contains a value of 0
- In the Scoreboard class, instead of using a hard-coded value for the high_score, we want to read and write/update the high score from the text file
- In the reset_scoreboard method, if the score value is greater than the high_score, we want to update the high_score attribute as well as the high_score in the high_score.txt file
- File: scoreboard.py
  ```py
  from turtle import Turtle

  ALIGNMENT = 'center'
  FONT = ('Courier', 20, 'normal')


  class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.score = 0
      with open("high_score.txt") as file:
        self.high_score = int(file.read())
      self.color('white')
      self.penup()
      self.goto(0, 270)
      self.hideturtle()
      self.update_scoreboard()

    def update_scoreboard(self):
      self.clear()
      self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
      if self.score > self.high_score:
        self.high_score = self.score
        with open("high_score.txt", mode="w") as file:
          file.write(f"{self.high_score}")
      self.score = 0
      self.update_scoreboard()

    def increase_score(self):
      self.score += 1
      self.update_scoreboard()
  ```

### Understand relative and absolute file paths
- A ***path*** is a way for the computer to navigate to the file or folder of interest
- Absolute file path - always starts off relative to the root of the computer
- Relative file path - starts from the current working directory to the file of interest

### Day 24 project: Mail Merge

