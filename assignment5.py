#input from user
n= int(input("how many numbers"))
lst=[]
for n in range (n):
    numbers= int(input("enter a number"))
    lst.append(numbers)
    print("sum of the numbers is:",sum(lst))

#smallest_largest
ls=[]
for i in range(5):
    num=int(input("enter the first number"))
    ls.append(num)
    ls.sort()
    print("smallest number is:",ls[-0])
    print("largest number is:",ls[-1])

#ascending_descending
val = eval(input("enter a list:"))
print("original list:",val)
val.sort()
print("ascending order list is:",val)
val.sort(reverse=True)
print("descending order list is:",val)

#list in tuple
t=(1,2,3,4)
ls=list(t)
print(ls)
print(type(1))

#deleted list
ls=[1,2,3,4,5,6,7,8,9,10]
del ls[1]
print(ls)