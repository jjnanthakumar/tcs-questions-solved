class Traveller:
    def __init__(self, name, traveledCountry, age, countryFrom):
        self.name = name
        self.traveledCountry = traveledCountry
        self.age = age
        self.countryFrom = countryFrom


class TravelAgency:
    def __init__(self, travelerList):
        self.travelerList = travelerList

    def countTravelersTraveledCountry(self, country):
        return len(list(filter(lambda x: country in x.traveledCountry, self.travelerList)))

    def getTravelerTravelledMaxCountry(self):
        return max(self.travelerList, key=lambda x: len(x.traveledCountry)).name

    def print_data(self):
        print([obj.name for obj in self.travelerList])


if __name__ == "__main__":
    n = int(input())
    travelerObjects = []
    for _ in range(n):
        name = input()
        traveledCount = int(input())
        traveledCountry = [input() for _ in range(traveledCount)]
        age = int(input())
        countryFrom = input()
        T = Traveller(name=name, traveledCountry=traveledCountry,
                      age=age, countryFrom=countryFrom)
        travelerObjects.append(T)
    Agency = TravelAgency(travelerList=travelerObjects)
    countryName = input()
    print(Agency.countTravelersTraveledCountry(countryName))
    print(Agency.getTravelerTravelledMaxCountry())

