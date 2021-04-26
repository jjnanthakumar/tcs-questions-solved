class Container:
    def __init__(self, id, length, breadth, height, pricepersqrft):
        self.id=id
        self.length=length
        self.breadth=breadth
        self.height=height
        self.pricepersqrft=pricepersqrft
    def findVolume(self):
        return self.length*self.breadth*self.height
class PackagingCompany:
    def __init__(self, containers):
        self.containers=containers
    def findContainerCost(self, id):
        container=list(filter(lambda x: x.id==id, self.containers))
        if not container:
            return "No container found"
        return container[0].findVolume()*container[0].pricepersqrft
    def findLargestContainer(self):
        return max(self.containers, key=lambda x:x.findVolume())
n=int(input())
container_objects=[]
for _ in range(n):
    id_,length, breadth, height, price=int(input()),int(input()),int(input()),int(input()),int(input())
    container_objects.append(Container(id_, length, breadth, height, price))
find_id=int(input())
pack = PackagingCompany(container_objects)
print(pack.findContainerCost(find_id))
container=pack.findLargestContainer()
print(container.id, container.findVolume())