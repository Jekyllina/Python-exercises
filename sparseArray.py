class SparseArray():
    def __init__(self, *args):
        self.sparse_array = []
        for arg in args:
            self.sparse_array.append(arg) 

    def __len__(self):
        return len(self.sparse_array)

    def __getitem__(self, index):
        if index > (len(self) - 1):
            return 0
        else:
            return self.sparse_array[index]

    def __setitem__(self, index, value):
        if value != 0:            
            self.sparse_array[index] = value 
        
    def __delitem__(self, index):
        del self.sparse_array[index]   

    def append(self, value):
        if value != 0:
            self.sparse_array.append(value) 
       

if __name__ == '__main__':
    sa = SparseArray(1, 4, 5, 0, 0, 2, 3, 0, 1)
    
    print(f"lenght of the array: {len(sa)}")
    print(f"element at index 1: {sa[1]}")
    
    val = sa[10]
    print(val)

    sa[2] = 0
    sa[3] = 9    
    print(sa.sparse_array)

    del(sa[6])
    print(f"array with element 6 deleted: {sa.sparse_array}")

    sa.append(18)
    print(f"array after append: {sa.sparse_array}")