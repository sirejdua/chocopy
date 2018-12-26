class HashMap:
    # this is a hashmap

class Object:
    def __equals__(self:"Object", other:"Object") -> bool:
        return False

    def __hash__(self:"Object", other:"Object") -> int:
        return 0
    
class Integer(Object):
    value:int = 0
    
    def set(self:"Integer", val:int) -> None:
        self.value = val

    def get(self:"Integer") -> int:
        return self.value

    def __equals__(self:"Integer", other:"Integer") -> bool:
        return self.value == other.value

    def __hash__(self:"Integer") -> int:
        #what is the hash of an integer in python?
        #rip it's just the integer
        return self.value

class String(Object):

class Boolean(Object):

