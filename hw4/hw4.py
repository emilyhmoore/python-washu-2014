##Note: not yet complete. 
class Node:
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next
	def __str__(self):
		return str(self.value)

##adapted and merged together from multiple sources:
##http://www.danielacton.com/Data-Structures/Linked-List/Python/
##
class LinkedList:
	def __init__(self, value):
		self.value=value
		self.head=Node(value)
		self.tail=self.head
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
	
	#def removeNode(self, node_to_remove): #Removes a node from the list
	
	#def removeNodesByValue(self, value): #Takes a value, removes all nodes with that value
	
	#def reverse(self): #Reverses the order of the linked list
	
	#def __str__(self): #Displays the list in some reasonable way
	
	
	