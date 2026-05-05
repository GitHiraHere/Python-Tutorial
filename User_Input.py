# input() = A function that prompts the user to enter data
# returns the entered data as a string

print("What is your name?")
name = input()
print(f"Hello {name}") #IT WORKSSS

#for numbers it's different, for example if you accept age input but wanna add for example 1 to it
#you cant do that as all user input is string, so you would have to type cast it into an int first

age = input("How old are you?") #user input
age = int(age) #type casting
age += 1
print(f"You are {age} years old")