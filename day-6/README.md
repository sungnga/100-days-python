## DAY 6 - Functions and While Loop

#### Today's lessons:
- Functions

#### Functions:
- while loop

#### Defining and calling functions
- Creating our own function is a two-step process:
  - First, we need to define the function using the `def` keyword and give the function a name. We know that we are defining a function by adding the `()` after the function name
  - Second, call or invoke the function to use it. We do this by adding the parenthesis `()` after the function name
  ```py
  # Define the function
  def my_function():
    #Do this
    #Then do this
    #Finally do this
    
  # Invoke the function
  my_function()
  ```

#### Indentation
- When defining a function, every line of that is indented after the definition will be inside the function

#### while loops
- The while loop is the loop that will continue going while a particular condition is true
```py
while something_is_true:
  #Do something repeatedly
```

### Day 6 project: Escaping the Maze
```py
def turn_right():
  turn_left()
  turn_left()
  turn_left()

while not at_goal():
  if right_is_clear():
    turn_right()
    move()
  elif front_is_clear():
    move()
  else:
    turn_left()
```