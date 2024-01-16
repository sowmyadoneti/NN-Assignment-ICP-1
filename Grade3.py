class_score = float(input("Enter the class score: "))
if 90 <= class_score <= 100:
    grade = 'A'
elif 80 <= class_score < 90:
    grade = 'B'
elif 70 <= class_score < 80:
    grade = 'C'
elif 60 <= class_score < 70:
    grade = 'D'
else:
    grade = 'F'
print(f"The letter grade for the class score {class_score} is: {grade}")