
from dataclasses import dataclass

@dataclass(frozen = True)
class ImmutableClass:
    value1: str 
    value2: int 

    def newValue(self , newVal):
        self.value2 = newVal

obj = ImmutableClass("abc" , 34) 
print(obj.value1) #output : immutable

# obj.value2 = 30
# print(obj) #output : dataclasses.FrozenInstanceError: cannot assign to field 'value2'

print(obj.newValue(45))