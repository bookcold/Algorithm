import sys

class KnapSack:
    def __init__(self,Items,BagWeight):
        self.Items = Items
        self.BagWeight = BagWeight
        self.Pack = {}
        self.Bag = []
    def __GetItemWeight__(self,item):
        return item[0]
    def __GetItemValue__(self,item):
        return item[1]
    def __GetItemName__(self,item):
        return item[2]

    def __PrintPack__(self):
        for i in range(len(self.Items)):
            for j in range(self.BagWeight+1):
                #sys.stdout.write(self.Pack[i,j])
                #sys.stdout.write("   ")
                print self.Pack[i,j],
            sys.stdout.write("\n")

    def ZeroOneKnapSack(self):
        for i in range(len(self.Items)):
            for limit in range (self.BagWeight+1):
                if i == 0:
                    self.Pack[i,limit] = 0
                elif self.__GetItemWeight__(self.Items[i]) > limit:
                    self.Pack[i,limit] = self.Pack[i-1,limit]
                else:
                    self.Pack[i,limit] = max(self.Pack[i-1,limit],
                                             self.Pack[i-1,limit-self.__GetItemWeight__(self.Items[i-1])]+
                                             self.__GetItemValue__(self.Items[i]))
        return self.Pack[len(self.Items)-1,self.BagWeight]
    
    def GetPackageItems(self):
        num = len(self.Items)-1
        limit = self.BagWeight
        while num > 0:
            if self.Pack[num,limit] == self.Pack[num-1,limit]:
                num -= 1
            else:
                num -= 1
                self.Bag.append(self.__GetItemName__(self.Items[num]))
                limit -= self.__GetItemWeight__(self.Items[num])
        self.Bag.reverse()
        return self.Bag



Items = [(3,3,'A'),
         (4,1,'B'),
         (8,3,'C'),
         (10,4,'D'),
         (15,3,'E'),
         (20,6,'F')]
knapsack = KnapSack(Items,32)
print knapsack.UnboundedKnapSack()
print knapsack.GetPackageItems()
