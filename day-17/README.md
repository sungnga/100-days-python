# DAY 17 - Creating Classes

### Today's lessons:
- Creating classes
- Working with attributes, class constructors, the **init**() function
- Adding methods to a class

### How to create your own classes
- **Class declaration:**
  - The `class` keyword, followed by the name of the class, and a colon `:`
  - Example of class declaration: `class Car:`
  - Any code after the colon `:` and is indented will be part of the class
- The name of the class is written in Pascal case, where each word is in uppercase: `UserName`

### Working with attributes, class constructors, and the **init**() function
- **To create an object from a class:**
  - Add parenthesis `()` after the class name to invoke the object constructor from a class. This will create a new object from the class
  - Then assign the new object a name, usually in snake_case
  - `user_1 = User()`
- **Attribute** - is a variable associated with an object
- **To add an attribute to an object:**
  - Use the dot notation `.` after the object and give the attribute a name. Then assign the attribute a value
  ```py
  class User:
    pass

  user_1 = User()
  user_1.id = "001"
  user_1.username = "nga"

  print(user_1.username) #nga
  ```
- **Class constructors:**
  - A constructor is part of the class blueprint that allows us to specify what should happen when an object is being constructed. This is also known as **_initializing an object._** When an object is being initialized, we can set variables or counters to their starting values
- **To create the constructor:**
  - By using the special `__init__()` function. This function is used to initialize the attributes of the object
  - Inside the `__init__()` function is where we initialize the values for the attributes
  - The `__init__()` function is going to be called every time when creating an object from a class
- **To set attributes in the constructor:**
  - By setting the attributes in the constructor of a class, all objects being constructed from that class will have the same attributes
  - We can add in additional parameters to the `__init__()` function:
    - The 1st params is the keyword `self`. `self` refers to the object
    - Can pass in as many additional params as you like
    - **NOTE:** When we create an object from the class, we must provide the same number of arguments as the number of params we have in the `__init__()` function
    - The values being passed to the params will then be used to set the initial value for the attributes
  - To set an object attribute, use the `self.` notation to refer to the object followed by the name of the attribute. Then initialize the attribute value by setting it equal to the params
    ```py
    # Create User class
    # Create class constructor using __init__() function
    # Set object attributes inside constructor and initialize its value
    class User:
      # self refers to the object
      # Pass in params to the constructor to set initial values of object attributes
      def __init__(self, user_id):
        # object.object_attribute = initial_attribute_value
        self.id = user_id #Set the object attribute to the params value

    # Create an object from class and pass in initial value for attribute
    user_1 = User('001') # attribute seats = 6
    # Another way to set object attribute
    user_1.id = '001'
    ```
- **Ways to initialize attributes in the constructor:**
  - One way to initialize an attribute is to set it equal to the params from the `__init__()` function. Note though when we create an object from the class, we must pass in the values as arguments to the class or else we will get an error
  - Another way is to set the attribute to a value. This way we don't need to pass in additional arguments to the class when we construct an object
    ```py
    class User:
      def __init__(self, user_id, username):
        # Initialize attribute to value from params
        self.id = user_id
        # It is convention to have the name of attribute to be the same as the params
        self.username = username
        # Set attribute to a value
        self.followers = 0

    # Must provide 2 args because we have 2 params in the class constructor
    user_1 = User("001", "nga")
    user_2 = User("002", "daniel")
    print(user_1.followers) #0
    ```

### Adding methods to a class
- The **attributes** are the things that the object has and the **methods** are the things that the object does
- Creating an object method inside a class is very similar to creating a regular method. The difference is the first parameter of the method is the keyword `self`. This refers to the object
  ```py
  # Class declaration
  class ClassName:
    # Class constructor
    def __init__(self, params_1):
      self.attribute = params_1

    # Method
    def method_name(self):
      # Do something

  # Create an object from class
  object_1 = ClassName()
  # Calling a method
  object_1.method_name()
  ```

### Quiz Project part 1: Creating the Question class
- File: question_model.py
  - Task: Create a Question class with an `__init()__` method with two attributes: `text` and `answer` attribute
  ```py
  class Question:
    def __init__(self, q_text, q_answer):
      self.text = q_text
      self.answer = q_answer
  ```

### Quiz Project part 2: Creating the list of question objects from the data
- File: main.py
  - TASK: Create question_bank
    - Write a for loop to iterate over the question_data
    - Create a Question object from each entry in question_data
    - Append each Question object to the question_bank
  ```py
  from data import question_data
  from question_model import Question

  question_bank = []

  for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

  print(question_bank[10].text)
  ```

### Quiz Project part 3: The QuizBrain and the next_question() method
- File: quiz_brain.py
  - The QuizBrain class:
    - attributes: question_number, questions_list
    - methods: next_question()
    - asking the questions
    - checking if the answer was correct
    - checking if we're the end of the quiz
  - TASK:
    - Create a class called QuizBrain
    - Write an **init()** method
      - Initialize the question_number to 0
      - Initialize the questions_list to an input
    - Write a next_question() method
      - Retrieve the item at the current question_number from the question_list
      - Use the input() function to show the user the Question text ans ask the user's answer
  ```py
  class QuizBrain:
    def __init__(self, q_list):
      self.question_number = 0
      self.question_list = q_list

    def next_question(self):
      current_q = self.question_list[self.question_number]
      self.question_number += 1
      input(f"Q:{self.question_number}: {current_q.text} (True/False)?: ")
  ```
- File: main.py
  - Import the QuizBrain class
  - Create a quiz object from the QuizBrain class
  - Call the next_question() method on the quiz object
  ```py
  from data import question_data
  from question_model import Question
  from quiz_brain import QuizBrain

  question_bank = []

  for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

  # print(question_bank[10].text)

  quiz = QuizBrain(question_bank)
  quiz.next_question()
  ```

### Quiz Project part 4: How to continue showing new questions
- File: quiz_brain.py
  - Create method called still_has_questions()
  - Return a boolean depending on the value of question_number
  ```py
  class QuizBrain:
    def __init__(self, q_list):
      self.question_number = 0
      self.question_list = q_list

    def next_question(self):
      current_q = self.question_list[self.question_number]
      self.question_number += 1
      input(f"Q:{self.question_number}: {current_q.text} (True/False)?: ")

    def still_has_questions(self):
      # Returns True or False
      return self.question_number < len(self.question_list)
  ```
- File: main.py
  - Use a while loop to show the next question until the end
  ```py
  from data import question_data
  from question_model import Question
  from quiz_brain import QuizBrain

  question_bank = []

  for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

  quiz = QuizBrain(question_bank)

  while quiz.still_has_questions():
    quiz.next_question()
  ```

### Quiz Project part 5: Checking answers and keeping score
- File: quiz_brain.py
  - Add a score attribute to the QuizBrain class and initialize it to 0
  - Create method called check_answer()
    - Compare the user's answer against the current question's answer. Let user know whether they got the answer correct or not
    - If user answered correctly, increase score by 1 point
    - Print the correct answer
    - Print the user current score
  ```py
  class QuizBrain:
    def __init__(self, q_list):
      self.question_number = 0
      self.question_list = q_list
      self.score = 0

    def next_question(self):
      current_q = self.question_list[self.question_number]
      self.question_number += 1
      user_answer = input(f"Q:{self.question_number}: {current_q.text} (True/False)?: ")
      self.check_answer(user_answer, current_q.answer)

    def still_has_questions(self):
      return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
      if user_answer.lower() == correct_answer.lower():
        self.score += 1
        print("You got it right!")
      else:
        print("That's wrong.")
      print(f"The correct answer was: {correct_answer}.")
      print(f"Your current score is: {self.score}/{self.question_number}.")
      print("\n")
  ```
- File: main.py
  - At the end of the quiz, let the user know they've completed the quiz and print their final score
  ```py
  from data import question_data
  from question_model import Question
  from quiz_brain import QuizBrain

  question_bank = []

  for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

  quiz = QuizBrain(question_bank)

  while quiz.still_has_questions():
    quiz.next_question()

  print("You've completed the quiz")
  print(f"Your final score was: {quiz.score}/{quiz.question_number}")
  ```

### The benefits of OOP: Use Open Trivia DB to get new questions
- Open Trivia docs: https://opentdb.com/api_config.php
- To generate new set of questions, select the category, level of difficulty and type of answer. Then click on "Generate API URL"
- This will generate a JSON-format list of trivia. Paste this list into trivia_data.py file
- File: main.py
  - Modify to import the question_data from trivia_data.py file
  - In the for loop of question_data, modify the keys to properly access the values of the question and answer
  ```py
  from trivia_data import question_data
  from question_model import Question
  from quiz_brain import QuizBrain

  question_bank = []

  for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

  quiz = QuizBrain(question_bank)
  quiz.next_question()
  ```
- The benefits of OOP is we can swap the database as much as we want without having to touch any of our classes, methods, and attributes we've created. Our classes are modular and can be reused in other applications
