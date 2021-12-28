# n=7
# a=0
# b=1
# sum=0
# for i in range(0,n):
#     print(sum)
#     a=b
#     b=sum
#     sum=a+b
def fibonacci(n):
    #end condition
    if n<=1:
        return n
    # recurssion
     
    return (fibonacci(n-1) + fibonacci(n-2))
   
print(fibonacci(7))

    
    
    
     