class Sorter:
    def __init__(self, data):
        self.data = data

    def sort(self):
        raise NotImplementedError("Sort method not implemented.")

class BubbleSort(Sorter):
    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data

class InsertionSort(Sorter):
    def sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i-1
            while j >=0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
        return self.data

# Using the sorting classes
data_to_sort = [64, 34, 25, 12, 22, 11, 90]

bubble_sorter = BubbleSort(data_to_sort[:])  # Passing a copy of the data
print("Bubble Sorted:", bubble_sorter.sort())

insertion_sorter = InsertionSort(data_to_sort[:])  # Passing another copy
print("Insertion Sorted:", insertion_sorter.sort())
