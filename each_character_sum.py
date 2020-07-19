from collections import Counter
test_str=input("enter the string:")
char_sum = {} 
  
for i in test_str: 
    if i in char_sum: 
        char_sum[i] += 1
    else: 
        char_sum[i] = 1
	
    res=Counter(char_sum)
# printing result  
print ("Count of all characters in given string is:\n " + str(res))
	

