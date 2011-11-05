class QuickSort:
    def __init__(self,array):
        self.array = array
        self.length = len(self.array)

    def __print__(self):
        print self.array

    def __Swap__(self,i,j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp
    
    def QuickSorting(self,first,last):
        if first < last:
            pos = self.Partition(first,last)
            self.QuickSorting(first,pos-1)
            self.QuickSorting(pos+1,last)
    
    def Partition(self,first,last):
        pivot = self.array[last]
        i = first -1
        for j in range(first,last):
            if self.array[j] <= pivot:
                i+=1
                self.__Swap__(i,j)
        self.__Swap__(i+1, last)
        return i + 1

array = [2,8,7,1,3,5,6,4]
q = QuickSort(array)
q.QuickSorting(0,len(array)-1)
q.__print__()
