
class Student:
    def __init__(self, name, house, patronus):
        houses = ["Gryffindor", "Slythering", "Hufflepuff", "Ravenclaw"]
        if not name:
            raise ValueError("Missing Name")
        if house not in houses:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐦"
            case "Otter":
                return "🐿"
            case "Jack Russell terrier":
                return "🐶"
            case _: "🍌"

    def __str__(self):
        return f"{self.name} from {self.house}, {self.patronus}"


def main():
    student = get_student()
    print(student)
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
