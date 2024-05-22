# def my_funtion():
#     local_var ="i'm local"
#     print(local_var)

# my_funtion()
# print(local_var)

global_var ="i'm global"

def show_global():
    global global_var
    global_var = "i'm overwriting you"
    print(global_var,"inside a function")

show_global()
print(global_var)




