class Sorting(list):
    def bubble_sort(self):
        needs_sorting = True
        while needs_sorting:
            needs_sorting = False
            p1 = 0
            p2 = 1
            while p2 < len(self):
                if self[p2] < self[p1]: 
                    needs_sorting = True
                    self[p1], self[p2] = self[p2], self[p1]
                p1 += 1
                p2 += 1
        return self
    

    def quick_sort(self):
        pass
    def merge_sort(self):
        pass


arr = Sorting([4,1,2,6,3,0,0,1,1,1,2,3])
arr.bubble_sort()
print("After sorting: ", arr)      
