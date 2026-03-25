student_name=input("enter your name :")
student_marks=input("enter your marks :")
data=student_name +","+student_marks +"\n"
result=[]
file_data=open("student.txt" , "a")
file_data.write(data)
file_data.close()

file_open=open("student.txt", "r")
main_data=file_open.readlines()
file_open.close()
for i in main_data:
    part=i.strip()
    names=part.split(",")
    name=names[0]
    marks=int(names[1])
    result.append({"name":name,"marks":marks})


for i in result:
    if i["marks"]>50:
        print(i)