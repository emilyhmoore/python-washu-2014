import random
import timeit
import matplotlib.pyplot as plt
import numpy

def bubblesort(numbers):
	for number in range(len(numbers)-1):
		for i in range(len(numbers)-1):
			if numbers[i]>numbers[i+1]:
				placeholder=numbers[i]
				numbers[i]=numbers[i+1]
				numbers[i+1]=placeholder
	return numbers

def mergesort(numbers):
	if len(numbers)>1:
		midpoint=len(numbers)//2
		left=numbers[:midpoint]
		right=numbers[midpoint:]
	
		mergesort(left)
		mergesort(right)
	
		i=0
		j=0
		k=0
	
		while i<len(left) and j<len(right):
			if left[i]<right[j]:
				numbers[k]=left[i]
				i=i+1
			else:
				numbers[k]=right[j]
				j=j+1
			k=k+1
		while i<len(left):
			numbers[k]=left[i]
			i=i+1
			k=k+1
		while j<len(right):
			numbers[k]=right[j]
			j=j+1
			k=k+1
	
	return numbers

bubble_times=[]
merge_times=[]
for i in range(1,500):
	dat=[int(100*random.random()) for p in xrange(i)]
	bubstart=timeit.default_timer()
	bubblesort(dat)
	mergestart=timeit.default_timer()
	mergesort(dat)
	endtime=timeit.default_timer()
	
	bubble_times.append(mergestart-bubstart)
	merge_times.append(endtime-mergestart)
	
plt.plot(bubble_times, "r-", label = "Bubble Sort")
plt.plot(merge_times, "g-", label = "Merge Sort")
plt.ylabel("Time (seconds)")
plt.xlabel("N")
plt.title("Runtime of Bubble and Merge Sort")
plt.legend(loc='upper left') #gets label information from the plt.plot calls.
plt.show()




