# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"

class Doctor:
    def __init__(self, id, name, spec, fee):
        self.doctorId = id
        self.doctorName = name
        self.doctorSpec = spec
        self.consultationfee = fee


class Clinic:
    def __init__(self, doctorList):
        self.doctorList = doctorList

    def SearchByDoctorName(self, name):
        filtered = list(
            filter(lambda x: x.doctorName.lower() == name.lower(), self.doctorList))
        return filtered if filtered else None

    def findSpecializationbyId(self, doctorIds):
        data = {}
        for d in doctorIds:
            doctor = list(filter(lambda x: x.doctorId == d, self.doctorList))
            if doctor:
                data[d] = doctor[0].doctorSpec
            else:
                return None
        return data

if __name__ == "__main__":
    n = int(input())
    doctors = []
    for _ in range(n):
        doctors.append(Doctor(int(input()),input(),input(),int(input())))
    clinic = Clinic(doctors)
    name = input().lower()
    id_count = int(input())
    doctorIds = [int(input()) for _ in range(id_count)]
    searched = clinic.SearchByDoctorName(name)
    if searched is None:
        print("No Doctor Exists with the given Doctor Name")    
    else:
        for r in searched:
            print(r.doctorId)
            print(r.doctorName)
            print(r.doctorspec)
            print(r.consultationfee)
    spec = clinic.findSpecializationbyId(doctorIds)
    if spec is None:
        print("No Doctor(s) with the given ID")
    else:
        print('\n'.join(f'{k} : {v}' for k,v in spec.items()))
