def camelcase(strigs):
	count=1
	for i in range(len(strigs)):
		if(strigs[i].isupper()):
			count+=1
		else:
			continue 

	return count

print(camelcase("oneTwoThree"))
