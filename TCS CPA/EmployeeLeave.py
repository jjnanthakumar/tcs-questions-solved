# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


from calendar import monthrange
from datetime import datetime, date

# LEAVE_TYPES = {'EL': 'Earned Leave', 'CL': 'Casual Leave', 'SL': 'Sick Leave'}


class Leave:
    def __init__(self, leaveId, leaveType, noOfDays, dateOfApplication):
        self.leaveId = leaveId
        self.leaveType = leaveType
        self.noOfDays = noOfDays
        self.dateOfApplication = dateOfApplication


class Employee:
    def __init__(self, leaveList, leaveBalance):
        self.leaveList = leaveList
        self.leaveBalance = leaveBalance

    def getUpdatedLeaveBalance(self):
        for obj in self.leaveList:
            if obj.noOfDays <= self.leaveBalance[obj.leaveType]:
                self.leaveBalance[obj.leaveType] = self.leaveBalance[obj.leaveType] - obj.noOfDays
            else:
                print(
                    f"Insufficient balance for {obj.leaveType} applied on {obj.dateOfApplication.strftime('%d-%m-%y')}")
        return {i: j for i, j in sorted(self.leaveBalance.items(), key=lambda kv: (kv[1], kv[0]))}

    def getLeaveCount(self, startMonth, endMonth):
        _, numdaysend = monthrange(2021, endMonth)
        firstday = date(2021, startMonth, 1)
        lastday = date(2021, endMonth, numdaysend)
        data = [firstday <= obj.dateOfApplication <= lastday for obj in self.leaveList]
        return sum(data) if all(data) else None


N = int(input())
LeaveObjects = []
for _ in range(N):
    leaveId, leaveType, noOfDays, dateOfApplication = int(
        input()), input(), int(input()), datetime.strptime(input(), '%d-%m-%y').date()
    LeaveObjects.append(Leave(leaveId, leaveType, noOfDays, dateOfApplication))
leaveBalance = {'EL': int(input()), 'CL': int(input()), 'SL': int(input())}
empObj = Employee(LeaveObjects, leaveBalance)
startMonth, endMonth = int(input()), int(input())

data = empObj.getUpdatedLeaveBalance()
for k, v in data.items():
    print(f'{k}:{v}')

leaveCount = empObj.getLeaveCount(startMonth, endMonth)
print('No leave applied between given months' if leaveCount is None else leaveCount)
