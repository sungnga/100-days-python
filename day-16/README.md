# DAY 16 - Object Oriented Programming (OOP)

#### Today's lessons:
- Object Oriented Programming (OOP)
- How to use OOP: classes and objects
- Constructing objects and accessing their attributes and methods
- How to add Python packages

#### Functions:


#### Why do we need OOP and how does it work?
- **Procedural programming:** 
  - Set up procedures or functions that do particular thing. One procedure leads to another procedure. The computer is working from top to bottom and jumping into a function as needed
  - Procedural programming is one of the earliest days of programming. Older programming languages such as Fortran and Cobol rely on procedural programming
- **Object Oriented Programming (OOP):**
  - Object Oriented Programming paradigm comes in handy for a large and complex software project
  - Split large tasks into smaller modules that can be worked on by different people and can be reusable

#### How to use OOP: classes and objects
- Object Oriented Programming (OOP) tries to model real-life objects
- An **object** has two things:
  1. What it has. In programming is called **attributes**
    - Usually modeled with variables
  2. What it does. In programming is called **methods**
    - Modeled by functions
- These variables and functions are not free floating, but they are associated with the object
- An object is a way of combining some piece of data and some functionality
- **Classes:**
  - A class is like the blueprint. It may contain attributes and methods
- **Objects:**
  - An object is an instance that is generated from a particular class
  - Multiple objects can be generated from a class

#### Constructing objects and accessing their attributes and methods
- **Constructing objects:**
  - To construct an object from a class, simply add parenthesis `()` after the class name. This activates the construction of the object from the blueprint. Then assign the new object a name
  - The name of a class is usually written with the first letter of each word capitalized. This differentiates a class name from a variable or a function that we name
  - `car = CarBlueprint()`
- **Accessing object attributes and methods:**
  - An object has attributes and methods. To access them, simply add a period `.` after the object name followed by the name of the attribute or method. Similar to invoking a function, add the parenthesis `()` after the method name to invoke the method
  ```py
  car = carBlueprint()
  car.speed #get the speed attribute
  car.stop() #invoking the stop method on car object
  ```

#### How to add Python packages and use PyPi


#### Practice modifying object attributes and calling methods



### Day 16 project: The OOP Coffee Machine
