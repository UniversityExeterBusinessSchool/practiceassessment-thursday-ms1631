#######################################################################################################################################################
# 
# Name: Moumita SInha
# SID: 740096245
# Exam Date: 27/03/2025
# Module: BEMM458 - Programming for Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-ms1631.git
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

#First and Last digit from my SID is 7 and 5 hence storing it in a list
allocated_key=[7,5]
# Initialize an empty list to store (start, end) positions
my_list = []
 #for loop to find start and end position using find().
for key in allocated_key:
    comment=key_comments[key]
    start=customer_feedback.find(comment)
    if start != -1:
        end = start + len(comment)
        my_list.append((start, end))
#Printing my_lis.
print(my_list)

#OUTPUT-
"""[(129, 136), (99, 109)]"""
##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin,  per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
first_two=74
# # Insert last two digits of ID number here:
last_two=45
# # Write your code for Operating Profit Margin
def operating_profit_marging(operating_marging,revenue):
    if revenue !=0:
        return (operating_marging/ revenue)*100
    else:
        return 0


# # Write your code for Revenue per Customer
def revenue_per_customer(revenue,customers):
    if customers !=0:
        return (revenue/customers)
    else:
        return 0

# # Write your code for Customer Churn Rate
def customer_churn_rate(lost_customer,total_customer):
    if total_customer !=0:
        return (lost_customer/total_customer)*100
    else:
        return 0
# # Write your code for Average Order Value
def avg_order_value(revenue,order):
    if order!=0:
        return (revenue/order)
    else:
        return 0
# # Call your designed functions here
print("Operating Profit Marging: ", operating_profit_marging(first_two,last_two))
print("Revenue Per Customer: ", revenue_per_customer(first_two,last_two))
print("Customer Churn rate: ",  customer_churn_rate(last_two,first_two))
print("Average Order value: ", avg_order_value(first_two,last_two))

#OUTPUT-
"""
Operating Profit Marging:  164.44444444444443
Revenue Per Customer:  1.6444444444444444
Customer Churn rate:  60.810810810810814
Average Order value:  1.6444444444444444

"""


##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
price = np.array([20,25,30,35,40,45,50,55,60,65,70])
demand = np.array([300,280,260,240,210,190,160,140,120,100,85])

b,a = np.polyfit(price, demand, 1)
#Printing the Estimated Slope
print("Estimated Slope: ", a)
print("Estimated Intercept", b)
#Printing the maximum revenue
max_revenue_price = -a/(a*2)
print("Price to Maximum Revenue: ", max_revenue_price)

demand_at_52 = a + b *52
print("Demand at 52 GBP", demand_at_52)

#OUTPUT-
"""
Estimated Slope:  391.2272727272727
Estimated Intercept -4.4818181818181815
Price to Maximum Revenue:  -0.5
Demand at 52 GBP 158.17272727272726
"""

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

#Fixes done below are explaained in comments
import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number

"""max-value = integer(input("Enter your Student ID: "))"""
#instead of Integer we use int to parse the output/variable in Integer
#Also max-value is replaced with max_value as "-" between variable name is not acceptable in python
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
#changed marker = o in lower, markercolor to markerfacecolor and markerredcolor to markerredgecolor,, changed lable to label
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red',
         linestyle='--', label='Random Numbers', color='blue');
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()
#final plot pasted in word document



