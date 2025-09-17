class Student:
    def __init__(self, roll, name, course, gender, email):
        self._roll = roll # making self.roll protected modifier by using underscore in start
        self._name = name # making self.name protected modifier by using underscore in start
        self.course = course
        self.gender = gender
        self.email = email

    def attend_class(self):
        print(f"{self.name} is attending class")
    def appear_exam(self):
        print(f"{self.name} is appearing in exam")
    def result(self):
        print(f"{self.name} is pass in exam")
    def get_roll_number(self):
        return self._roll 
    def set_roll_number(self, new_roll):
        self._roll = new_roll
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name