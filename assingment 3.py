# Q-1
vowels=['a','e','i','o','u']
print(vowels)
# Q-2
New=['x','y','z']
Add=New + vowels
print(Add)
# Q-3
Num=[1,0,1,5,2,6,2,5,3,0,3]
print(Num.count(0))

# Q-4.
Numbers=[30,26,25,20,15,10,3]
Numbers.sort()
print(Numbers)

# Q-5
A=[3,10,15,20]
B=[25,26,30]
C=A+B
C.sort()
print(C)

# Q-6
Numbers=[3,10,15,20,25,26,30]
count1=0
count2=0
for i in Numbers:
    if not i % 2:
        count1=count1+1
    else:
        count2=count2+1
print("Even Numbers=",count1)
print("Odd Numbers=",count2)

# Q-7.
A=("10,15,20")
B=reversed(A)
print(tuple(B))

# Q-8
A=[4,6,15,85,100]
print('Maximum is=',max(A))
print('Minimum is=',min(A))

# Q-9
string="varun"
print(string.upper())

# Q-10
str="123Hello456"
print(str.isnumeric())

# Q-11
string='Hi'
print(string.replace('Hi','Hello'))
