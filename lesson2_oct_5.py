# -*- coding: utf-8 -*-
"""Lesson2.Oct.5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Xo4yXOgDlZ4cY6owNvMMcc-R2SsUaTP

#Lesson 2: Functions and Matplotlib
#Author: Arnav Maskey
"""

#########################

#Functions
#Functions are blocks of code that can be executed anywhere in a program. Functions can be #reused makes the code more modular.

#########################
#Basic Function Definition and Calling:

# Defining a function to greet the user
def greet(name):
    """This function greets the provided name."""
    print(f"Hello, {name}!")

# Calling the function
greet("Arnav")

#########################

#Function with Return Value:

# Defining a function to add two numbers
def add(num1, num2):
    """This function returns the sum of two numbers."""
    return num1 + num2

# Calling the function and storing the result
sum_result = add(5, 3)
print(sum_result)

#########################

# Function with Default Arguments:

# Defining a function with a default argument
def greet(name="User"):
    """This function greets the provided name or 'User' if no name is provided."""
    print(f"Hello, {name}!")

# Calling the function without providing an argument
greet()

# Calling the function with an argument
greet("Arnav")

#########################


# Function with Multiple Return Values:

# Defining a function to return multiple values
def min_max(numbers):
    """This function returns the minimum and maximum of a list of numbers."""
    return min(numbers), max(numbers)

# Calling the function and unpacking the result
min_value, max_value = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {min_value}, Max: {max_value}")

#########################

# Function with Variable Number of Arguments:

# Defining a function to accept a variable number of arguments
def print_args(*args):
    """This function prints all provided arguments."""
    for index, arg in enumerate(args):
        print(f"Argument {index}: {arg}")

# Calling the function with multiple arguments
print_args("Alabama", "Georgia", "Tennessee")

#########################
#Matplotlib examples
#Steps:
#First, the necessary library (matplotlib.pyplot) is imported.
#Data for the chart is defined.
#The chart is created using a function from matplotlib.pyplot (such as plt.plot, plt.bar, etc.).
#Title and labels are added to the chart using plt.title, plt.xlabel, and plt.ylabel.
#Finally, the chart is displayed using plt.show().

#########################

# Line chart

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create line chart
plt.plot(x, y)

# Add title and labels
plt.title('Line Chart Example')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# Display the chart
plt.show()

#########################

# Bar chart

# Data
categories = ['Category 1', 'Category 2', 'Category 3']
values = [4, 7, 1]

# Create bar chart
plt.bar(categories, values)

# Add title and labels
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the chart
plt.show()

##########################

# Pie chart

# Data
labels = ['Section 1', 'Section 2', 'Section 3']
sizes = [15, 30, 45]

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add title
plt.title('Pie Chart Example')

# Display the chart
plt.show()

##########################

# Histogram

# Data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create histogram
plt.hist(data, bins=5, edgecolor='black')

# Add title and labels
plt.title('Histogram Example')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Display the chart
plt.show()

##########################

# Scatter plot

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# Display the chart
plt.show()

##########################

# Box plot

# Data
data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# Create box plot
plt.boxplot(data)

# Add title and labels
plt.title('Box Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the chart
plt.show()

#########################