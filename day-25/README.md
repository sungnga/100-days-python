# DAY 25 - Working with CSV Data and the Pandas Library

### Today's lessons:
- Reading CVS data
- Introduction to the Pandas framework

### Functions:
- .readlines()
- .to_dict()
- .to_list()

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

data = pandas.read_csv("weather_data.csv")
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
```

### The Great Squirrels census data analysis (with Pandas)



### Day 15 project: U.S. States Game

