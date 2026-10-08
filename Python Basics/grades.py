grades = [85, 78, 89, 76, 88]

#Adding a new grade
grades.append(96)

# Calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"Average Grade: {average_grade: .2f}")

#Finding the highest and lowest grade
highest_grade = max(grades)
lowest_grade = min(grades)
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")