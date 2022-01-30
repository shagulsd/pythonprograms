print("hello")
print("shagul")

# reversed numbers
number=1234
rev=0
while(number>0):
    rem=number%10
    rev=rev*10+rem
    number=number//10
print(rev)

# leap year
year=int (input("enter the year"))
if(year % 400 == 0 and year % 100 == 0):
    print(year,"leap year")
else:
    print(year,"not a leap year")


# prime number
number= int(input("enter number"))
count=0

for i in range(1,number+1):
    if (number % i) == 0:
        count+= 1
if count== 2:
    print('prime number')
else:
    print('not a prime number')

largest three numbers
num1 = 14
num2 =12
num3 =10
if (num1>=num2 and  num1>=num3):
    largest =num1
elif (num2>=num3 and num2>=num1):
    largest=num2
else:
    largest =num3

print(largest)

































