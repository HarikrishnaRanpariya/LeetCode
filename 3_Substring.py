import numpy as np

def find_letter(letter, lst):
    return any(letter in word for word in lst)
def main():
	temp = 0
	c = 1
	Flag=0
	sList = list("pwwkew")
	print("pwwkew")
	if len(sList) > 1:	
		for i in range(len(sList)):
			c=1
			for j in range(i+1,len(sList)):
				print("j%d=%c, list=" %(j,sList[j]))
				print(sList[i:j])
				s = find_letter(sList[j], sList[i:j])
				if s == True:
					print("+")
					break
				else:
					c = len(sList[i:j])+1
			if temp < c:
				temp = c
				print("temp =%d" %temp)
	else:
		temp=len(sList)
		print("lcount is %d" %temp)
	print("fcount is %d" %temp)

main()

