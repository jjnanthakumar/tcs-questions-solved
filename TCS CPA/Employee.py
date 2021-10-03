# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Employee:
    def __init__(self,e_id,e_name,e_dept,salary,role):
        self.employeeId = e_id
        self.employeeName = e_name
        self.department = e_dept 
        self.salary = salary
        self.role = role
    
    def calculateIncentive(self,roleIncentivePercentage):
        percent=roleIncentivePercentage.get(self.role)
        if percent is not None:
            return self.salary*(percent/100)
        else:
            return percent
    @staticmethod
    def calculateEmployeeSalaryByRole(role,empObjects,roleIncentives):
        filteredObjects=list(filter(lambda x:x.role==role,empObjects))
        if filteredObjects:
            for emp in filteredObjects:
                emp.salary+=emp.calculateIncentive(roleIncentives)
            return filteredObjects

# Driver Program
numberRoles=int(input())
roleIncentives={input().lower(): int(input()) for _ in range(numberRoles)}
n=int(input())
EmpObjects=[Employee(int(input()),input(),input(),int(input()),input().lower()) for _ in range(n)]
role=input().lower()
incentive0=EmpObjects[0].calculateIncentive(roleIncentives)
if incentive0 is None:
    print("Employee Not Found")
else:
    print(incentive0)

res=Employee.calculateEmployeeSalaryByRole(role,EmpObjects,roleIncentives)
if res is None:
    print("Employee Not Found.")
else:
    for r in res:
        print(r.employeeId,r.employeeName,r.salary)


