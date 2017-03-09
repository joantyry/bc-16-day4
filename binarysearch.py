
class BinarySearch(list):
   
    def __init__(self, length, step):
       
        super(BinarySearch, self).__init__()

       
        for element in range(1, length+1):
            self.append(element * step)

       
        self.length = len(self)

    def search(self, to_search):
        
        first = 0
        last = len(self) - 1
        value_index = 0
        found = False

       
        counter = 0

        
        if to_search == self[first]:
            value_index = first
            found = True
        elif to_search == self[last]:
            value_index = last
            found = True

        
        if to_search not in self:
            found = True
            value_index = -1

        
        while first <= last and not found:
            mid = (first + last) // 2
            if self[mid] == to_search:
                found = True
                value_index = mid
            else:
                counter += 1  
                if to_search < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': counter, 'index': value_index}

print BinarySearch(20,19)