# import sys
# def max_recursion sys.getrecursionlimit()
# print(max_recursion)


# def hello():
#      print("hello")
#      hello()
# hello()
    

# def count_down(start):
#     """count_downfrom a number"""
#     print(start)
#     if start < 16:
#         count_down(start+1)
# count_down(0)
        

# def factor(n):
#     f=1
#     for i in range(1,10+1):
#         f=f*i
#     return f
# result= factor(5)
# print(result)
        

def factorial(n):
    """calculate the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))




