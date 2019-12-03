#indentation matters!

#declaration of variables
answer = 42
name = "PythonBo"

#type hinting
def add_numbers(a: int, b: int) -> int:
    return a + b 

#Defining a integer and floats
answer = 42
pi = 3.14159 #can add answer + pi and it will return a float. Dont have to worry about types

#converting types
int(pi) #3
float(answer) #42.0

#strings
hello = 'hello world'
hello = "hello world"
hello = """hello world""" #All of these are the same

"hello".capitalize() #Hello
"hello".replace("e","a") #hallo
"hello".isalpha() #true
"123".isdigit() #true
"some,csv,values".split(",") #["some", "csv", "values"]

name = "PythonBo"
machine = "HAL"

"Nice to meet you {0}. I am {1}".format(name, machine) #Nice to meet you PythonBo. I am HAL
f"Nice to meet you {name}. I am {machine}".format(name, machine) #Nice to meet you PythonBo. I am HAL
#if you want to use string interpolation must put f infront of string

#booleans
python_course = True
java_course = False

int(python_course) #1
int(java_course) #0
str(python_course) #"true"

aliens_found = None #same as null

#if statements --> no curly braces or parenthesis
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

if not python_course:
    print("This will not run")

#conditionals
number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute")

#Ternary if statements
a = 1
b = 2
print("bigger") if a > b else print("smaller")

#lists aka arrays
student_names = ["Mark", "Joe" , "Bob"]
#                  0       1       2
#                 -3      -2      -1
student_names[0] #Mark
student_names.append("Homer") #add to the end
"Mark" in student_names #true
len(student_names) #4 elements len is length

del student_names[2] #deletes Bob

student_names[1:] #return ["Joe", "Homer"]
student_names[1:-1] #returns ["Joe"]

#loops

for name in student_names:
    print("Student name is {0}".format(name))

x = 0
for index in range(10):
    x += 10 #x = x + 10
    print("The value of X is {0}".format(x))

#range can take in 3 arguments (start, stop, increment)
#example
for index in range(5,10,2): #[5,7,9]
    print("index is {0}".format(index))
#Break and Continue
#Add the break keyword to stop a loop
#if you want to stop executing code in an iteration use the word continue and it will skip to the next iteration

x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1

#Dictionaries aka objects
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["name"] #"Mark"
student.get("last_name", "Unknown") #Will try to get the last_name key
#if there is no last_name then it will default to the second argument which
#we put as "Unknown"

student.keys() #gives you list of keys
student.values() #gives you a list of values
student["name"] = "James" #changes name mark to james
del student["name"] #deletes this key and value

#Exceptions

try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding last_name")
except TypeError as Error:
    print("I can't add these two together")
    print(error)
except Exception:#all errors
    print("Unkown Error")

print("This code executes!")

#Other Data Types
#complex
#bytes
#bytearray
#tuple a list of values that dont change
#set
#frozenset