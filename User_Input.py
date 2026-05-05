# input() = A function that prompts the user to enter data
# returns the entered data as a string

print("What is your name?: ")
name = input()
print(f"Hello {name}") #IT WORKSSS

#for numbers it's different, for example if you accept age input but wanna add for example 1 to it
#you cant do that as all user input is string, so you would have to type cast it into an int first

age = input("How old are you?: ") #user input
age = int(age) #type casting
age += 1 #adding 1
print(f"You are {age} years old")

#we can combine these steps to the following
age = int(input("How old are you?: ")) #encase the input in the type casting function

#Exercise 1 Rectangle Area calc - attempting this myself

#Area = width * length
#All inputs are strings, so I will need to typecast into integers so I can do the math
# declare variables, allow user input, print statements using print f

width = int(input("What is the rectangle's width?: "))
length = int(input("What is the rectangle's length?: "))

area = width * length

print(f"The area of the rectangle is {area}cm²") #windows + alt + numlock + 0178 for the little 2
#Notes: the difference between mine and his code is that he used float instead of int, which works better for this scenario