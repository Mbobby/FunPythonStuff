#joins the left and right side of the list and returns an ordered list
def merge(list_1, list_2):
	total = len(list_1) + len(list_2)
	total_list = []
	l1_index = 0
	l2_index = 0
	for i in range(0,total, 1):
		if((l1_index < len(list_1)) and (l2_index < len(list_2))):
			if(list_1[l1_index] < list_2[l2_index]):
				total_list.append(list_1[l1_index])
				l1_index += 1
			elif(list_2[l2_index] < list_1[l1_index]):
				total_list.append( list_2[l2_index])
				l2_index += 1
			else:
				total_list.append(list_1[l1_index])
				l1_index += 1
		elif(l1_index >= len(list_1)):
			total_list.append(list_2[l2_index])
			l2_index += 1
		elif(l2_index >= len(list_2)):
			total_list.append(list_1[l1_index])
			l1_index += 1

	return total_list

#main mergesort function to break the list into parts and use recursion to sort it
def mainmerge(list_):
	if len(list_) < 2:
		return list_
	else:
		middle = len(list_)/2
		left = mainmerge(list_[:middle])
		right = mainmerge(list_[middle:len(list_)])
	return merge(left, right)

def main():
	list_ = [12,1,3,4,5,6,7,9,10,2,8,24,19,14,5,9,16,15]
	print mainmerge(list_)

if __name__ == "__main__":
	main()
