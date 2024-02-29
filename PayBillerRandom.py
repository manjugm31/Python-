import random
name=input("enter your friends name")
nameSplit=name.split(" ")
# choice=random.choice(nameSplit)
# print(choice +"has to pay the bill")
length=len(nameSplit)
choice=random.randint(0,length-1)
print(nameSplit[choice] +"  has to pay the bill")