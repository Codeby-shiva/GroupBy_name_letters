# students list 
student_list = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", 
    "Sai", "Aanya", "Diya", "Ananya", "Pari", 
    "Rohan", "Kabir", "Aryan", "Ishaan", "Dhruv", 
    "Aaradhya", "Avani", "Shanaya", "Siya", "Navya", 
    "Krishna", "Vedant", "Reyansh", "Atharva", "Aarav", 
    "Krish", "Myra", "Kiara", "Prisha", "Aliya",
    "Ansh", "Ayaan", "Darsh", "Kabir", "Madhav", 
    "Diya", "Sara", "Saanvi", "Samaira", "Zoya"
]


import string

Group = {
"Group1" : [i for i in student_list  if  i.startswith(("A", "B", "C", "D"))],
"Group2" : [i for i in student_list  if  i.startswith(("E", "F", "G", "H"))],
"Group3" : [i for i in student_list  if  i.startswith(("I", "J", "K", "L"))],
"Group4" : [i for i in student_list  if  i.startswith(("M", "N", "O", "P"))],
"Group5" : [i for i in student_list  if  i.startswith(("Q", "R", "S", "T"))],
"Group6" : [i for i in student_list  if  i.startswith(("U", "V", "W", "X"))],
"Group7" : [i for i in student_list  if  i.startswith(("Y", "Z"))]

}

for i in range (1,8):  
    print(f"Group{i} = ", Group[f"Group{i}"])
    
    

    