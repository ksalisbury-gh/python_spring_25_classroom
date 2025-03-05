grade = int(input("Enter the numeric grade: "))

if grade < 59:
    letter = "F"
elif grade < 69:
    letter = "D"
elif grade < 79:
    letter = "C"
elif grade < 89:
    letter = "B"
elif grade < 100:
    letter = "A"
else:
    print("ERROR: Invalid number.")

print(f"The letter grade is: {letter}")