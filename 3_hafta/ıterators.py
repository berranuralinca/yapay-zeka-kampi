### Iterators ###

liste = [1,2,3,4]

for i in liste:  # iterable obje
    print(i)
    
    
    
import time   

liste = [1,2,3,4]

iterator =  iter(liste) # iterable obje gonder

while True:
    try:
        element = next(iterator)
        print(element)
        time.sleep(1)
        
    except StopIteration:
        break

# belli aralikta deger uretme
class mynumbers:  
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop :
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
            
            
list = mynumbers(10, 15)       

myiter = iter(list)

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break
