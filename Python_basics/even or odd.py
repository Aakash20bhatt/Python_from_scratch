n=int(input("Enter the number:"))
#Logic 1
'''if n%2==0:
    print("even number")
else:
    print("odd number")
'''

#Logic 2
'''
if not n%2 :
    print(" even")
else :
    print("odd")
'''
#Logic 3
'''b=n//2
if n==b*2:
    print("Even")
else:
    print("odd")
'''
#Logic 4
'''a=n/2
b=n//2
if a==b:
    print("Even")
else:
    print("odd")
'''
#Logic 5
'''a=bin(n)
if a[-1]=="1":
    print("odd")
else:
    print("even")
'''
#Logic 6
'''c=("even"if n&1==0 else "odd")

print(c)
'''
#Logic 7
'''a=n//2
b=0
for i in range(a):
    n=n-2
    if n==0:
        print("Even")
        break
    
    elif n==1:
        print("Odd")

    break
'''
#Logic 8
'''if n|1==n+1:
    print("Even")
else:
    print("odd")
'''
#Logic 9

'''print("Even"if (n>>1)<<1==n else "Odd")'''
#Logic 10
'''print("Even" if(n//2)*2==n else "odd")'''
#Logic 11

'''l=['even','odd']
 
print(l[n%2]) '''   

#Logic 12

'''print(n%2 and "odd" or "even")'''





