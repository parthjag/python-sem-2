t1 = (16, 23, 57,45)
print("Tuple:", t1)
print("First element:", t1[0])
print("Last element:", t1[-1])

nested_tuple = (1, 2, (3, 4, 5), 6)
print("Nested Tuple:", nested_tuple)
print("Access nested element:",
nested_tuple[2][1])

t2 = (7, 8)
repeated_tuple = t2 * 3
print("Original Tuple:", t2)
print("Repeated Tuple:", repeated_tuple)

t3 = (100, 200)
t4 = (300, 400)
concatenated_tuple = t3 + t4
print("First Tuple:", t3)
print("Second Tuple:", t4)
print("Concatenated Tuple:", concatenated_tuple)