# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"

from datetime import datetime, timedelta


class Leave:
    def __init__(self, id_, type_, days, app_date, approval_date, doc_uploaded=""):
        self.id_ = id_
        self.type_ = type_.lower()
        self.days = days
        self.app_date = datetime.strptime(app_date, "%d/%m/%Y")
        self.approval_date = datetime.strptime(approval_date, "%d/%m/%Y")
        self.doc_uploaded = doc_uploaded.lower()


class LeaveManagement:
    def __init__(self, leave_list):
        self.leave_list = leave_list

    def count_leaves(self):
        data = {"Approved": [], "NonApproved": []}
        for leave in self.leave_list:
            end = leave.app_date + timedelta(days=2)
            if leave.approval_date < end:
                data["Approved"].append(leave)
            else:
                data["NonApproved"].append(leave)
        return data if any((bool(ele) for ele in data.values())) else None

    def get_leaves_per_month(self, month):
        return list(filter(lambda x: int(x.app_date.month) == month and ((x.type_ == "sl" and x.days > 2 and x.doc_uploaded == 'yes') or (x.type_ == "ml" and x.doc_uploaded == 'yes')), self.leave_list))


if __name__ == "__main__":
    n = int(input())
    leaveObjects = []
    for _ in range(n):
        leaveObjects.append(Leave(int(input()), input(), float(
            input()), input(), input(), input()))
    month_inp = int(input())
    leaveManager = LeaveManagement(leaveObjects)
    leaves_count = leaveManager.count_leaves()
    if leaves_count is None:
        print("No Data Found.")
    else:
        print('\n'.join([f'{k}:{len(v)}' for k, v in leaves_count.items()]))

    leaves_month = leaveManager.get_leaves_per_month(month_inp)
    if leaves_month is None:
        print("No Data Found")
    else:
        for ele in leaves_month:
            print(ele.id_, ele.type_, ele.days, ele.app_date.strftime("%d/%m/%Y"),
                  ele.approval_date.strftime("%d/%m/%Y"), ele.doc_uploaded)
