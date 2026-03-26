# Student_name="mukesh"
# Student_age=20
# Student_grade="A"
# print("Student Name:", Student_name)
# print("Student Age:", Student_age)
# print("Student Grade:", Student_grade)
# new_age=21
# Student_age=new_age

# name="mukesh"
# age=20
# district="Panchkula"
# print("My name is ", name )
# print("my age is " ,age , "years " )
# print(" i am from ", district)


# game_name="Assassin's Creed Origins"
# release_year=2017
# Publisher="Ubisoft"
# rating=9.5
# print(game_name,"is one of my favortie games" )
# print("this was released in the year ", release_year)
# print("the publisher of this game is ", Publisher)
# print( "i would rate this game",rating ,"out of 10")

# print("twinkle twinkle little star \n how i wonder what you are ")
# num = "45"
# number=int(num)
# new_num= number + 10
# print (number)
# print("the new number is ", new_num)
# users_food=input("what is your favorite food :")
# print("i also like",users_food) 

# num1=int(input("enter the first number :"))
# num2=int(input("enter the second number :"))
# sum=num1+num2
# print("the sum of  2 numbers is: ",sum)
# diffrence= num1-num2
# print("the diffrence of 2 numbers is: ",diffrence)
# product=num1*num2
# print("the product of 2 numbers is: ",product)
# qoutient=num1/num2
# print("the qoutient of 2 numbers is: ",qoutient)

# print("this is a line in this line i am using the escape sequence to print this upcoming line\n in the next line ")
# print( "the upcoming line is the under the doble couteded \" this is in the dobule qoute \" this is after the qoutes")
# print("this upcoming line has a tab of space ->\t<- this is after the tab" )

# print(" he says \"python is amazing\"")
# print("this file path is C:\\Users\\mukesh\\mac\\")
# num1=2
# squre=num1*3
# print("the squre of ", num1, "is ", squre)
# num2="5"
# num3=5
# print(num2==num3)
# marks=int(input("enter your marks :"))
# if marks>=90:
#     print("you got A grade")
# elif marks>=80:
#         print("you got B grade")
# elif marks>=70:
#       print("you got C grade")
# elif marks>=60:
#       print("you got D grade")
# else:
#       print("you got F grade better luck next time")
# 9 or above → Masterpiece game
# 7–8.9 → Great game
# 5–6.9 → Average game
# Below 5 → Bad game

# game_rating=float(input("enter the game rating out of 10:"))
# if game_rating>=9 and  game_rating <=10:
#     print("Masterpiece game")
# elif game_rating>=7 and game_rating<9:
#     print("great game")
# elif game_rating>=5 and game_rating<7:
#     print("average game")
# else:
#     print("bad game")
# for i in range(1,11):
#     print(i)
# i = 1
# num = int(input("Enter a number to print its multiplication table: "))

# while i <= 10:
#     product = num * i
#     print(num, "x", i, "=", product)
#     i += 1

# num = int(input("enter a number:"))
# while True:

#     if num==0:
#       break 
#     if num%2==0:
#      num=int(input("enter a numbr"))
#      continue
#     else:
#      print("you enterd odd number", num)
#     num=int(input("enter a number"))


# def is_even(num):
     
#   if num>0:
#         return "positive"
#   elif num <0:
#        return"negative"
#   else:
#       return "zero"



# num=int(input("enter a number"))
# num1=is_even(num)
# print(num1)

# ---------- FUNCTIONS ----------
def load_students():
    result = []
    try:
        data = open("student.txt", "r")
        main_data = data.readlines()
        data.close()
    except FileNotFoundError:
        print("File not found!")
        return []

    for i in main_data:
        parts = i.strip()
        name = parts.split(",")
        result.append({"name": name[0], "marks": int(name[1])})
    return result


class StudentManager:
    def __init__(self):
        self.students = load_students()

    def save_students_to_file(self):
        f = open("student.txt", "w")
        for student in self.students:
            data = student["name"] + "," + str(student["marks"]) + "\n"
            f.write(data)
        f.close()

    def display_student(self, student):
        print("Name:", student["name"], "| Marks:", student["marks"])

    def add_student(self):
        name = input("Enter student name: ")

        while True:
            try:
                marks = int(input("Enter marks: "))
                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100")
                    continue
                break
            except ValueError:
                print("Enter valid marks!")

        # ✅ update list first
        self.students.append({"name": name, "marks": marks})

        # ✅ then save to file
        self.save_students_to_file()

        print("Student added successfully")

    def view_students(self):
        if len(self.students) == 0:
            print("No students available")
            return

        for student in self.students:
            self.display_student(student)

    def search_student(self):
        if len(self.students) == 0:
            print("No students available")
            return

        input_name = input("Enter name to search: ")
        found = False

        for student in self.students:
            if input_name.lower() == student["name"].lower():
                self.display_student(student)
                found = True

        if not found:
            print("Student not found")

    def delete_student(self):
        if len(self.students) == 0:
            print("No students available")
            return

        delete_input = input("Enter student name to delete: ")
        found = False

        for student in self.students:
            if delete_input.lower() == student["name"].lower():
                self.students.remove(student)
                print("Student deleted successfully")
                found = True
                break

        if not found:
            print("Student not found")
            return

        self.save_students_to_file()

    def update_student(self):
        update_input = input("Enter student name: ")

        while True:
            try:
                update_marks = int(input("Enter updated marks: "))
                if update_marks < 0 or update_marks > 100:
                    print("Marks must be between 0 and 100")
                    continue
                break
            except ValueError:
                print("Enter valid marks!")

        found = False

        for student in self.students:
            if update_input.lower() == student["name"].lower():
                student["marks"] = update_marks
                print("Updated successfully")
                found = True
                break

        if not found:
            print("Update failed!")
            return

        self.save_students_to_file()


# ---------- MAIN PROGRAM ----------
manager = StudentManager()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update")
    print("6. Exit")

    try:
        opt = int(input("Enter choice: "))
    except ValueError:
        print("Enter valid input!")
        continue

    if opt == 1:
        manager.add_student()
    elif opt == 2:
        manager.view_students()
    elif opt == 3:
        manager.search_student()
    elif opt == 4:
        manager.delete_student()
    elif opt == 5:
        manager.update_student()
    elif opt == 6:
        print("Exited successfully")
        break
    else:
        print("Invalid choice")