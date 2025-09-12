class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science

    def average(self):
        return (self.spanish + self.english + self.social + self.science) / 4

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social": self.social,
            "science": self.science
        }

def create_student_from_dict(data):
    return Student(
        data["name"],
        data["section"],
        float(data["spanish"]),
        float(data["english"]),
        float(data["social"]),
        float(data["science"])
    )
