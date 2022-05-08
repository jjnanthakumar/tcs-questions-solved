# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Associate:
    def __init__(self, id, grade, skill):
        self.id = id
        self.grade = grade.lower()
        self.skill = skill.lower()
class Project:
    def __init__(self, associate_list, skill_requirement):
        self.associate_list = associate_list
        self.skill_requirement = skill_requirement
            
    def validate_resource(self, associate_object):
        associate_ids =  list(map(lambda x:x.id,self.associate_list))
        associate_skill_count = len(list(filter(lambda x:x.skill==associate_object.skill, self.associate_list)))
        required_count = self.skill_requirement.get(associate_object.skill,0)
        if associate_object.id in associate_ids:
            return False,associate_skill_count
        elif associate_object.skill not in self.skill_requirement:
            return False,associate_skill_count
        elif associate_skill_count>=required_count:
            return False,associate_skill_count
        else:
            return True,associate_skill_count

# main function
if __name__ == "__main__":
    N = int(input())
    associates = [Associate(input(),input(),input()) for _ in range(N)]
    skill_requirements = {input().lower():int(input()) for _ in range(int(input()))}
    associate_inp = Associate(input(),input(),input())
    project = Project(associates, skill_requirements)
    validation, count = project.validate_resource(associate_inp)
    if validation:
        print("Associate added")
        print(count)
    else:
        print("Associate not added")
        print(count)



        


        