### FUNCTIONS ###
### functions are one of the reasons programming is so practical
### in short, functions allow you to make certain processes that you would like to do
### over and over again modular, without having to re-write the same code multiple times

### defining functions in python is simple, and always begins with the built-in 'def' statement
### for example, the function below takes in an input number x and returns the number x+1:

def add_one(x):
    return x+1

### one can then call a function simply as below

print(add_one(1)) #prints 2

### one can also call a function with a variable

x = 1
print(add_one(x)) #prints 2

### you can also store the output of the function in another variable:

y = add_one(x)
print(y) #prints 2

### the 'return' statement defines what the function returns. Not all functions need to have a return statement
### nor do they need to take in any inputs. for example, the below function simply prints "hello":

def print_hello():
    print("hello")

print_hello() #prints "hello" to console

### one can also call functions inside of other functions
### as an example, for any number x, the absolute value of x can be defined as: |x| = sqrt(x^2)
### (where sqrt is the square root of a positive number)

### we can implement this easily by making our own functions sqrt and square (though functions are probably overkill for this):

def sqrt(x):
    return pow(x, 0.5) # the built-in 'pow' function takes powers of ints and floats

def square(x):
    return pow(x, 2)

def absolute_val(x):
    x_squared = square(x)
    abs_x = sqrt(x_squared)
    return abs_x

x1 = -3
x2 = 3

print(absolute_val(x1)) #prints 3.0
print(absolute_val(x2)) #prints 3.0

### functions can also take in multiple objects as inputs
### for example, the following functions take in two numbers and adds them:

def add_numbers(x,y):
    return x+y

print(add_numbers(3, 5)) #returns 8

##### PROBLEM 1 #####
### implement your own function 'in_list' to check if a particular value, x, is in a given list
### your function should take two inputs: x and list, and check if x is in the list
### if x is in the list, the function should return True, otherwise it should return False
### hint: you can use a for loop and iterate through each value in list, and check if x is equal to that value
### *NOTE: this problem is actually superfluous, as python has a built-in operation 'in' that does this operation
### nonetheless, it is a good exercise to try and implement it yourself :)

############## CODE GOES HERE #################



###############################################


## should return True ##
test_x1 = 1
test_list1 = [1,2,3]

## should return True ##
test_x2 = 'hello'
test_list2 = [2,4,5,'hello',9,'goodbye']

## should return False ##
text_x3 = 17
test_list3 = [14,9,'tommy',1]
