class Employees():
    def __init__(self, name, gender, age, title,):
        self.name = name
        self.gender = gender
        self.age = age
        self.title = title


    def post(self):
        print("I am a", self.title)

    
if __name__ == "__main__":

    employee1 = Employees("Jane", "Female", 30, "Junior")
    employee1.post()

    employee2 = Employees("Andrew", "Male", 45, "Manager")
    employee2.post()
    print("My name is",employee2.name.)