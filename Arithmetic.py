import math

friends = 0

friends += 1 #augmented assignment operator
friends -= 1 #augmented assignment operator
friends *= 3 #augmented assignment operator
friends /= 2 #augmented assignment operator
friends **= 2 #augmented assignment operator, exponent equals, friends to the power of 2
remainder = friends % 3 #modulous operator
print(friends)

#Built in math operations
x = 3.14
y = 4
z = 5

result = round(x) #round function to the nearest whole integer
result = abs(y) #absolute value, distance from 0 as a whole number
result = pow(4, 5) #4 to the power of 5, 4x4x4x4x4
result = max(x, y, z) #max value between these variables
result = min(x, y, z) #min value between these variables
print(result)

#Following code requires the imported math class
print(math.pi)
print(math.e) #exponential constant, used in physics, may need it may not lol
result = math.sqrt(x) #square root of x
result = math.ceil(x) #rounds up
result = math.floor(x) #rounds down

#Exercise Circle Area calc - attempting this myself
# C = 2*pi*radius

