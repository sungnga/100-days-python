# DAY 24 - Files, Directories, and Path

### Today's lessons:
- File I/O reading and writing to local files
- File directories
- Reading and writing to CSV
- Intro to the Pandas framework

### Add a high score to the Snake Game
- The Snake Game project from day 20-21
- Let's add the functionality to keep track of high score
- File: scoreboard.py
  - In the Scoreboard class, add a high_score attribute and set it to 0
  - Replace the game_over method with a new method called reset. Instead of writing "GAME OVER", we're going to reset the scoreboard and save the high score in the high_score attribute
  - In the update_scoreboard() method, call the self.clear() method because we've saved the high score in the high_score attribute. Lastly, display the high_score value as well
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

    def reset(self):
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
- File: main.py
```py

```

### How to open, read, and write to files using the "with" keyword

### Read ans write the high score to a file in Snake Game


### Understand relative and absolute file paths


### Day 24 project: Mail Merge

