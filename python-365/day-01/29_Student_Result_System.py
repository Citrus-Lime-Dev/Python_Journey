def calculate_total(marks_01, marks_02, marks_03):
    return marks_01 + marks_02 + marks_03

def calculate_average(total , subjects):
    return total / subjects

def calculate_grade(avg):
    if avg > 100:
            return"Grade is amateurish"
    elif 90 <= avg <= 100:
            return"A"
    elif 80 <= avg < 90:
            return"B"
    elif 70 <= avg < 80:
            return"C"
    elif 60 <= avg < 70:
            return"D"
    elif 0 <= avg < 60:
            return"F"
    elif avg < 0:
            return"Rejected piece!!!"

name = input("Please enter your name: ")

number_of_subjects = 3

marks_1 = int(input("Please enter your marks in Maths: "))
marks_2 = int(input("Please enter your marks in English: "))
marks_3 = int(input("Please enter your marks Science: "))

if 0 <= marks_1 <= 100 and 0 <= marks_2 <= 100 and 0 <= marks_3 <= 100:
    sum_of_marks = calculate_total(marks_1, marks_2, marks_3)
    average = calculate_average(sum_of_marks, number_of_subjects)

    print(f"Total: {sum_of_marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {calculate_grade(average)}")
    print(f"Result: {'Pass' if average >= 40 else 'Fail'}")
else:
    print("Invalid input")
