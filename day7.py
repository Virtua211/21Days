class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name:", self.name, " Age:", self.age, " Grade:", self.grade)

students = []

while True:
    print("欢迎使用学生信息管理系统")
    print("1. 添加学生信息")
    print("2. 查看学生信息")
    print("3. 退出")

    choice = int(input("输入你的选择: "))

    if choice == 1:
        name = input("输入姓名: ")
        age = int(input("输入年龄: "))
        grade = input("输入年级: ")
        students.append(Student(name, age, grade))
        print("添加成功!")
    elif choice == 2:
        for student in students:
            student.display()
    elif choice == 3:
        break
    else:
        print("选项错误，请重试")
