#A dictionary in Python is an ordered, mutable collection that stores key-value pairs.

#Syntax of a Dictionary:
#dictionary_name = {key1: value1, key2: value2, key3: value3}

#creating a dictionary
student={"name":"Rushindra Reddy","Age":21,"gender":"Male"}
print(student)
#Output: {'name': 'Rushindra Reddy', 'Age': 21, 'gender': Male}

#Accessing Values
print(student["name"]) #Output: Rushindra Reddy
print(student.get("name"))# most preferred way to access values

#Adding and updating:
student["college"]="ICFAI"
print(student)
#output:{'name': 'Rushindra Reddy', 'Age': 21, 'gender': 'Male', 'college': 'ICFAI'}

#removing items:
student.pop("Age")
print(student) #{'name': 'Rushindra Reddy', 'gender': 'Male', 'college': 'ICFAI'}

#removes last item:
student.popitem()
print(student)#{'name': 'Rushindra Reddy', 'gender': 'Male'}

#clear:
student.clear()
print(student)#{}