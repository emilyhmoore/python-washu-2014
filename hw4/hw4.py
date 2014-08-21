##Note: not yet complete. 
class Node:
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next
	def __str__(self):
		return str(self.value)

##adapted and merged together from multiple sources including:
##http://www.danielacton.com/Data-Structures/Linked-List/Python/
##http://kkthegeek.wordpress.com/2010/05/06/linked-list-implementation-in-python/
##http://en.literateprograms.org/Singly_linked_list_%28Python%29

class LinkedList:
	def __init__(self, value):
		self.value=value
		self.head=Node(value)
		self.tail=self.head
		self.tail.next=None
		self.size=1
	
	def length(self): #Returns the length of the list
		return self.size
	
	def addNode(self, new_value): 
	#Takes a number and adds it to the end of the list
		node=Node(new_value, None)
		self.tail.next = node
		self.tail = node
		self.size+=1
		
	def addNodeAfter(self, new_value, after_node): 
	#Takes a number and adds it after the after_node
		new_node=Node(new_value)
		node=self.head
		location=after_node-1
		count = 0
		while count != location:
			node = node.next
			count+=1
		new_node.next=node.next
		node.next = new_node
		self.size+=1
	
	def addNodeBefore(self, new_value, before_node): 
	#Takes a value and adds before the before_node
		loc = self.head
		while tail.next != before_node:
			loc = loc.next
		addNodeAfter(new_value, loc)
		self.size+=1
	
	#Removes a node from the list
	##Node_to_remove should be an integer of the location of the node to remove.
	##e.g. if one wants to remove the second node, "2" should be entered.
	def remove_after(self, node_to_remove):
		node=self.head
		location=node_to_remove-2
		count = 0
		if location==-1:
			self.head=node.next
			self.size-=1
		else:
			while count != location:
				node = node.next
				count+=1
			node.next = node.next.next
			self.size-=1
		if node.next is None:
			self.tail = node
	
	def removeNodesByValue(self, value): 
	#Takes a value, removes all nodes with that value
		node=self.head
		location=1
		while location <= self.size:
			if node.value==value:
				self.remove_after(location)
			location+=1
			if node.next != None:
				node=node.next
	
	#def reverse(self): #Reverses the order of the linked list
	
	##for some reason calling str(ll) prints the list, then returns an error
	##while listname.__str__() returns the desired output.
	def __str__(self): #Displays the list in some reasonable way
		node=self.head
		while node != None:
			print str(node.value)
			node=node.next
	
	
	