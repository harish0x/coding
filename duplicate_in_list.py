def dublicate_in_list(a,b):
	if((len(a)==len(set(b))) and (len(set(a))==len(b))):
		return True 
	else:
		return False

a=[1,2,3,4]
b=[1,2,3,4]
print(dublicate_in_list(a,b))
