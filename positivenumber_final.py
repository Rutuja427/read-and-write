numlist1=[]
numlist2=[]
num1=int(input("enter the total elements of list1:"))
for i in range(1, num1+1):
	value=int(input("enter the values:"))
	numlist1.append(value)
	
print("list1", numlist1)
pos_num=list(filter(lambda x:x>0, numlist1))
print("posituve numbers are:",pos_num)
print('\n')

num2=int(input("enter the total elements of list2:"))
for i in range(1, num2+1):
	value=int(input("enter the values:"))
	numlist2.append(value)
print("list1", numlist2)
pos_num=list(filter(lambda x:x>0, numlist2))
print("posituve numbers are:",pos_num)
