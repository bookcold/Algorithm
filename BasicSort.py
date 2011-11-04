class BasicSort:
    def __init__(self,array):
        self.array = array
        self.length = len(self.array)

    def BubbleSort(self):
        for i in range (self.length -1):
            for j in range ( self.length - i -1):
                if self.array[j] > self.array[j+1]:
                    tmp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = tmp
        return self.array
    
    def SelectionSort(self):
        for i in range (self.length -1):
            minimun = i
            for j in range (i+1 , self.length):
                if self.array[minimun] > self.array[j]:
                    minimun = j
            tmp = self.array[i]
            self.array[i] = self.array[minimun]
            self.array[minimun] = tmp
        return self.array            
    
    def InsertionSort(self):
        for i in range (2,self.length):
            key = self.array[i]
            j = i -1
            while j >= 0 and self.array[j] > key:
                self.array[j+1] = self.array[j]
                j = j - 1
            self.array[j+1] = key
        return self.array
    
    def CountingSort(self):
        countlist = [0 for i in range(max(self.array)+1)]
        a = self.array[:]
        for j in self.array:
            countlist[j] += 1
        for i in range(1,len(countlist)):
            countlist[i]= countlist[i]+countlist[i-1]
        countlist = [i-1 for i in countlist]
        for j in range(self.length-1,-1,-1):
            a[countlist[self.array[j]]]= self.array[j]
            countlist[self.array[j]] = countlist[self.array[j]] - 1
        return a

array = [10,51,2,18,0,10,4,31,29,13,57,9,64,29]
sort = BasicSort(array)
#a = sort.BubbleSort()
#a = sort.SelectionSort()
#a  = sort.InsertionSort()
a = sort.CountingSort()
print a

