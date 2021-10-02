import re
class School:
    def __init__(self, uniqueId, stateCode, subjects):
        self.uniqueId = uniqueId
        self.stateCode = stateCode
        self.subjects = subjects


def remove_schools(schools, subjectsCount):
    return list(filter(lambda x: len(x.subjects)>=subjectsCount, schools))

def clean_statecode(schools):
    for scl in schools:
        res = re.sub(r'[^a-zA-Z0-9]+','',scl.stateCode)
        scl.stateCode = res if scl.stateCode !=res else 0
    return list(filter(lambda x:x.stateCode,schools))


if __name__ == "__main__":
    n = int(input())
    schoolObjects = []
    for _ in range(n):
        school_id = int(input())
        state_code = input()
        num_subjects = int(input())
        subjects = [input() for _ in range(num_subjects)]
        schoolObjects.append(School(school_id, state_code, subjects))
    subinpCount = int(input())

    updatedSchools = remove_schools(schoolObjects, subinpCount)
    print("Updated School List:")
    for ele in updatedSchools:
        print(ele.uniqueId, len(ele.subjects))
    obj = clean_statecode(schoolObjects)
    if not obj:
        print("All State Codes are Valid.")
    else:
        print("Updated State Codes:")
        for ob in obj:
            print(ob.uniqueId, ob.stateCode)
    


