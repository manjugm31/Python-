def Primenumber(num):
    count=0
    for i in range(1,num+1):
        
        if num%i==0:
            count=count+1
    if count ==2:
        print("yes u have entered prime number")
        
    else:
        print("no sorry!! its not prime number")  
         
        
num=int(input("enter the number="))
Primenumber(num)