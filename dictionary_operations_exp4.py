dictionaries = {
"roll_no": 51,
"name": "Pragya",
"marks": 92
}

print("Dictionary:", dictionaries)
print("Marks:", dictionaries.get("marks"))
print()

dictionaries["marks"] = 90
dictionaries["grade"] = "A"
print("Updated Dictionary:", dictionaries)
print()

removed_value = dictionaries.pop("grade")
print("Removed Value:", removed_value)
print("After Removing 'grade':", dictionaries)
dictionaries.popitem()
print("After popitem():", dictionaries)
print()

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = dict1 | dict2
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)