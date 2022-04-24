# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Person:
    def __init__(self, pName, pHeight, pWeight, pBmi=0, pBmi_status=""):
        self.pName = pName
        self.pHeight = pHeight
        self.pWeight = pWeight
        self.pBmi = pBmi
        self.pBmi_status = pBmi_status
        # self.calculateBmi()

    def calculateBmi(self):
        self.pBmi = self.pWeight//(self.pHeight**2)


class Society:
    def __init__(self, bmi_status, personObjects):
        self.bmi_status = bmi_status
        self.personObjects = personObjects

    def findBmistatus(self, person):
        return ''.join(k for k, v in self.bmi_status.items() if person.pBmi >= v[0] and person.pBmi <= v[1])

    def getRespectivePersons(self, name):
        return list(filter(lambda x: x.pName == name and x.pBmi != 0, self.personObjects))

    def calculateBmiAndStatusByName(self, name):
        curPersons = list(
            filter(lambda x: x.pName == name, self.personObjects))
        if not curPersons:
            return False
        for person in curPersons:
            person.calculateBmi()
            # set bmi status
            person.pBmi_status = self.findBmistatus(person)
        return True

    def removeInvalidPersons(self, bmi):
        return list(filter(lambda x: x.pBmi < bmi, self.personObjects))


n = int(input())
person_objects = [Person(input(), int(input()), int(input()))
                  for _ in range(n)]
no_ofkeys = int(input())
data = {input(): (int(input()), int(input())) for _ in range(no_ofkeys)}
society = Society(data, person_objects)
name = input()
bmi = int(input())
if society.calculateBmiAndStatusByName(name):
    for person in society.getRespectivePersons(name):
        print(person.pBmi, person.pBmi_status)
else:
    print('No Person Exists')
for person in society.removeInvalidPersons(bmi):
    print(person.pName, person.pBmi)
