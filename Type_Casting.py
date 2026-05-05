#Type casting is the process of converting a var from one data type to another
# str(), int(), float(), bool()
#used with user input, and user inputs are always strings so can be used if you need to
#convert the data type

name = "H"
age = 67
gpa = 3.2
is_student = True

type(name) #this is how we get the data type of variable, but this does not print anything
#to print it we can do the following
print(type(name)) #prints <class 'str'>

#converting gpa from float to int
gpa = int(gpa)
print(f"The GPA is {gpa}")

name = bool(name) #this will either print true or false. we can use this to check
#if a user has inputted a name or if the string is empty i.e. ""
print(name)
