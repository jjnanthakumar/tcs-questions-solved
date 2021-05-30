class Citizen:
    def __init__(self, citizenID, citizenName, citizenAge, isFronlineWorker, vaccineOptedFor, preference=None):
        self.citizenID = citizenID
        self.citizenName = citizenName
        self.citizenAge = citizenAge
        self.isFronlineWorker = isFronlineWorker.lower()
        self.vaccineOptedFor = vaccineOptedFor
        self.preference = self.setPreference()

    def setPreference(self):
        return self.citizenAge > 45 or self.isFronlineWorker == 'yes'


class VaccinationDrive:
    def __init__(self, citizenObjects):
        self.citizens = citizenObjects

    def getPreferredVaccinationCount(self):
        return len(list(filter(lambda x: x.preference, self.citizens))) or None

    def getCitizensAsPerVaccine(self, vaccineName):
        return sorted(filter(lambda x: x.vaccineOptedFor == vaccineName, self.citizens), key=lambda x: x.citizenAge) or None


# Driver Program
n = int(input())
citizenObjects = [Citizen(int(input()), input(), int(
    input()), input(), input().lower()) for _ in range(n)]
vaccinationDrive = VaccinationDrive(citizenObjects)
vaccine = input()
vaccinatedCount = vaccinationDrive.getPreferredVaccinationCount()
citizensbyVaccine = vaccinationDrive.getCitizensAsPerVaccine(vaccine)
print("Citizen not found" if citizensbyVaccine is None else '\n'.join(
    [f'{cit.citizenID}\n{cit.citizenName}\n{cit.citizenAge}' for cit in citizensbyVaccine]))
print("Preferred Citizen not found" if vaccinatedCount is None else vaccinatedCount)
