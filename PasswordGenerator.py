import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','^','&','*','()',')']
# input("password will be generated")
alphabet1=int(input("enter the number of alphbet u need to generate"))
number1=int(input("enter the number of number u need to generate"))
symbol1=int(input("enter the number of symbol u need to generate"))
password=[]
for i in range(1,alphabet1+1):
    a=random.choice(alphabet)
    password.append(a)
for j in range(1,number1+1):
    b=random.choice(numbers)
    password.append(b)
for k in range(1,symbol1+1):
    c=random.choice(symbol)
    password.append(c)


(random.shuffle(password))
genrator=''.join(password)
print(genrator)