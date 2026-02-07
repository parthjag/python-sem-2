# create and accesss dictionary elements
student = {
    "roll_no":"101",
    "name":"Amit",
    "marks":85
}
print ("Dictionary:",student)
print("Name:",student["name"])
print("Marks:",student.get("marks"))
print()

# update dictionary 
print("Update Dictionary")
student["marks"]=90
student["grade"]="A"
print("Update Dictionary:", student)
print()

# removing elements
print("Removing Elements")
removed_value=student.pop("grade")
print("Removed Value:",removed_value)
print("After removing 'grade':",student)

student.popitem()
print("After popitem():",student)
print()

# merging dictionaries 
print ("Merging Dictionaries")
dict1= {"a":1,"b":2}
dict2= {"c":3,"d":4}

merged_dict=dict1 | dict2
print("Merging dictionaries")
dict1={"a,"}