class Table:
    def __init__(self, tableNo=None, waiterName=None, status=None):
        self.tableNo=tableNo
        self.waiterName=waiterName
        self.status=status
    def findWaiterWiseTotalNoOfTables(self, table_objects):
        data={}
        for obj in sorted(table_objects, key=lambda x: x.waiterName):
            data[obj.waiterName]=data.get(obj.waiterName,0)+1
        return '\n'.join([f'{k}-{v}'for k,v in data.items()])
    def findWaiterNameByTableNo(self, table_objects, table_no):
        data=list(filter(lambda x: x.tableNo==table_no,table_objects))
        if data:
            return data[0].waiterName

n=int(input())
tableobjects=[Table(int(input()),input(),input()) for i in range(n)]
tab_no=int(input())
table_data=Table()
print(table_data.findWaiterWiseTotalNoOfTables(tableobjects))
name= table_data.findWaiterNameByTableNo(tableobjects,tab_no)
if name is None:
    print("No Table Found")
else:
    print(name)

