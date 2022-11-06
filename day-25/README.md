# DAY 25 - Working with CSV Data and the Pandas Library

### Today's lessons:
- Reading CVS data
- Introduction to the Pandas framework

### Functions:
- .readlines()

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



### The Great Squirrels census data analysis (with Pandas)



### Day 15 project: U.S. States Game

