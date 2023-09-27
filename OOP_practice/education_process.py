import random


class Person:
    possible_sex = {'мужской', 'женский'}
    def __init__(self, name:str, age:int, sex:str):
        self.name = name
        self.age = age
        if sex in self.possible_sex:
            self.sex = sex
        else:
            raise NameError('Неверный пол')

class Teacher(Person):
    students_taught: int = 0

    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age, sex)


    def teach(self, topic: str, *args):
        for student in args:
            student.take(topic)
            self.students_taught += 1

class Students(Person):
    def __init__(self,  name: str, age: int, sex: str):
        self.knowledge = []
        super().__init__(name, age, sex)

    def __len__(self):
        return len(self.knowledge)

    def take(self, topic: str):
        return self.knowledge.append(topic)

    def forget(self):
       if self.knowledge:
            self.knowledge.pop(random.randrange(len(self.knowledge)))


class StudyMaterial:
    def __init__(self, *args):
        self.topics = list(args)

    def __len__(self):
        return len(self.topics)


themes = StudyMaterial("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher('Виктор Леонидович', 53, 'мужской')
# students_data = Students()

students_data = (('Анна Смирнова', 20, "женский"),
                 ('Петр Петров', 25, "мужской"),
                 ('Мария Иванова', 22, "женский"),
                 ('Алексей Сидоров', 24, "мужской"))

students = [Students(*data) for data in students_data]

for theme in themes.topics:
    students_set = random.sample(students, k=random.randint(1, len(students)))
    teacher.teach(theme, *students_set)

for student in students:
    print(student.knowledge)

for student in students:
    student.forget()

print('-' * 30)

for student in students:
    print(student.knowledge)
    print(len(student))