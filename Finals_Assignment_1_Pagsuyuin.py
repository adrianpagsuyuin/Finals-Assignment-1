#Adrian Pagsuyuin
#List: Student Names

students = ["Ruzzel", "Valencia", "Yape"]
#Add 1 new item
students.append("Rico")

#Remove 1 item
students.remove("Ruzzel")

#Sort the list
students.sort()

print("List of Students")
print(students)

#Tuple: School Info
print("\nTuple: School Details")
school_info = ("Pateros Technological College", 2026, True)

#Try modifying one element
#Para mabago, kailangan muna iconvert sa list
temp_list = list(school_info) #Convert to List
temp_list[1] = 2027 #Modified na siya dito kaya change value
school_info = tuple(temp_list) #Locked (Convert back to Tuple)
print(school_info)
#Dahil ang tuple ay immutable, kailangan muna itong i-convert sa list (na mutable o pwedeng baguhin) gamit ang list() function.
#Pagkatapos mabago ang value, ibinabalik siya sa tuple() para maging immutable o protected ulit.

#Set
print("\nSet: Subjects")
subjects = {"FIL 2", "WS 101", "Pathfit"}

#Add a value
subjects.add("Programming")

#Remove a value
subjects.remove("Pathfit")

#Print the updated set
print(subjects)

#Dictionary
print("\nDictionary: My Profile")
my_profile = {"name": "Adrian", "age": 17, "passed": True}

#Add a new key "grade"
my_profile["grade"] = 1.28
#Update your "age"
my_profile["age"] = 19
print(my_profile.keys())
