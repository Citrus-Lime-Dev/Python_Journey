def calculate_grade(marks):
    if marks > 100:
            return "Grade is amateurish"
    elif 90 <= marks <= 100:
            return "A"
    elif 80 <= marks < 90:
            return "B"
    elif 70 <= marks < 80:
            return "C"
    elif 60 <= marks < 70:
            return "D"
    elif 0 <= marks < 60:
            return "F"
    elif marks < 0:
            return "Invalid!!!"
    return None


score = int(input("Enter your score: "))
print(calculate_grade(score))