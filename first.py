# # # a=int(input("enter the number:"))
# # # if a % 2 == 0:
# # #     print("Even number is " + str(a))
# # # else:
# # #     print("Odd number " + str(a))

# # a = [2, 4, 3, 5, 1, 6]
# # # Sort and find smallest and largest
# # a.sort()
# # print(str(a[0]) + " is the smallest")
# # print(str(a[-1]) + " is the largest")

# # # Sum of array
# # a = [1, 2, 3, 4, 5, 6, 7]
# # sum = 0
# # for b in a:
# #     sum = sum + b
# # print(str(sum) + " is the sum")

# # pattern 
# for a in range(5):
#     for b in range(5):
#         print("*",end="")
#     print()

#pattern2
# for a in range(5):
#     for b in range(5):
#         if a>=b:
#             print("*",end="")

#     print()

#pattern3
# for a in range(5):
#         for b in range(5):
#             if a<=b:
#                 print("*",end="")
#         print()

# #average
# size=int(input("enter the size of array:"))
# arr=[]
# for i in range(size):
#      arr.append(int(input("enter elements"+str(i))))
# print(arr)
# sum=0
# size=len(arr)
# print(size)
# for j in (arr):
#      sum=sum+i
# print(sum)
# print(sum/size)    


#linear search
size=int(input("enter the length of array"))
arr=[]
for i in range( size):
    arr.append(int(input("enter the element"+ str(i))))
print(arr)
element=int(input("enter the elemet u need to find"))
found=False
for j in arr:
    if(arr[j]==element):
        found=True
        break
if(found):
    print("found")
else:
    print("not found")    







