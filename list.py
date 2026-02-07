# Creat List 
numbers = [1,2,3,4,5]
print (numbers)

# Access list elements
print("Orignal List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Add elements 
numbers.append(6)
numbers.insert(7,8)
print("List after addin elements:", numbers)

#Remove elements 
numbers.remove(1)
numbers.pop()
print("list after remove elements:", numbers)

# Short list elements 
numbers.sort()
print("Sorted list:",numbers)

# Reverse list elements 
numbers.reverse()
print("Reversed List:", numbers)