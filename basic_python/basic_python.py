
#### DATA TYPES ####
### Python (and most programming languages) has several different data types
### the most common numeric data types are int and float
### int is an integer, and float can be a decimal
### for example:

x_int = 4
x_float = 4.5

print(type(x_int)) ## prints <class 'int'>
print(type(x_float)) ## prints <class 'float'>

### you can convert data types as follows

x_float_converted = int(x_float)
x_int_converted = float(x_int)

print(x_float_converted) #prints 4
print(x_int_converted) #prints 4.0

### the next most common data type is a 'string'
### strings can contain anything, and are initialized with quotation marks
### for example

name1 = 'ryan'
name2 = 'tommy'

### you can convert an int or a float to a string, but not the other way around. why?

print(str(x_int)) #still prints 4, but now python recognizes it as a string, rather than a numeric value
print(str(x_float))

print(type(str(x_int))) #prints <class 'str'>

#### BOOLS ####
### boolean variables are simply variables that contain either 'True' or 'False'

x_true = True
x_false = False

print(x_true)
print(x_false)

print(type(x_true))

#when converted to integers, booleans convert to 1 for True, 0 for False
print(int(x_true)) #prints 1
print(int(x_false)) #prints 0

#### LISTS ####
### a list is exactly what it sounds like - a collection of valid python data values
### for example:

list1 = [1,2,3,4]

### lists can have different types of data:

list2 = [1, 3.2, 'hello']

### you can access values in a list using an index (always starting at 0)

print(list1[0]) # prints 1
print(list2[2]) # prints 'hello'

### you can add elements to a list as follows:

list2.append('this is a new element')

print(list2[3])

#### DICTIONARIES ####

### the below object is called a python 'dictionary'
### it contains KEY/VALUE pairs
### in this case, the keys are our names, and the values are grades

grades = {'ryan': 'B', 'tommy': 'B+', 'will': 'A-', 'falco': 'C'}

### you can access elements of a dictionary as follows:

print(grades['ryan']) ## prints 'B'
print(grades['falco']) ## prints 'C'

### you can assign new values to the dictionary as follows:

grades['potter'] = 'C+'

### below is another dictionary that maps keys (letter grades) into values (GPA)

grades_to_gpa = {'A+': 4.33, 'A': 4, 'A-': 3.66, 'B+': 3.33, 'B': 3, 'B-': 2.66, 'C+': 2.33, 'C': 2}


#### LOGICAL STATEMENTS ####
### one of the simplest operations in programming is to check if a certain logical statement is true or not
### for example, we can check if x_int from above is equal to 3:

print(x_int == 3) #prints False

### or we could check greater than or equal to:
print(x_int >= 3) #prints True


#### IF STATEMENTS ####
### we can use logical statements, together with a special operation called 'if' to run code only if a certain
### condition is met. we can also use the 'else' statement to do something different if the condition is not met
### for example:

if x_int == 3:
    print('x_int is equal to 3')
else:
    print('x_int is not equal to 3') #this will be printed

if x_int >= 3:
    print('x_int is greater than or equal to 3') #this will be printed
else:
    print('x_int is less than 3')

### we can evaluate an if statement at a boolean variable:

if x_true:
    print('x_true is True') #this will always be printed, since x_true is always true (unless we change it)

#### FOR LOOPS ####
### sometimes we want to loop through a list of python objects. we can achieve this with a 'for' loop
### for example:

for x in list1:
    print(x) # will print each value in the list

### we can also evaluate the list at the indices of the list as follows:

for i in range(len(list1)):
    print(list1[i]) # prints the same as the previous list

### note the use of range(len(list1))
### 'len' will return to the length of the list
### 'range' will return a list of integers from 0 to the integer provided minus 1
### for example:

print(len(list1)) #prints 4

for i in range(5):
    print(i) #prints 0,1,2,3,4


##### PROBLEM 1 ######
### write some code to create a new dictionary called 'gpa', using both the 'grades' dictionary
### and the 'grades_to_gpa' dictionary from above,  that contains key/value pairs for names and the corresponding gpa
### for example, the dictionary should have and entry for tommy that looks like: {'tommy': 3.33}
### hint: you can initialize an empty dictionary as follows: gpa = {}
### hint 2: use a for loop

############# CODE GOES HERE ######################





###################################################


##### PROBLEM 2 ######
### write some code to create a new list called 'good_students', using the newly created
### 'gpa' dictionary, that contains the names of all students that have at least a 3.33 gpa
### hint: you an initialize an empty list as follows: good_students = []
### hint 2: use an 'if' statement within a 'for' loop to check if the student has a high enough gpa


############# CODE GOES HERE ######################





###################################################

