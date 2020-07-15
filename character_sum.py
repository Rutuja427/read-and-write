def str_test(s):
	upper_case=[]
	lower_case=[]
	for i in s:
		if i.isupper():
			upper_case.append(i)
			u=len(upper_case)
		elif i.islower():
			lower_case.append(i)
			l=len(lower_case)
		else:
			pass
	print("sample string=",s)
	print("No. of upper case characters:", u)
	print("No. of loer case characters:", l)
str_test("The quick Brow Fox")