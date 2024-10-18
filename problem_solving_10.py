#convert the following dictionary into JSON format.
#student_data = {"name":"David","age":13,"marks":87}
import json
student_data = {"name":"David","age":13,"marks":87}
print(type(student_data))
data = json.dumps(student_data)
print(data)
print(type(data))

#access the value of age from the given data
#student_data = {"name":"David","age":13,"marks":87}
import json
student_data = """{"name":"David","age":13,"marks":87}"""
data1 = json.loads(student_data)
print(data1["age"])

#Pretty print the following JSON data.
#student_data = {"name":"David","age":13,"marks":87}
student_data = {"name":"David","age":13,"marks":87}
data = json.dumps(student_data,indent=4,separators=(",","="))
print(data)
