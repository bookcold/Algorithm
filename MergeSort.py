class MergeSort:
    def __init__(self,array):
        self.array = array
        self.length= len(array)

    def __print__(self):
        print self.array

    def MergeSorting(self,first,last):
        if first < last:
            middle = (first + last)//2
            self.MergeSorting(first, middle)
            self.MergeSorting(middle+1, last)
            self.Merge(first, last, middle)

    def Merge(self, first, last, middle):
        leftArray = [self.array[i] for i in range(first,middle+1)]
        rightArray = [self.array[i] for i in range(middle+1,last+1)]
        i = 0
        j = 0
        for k in range(first,last):
            if(leftArray[i] <= rightArray[j]):
                self.array[k] = leftArray[i]
                i +=1
            else:
                self.array[k] = rightArray[j]
                j +=1

array = [3,5,1,7,2,6,4,8]
s = MergeSort(array)
s.MergeSorting(0,len(array)-1)
s.__print__()
