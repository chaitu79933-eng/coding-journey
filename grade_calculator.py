print("=== student grade calculator ===")
name = input("enter your name: ")
maths = float(input("enter your maths marks: "))
physics = float(input("enter your physics marks: "))
chemistry = float(input("enter your chemistry marks: "))
english = float(input("enter your english marks: "))
python = float(input("enter your python marks: "))
total  = maths + physics + chemistry + python
average = total/4
print("total marks:", total)
print("average marks:", average)
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print()    
print("student name:", name)
print("total marks:", total)
print("average marks:", average)
print("grade:", grade)
