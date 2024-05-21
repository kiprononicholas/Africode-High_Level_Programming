# try:
#     result = 56 / 0
# except ZeroDivisionError:
#     print("input cannot be divided by zero")



# try:
#    x = int(input("enter an number: "))
#    y = 1 / x 
# except(ZeroDivisionError,ValueError):
#    print("invalid input")
   


# try:
#     risky_oparatioin()
# except Exception as e:
#     print(f"an error occured: {e}")

def validate_age(age):
 if age <18:
    raise ValueError("age must be 18 or older")
 else:
    return True

try:
  validate_age(20)
except ValueError as e:
  print(e)

else:
  print("meets mininum age")

finally:
  print("i always run no matter what")









