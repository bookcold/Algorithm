class HeapSort:
    def __init__(self,array):
        self.array    = array
        self.length   = len(array)-1
        self.heapsize = self.length

    def __parent__(self,i):
        return i//2

    def __left__(self,i):
        return 2*i+1

    def __right__(self,i):
        return 2*i+2

    def __print__(self):
        print self.array

    def __swap__(self,i,j):
        tmp           = self.array[i]
        self.array[i] =self.array[j]
        self.array[j] =tmp

    def BuildMaxHeap(self):
        for i in range(self.length//2,-1,-1):
            self.MaxHeapify(i)

    def MaxHeapify(self,i):
        largest = 0
        left    = self.__left__(i)
        right   = self.__right__(i)
        if left <= self.heapsize and self.array[left] > self.array[i]:
            largest = left
        else:
            largest = i
        if right <= self.heapsize and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            self.__swap__(i,largest)
            self.MaxHeapify(largest)

    def HeapSorting(self):
        self.BuildMaxHeap()
        for i in range(self.length,0,-1):
            self.__swap__(0,i)
            self.heapsize -=1
            self.MaxHeapify(0)

array = [3,7,5,1,9,4,8,2,6,0]
s = HeapSort(array)
s.HeapSorting()
s.__print__()
