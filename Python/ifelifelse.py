new_student = "kim"
print(new_student)
if new_student == "frank":
    print("The student's name is frank")
elif new_student == "niko":
    print("niko is not a new student")
elif new_student == "benz":
    print("benz is not a new student")
elif new_student == "bett":
    print("bett is not a new student")
elif new_student == "naomy":
    print("naomy is not a new student")
elif new_student == "gladwwel":
    print("gladwel is not a new student")
                   


else:
    print(f"{new_student} is not our student")    
   

age = 16
height = 160
weight = 50
if age > 18 and height >= 160:
    print("eligible for military service,")
elif age >= 18 and weight >= 50:
    print("also eligible for military service")



age = 16
height = 180

if age > 18 and height > 170:
    print("eligible for military service,")
elif age < 18 and height > 170:
    print("not eligible for military service due to age,")
else:
    print("other condion appy")




is_logged_in = False
is_admin = False

if is_logged_in and is_admin:
    print("admin dashboard") 
elif is_logged_in and not is_admin:
    print("regular user page")

else:
    print("please log in")



height = 170
is_bribe = True

if height >= 170 or  is_bribe:
    print("eligible for military service")

else:
    print("not eliigible")

sum = 0

for i in range(1 ,21):
    if i % 2 == 0:  
       sum += i
    print("the sum of all even number  between 1,20 is:",sum)


word = "PYTHON"
lowercase = word.lower()
print(lowercase)



fruits = ["apple","banana","orange","three tomatoes"]
for fruit in fruits:
    if fruit == "orange":
        break
    print(fruit)

for i , fruit in enumerate(fruits):
    print(i+1,fruit)   

for i in range(1,20):
    for x in "abcdef":
        print(i,x)
    
         FUNCTION   
   ******************
def name_function():
    print("nicholas")
name_function()
    
def sum(num1=0,num2=0):
    if num1 is not int or num2 is not int:
        return
    return num1 +num2
# print(sum(2,5))
result = sum(25,"is an integer")
print(result)

             f (string)
          ****************
name = "dolly"
age = 19

user_string = f"hello{} you are {} years old."(name,age)
print(user_string)


def multiple_items(*student):
    print(student)
    print(type(student))

multiple_items("nicholas", "bett","benz",8 ,["gladwel","naomi"])

               key value == (kwargs)
      *************************************
def mult_name_items(**kwargs):       
    print(kwargs)
    print(type(kwargs))

mult_name_items(first="nicholas", last="bett")


def mult_items(name,age,admission):
    print(name,admission)
mult_items("bett", 21,"AAW3R4")



def sentence(*args):
    print(args)
sentence("ben",{"language": "python", "framework": "flask", "semester":1},3,["morning lesson","midday lesson","evening lesson"])

sentence = sentence.replace('(','') .replace('{','') .replace('}', '') .replace("[", '') .replace(']', '') .replace(')','')
print(sentence)































































