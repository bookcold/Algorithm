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
        tmpArray = []
        i = first
        j = middle+1
        while i<=middle and j<=last:
            if(self.array[i] <= self.array[j]):
                tmpArray.append(self.array[i])
                i += 1
            else:
                tmpArray.append(self.array[j])
                j += 1
        while i<=middle:
            tmpArray.append(self.array[i])
            i += 1
        while j<=last:
            tmpArray.append(self.array[j])
            j += 1
        for k in range(0, last - first + 1):
            self.array[first + k] = tmpArray[k]

array = [3,5,1,9,7,2,6,4,8,10]
s = MergeSort(array)
s.MergeSorting(0,len(array)-1)
s.__print__()
