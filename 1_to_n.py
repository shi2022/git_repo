def number(n):
    if n==1:
        print(1)
        return 
    else:
        
        number(n-1)
        print(n)
 
num=int(input())
print(number(num))