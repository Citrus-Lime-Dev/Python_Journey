marks = int(input("Enter your marks: "))

match marks:
    case _ if marks > 100:
        print("Grade is amateurish")
    case _ if 90 <= marks <= 100:
        print("A grade")
    case _ if 80 <= marks < 90:
        print("B grade")
    case _ if 70 <= marks < 80:
        print("C grade")
    case _ if 60 <= marks < 70:
        print("D grade")
    case _ if 0 <= marks < 60:
        print("F grade")
    case _ if marks < 0:
        print("Rejected piece!!!")
