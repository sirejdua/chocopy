MAX_INT:int = 4294967295
MIN_INT:int = -4294967296

# disclaimer
# nothing here is tested 
# yet.
class Map:
    #interface for map implementations
    def put(self: "Map", key: "Object", val: "Object") -> object:
        pass

    def get(self: "Map", key: "Object") -> "Object":
        return None

class HashMap(Map):
    # This is a hashmap
    # the implementation is below
    n:int = 8
    size:int = 0
    buckets:["LinkedList"] = []

    def __init__(self: "HashMap") -> object:
        i:int = 0
        while (i < n):
            self.buckets.append(LinkedList())
            i = i + 1

    def put(self: "HashMap", key: "Object", val: "Object") -> object:
        h:int = 0
        bucket_num:int = 0
        if (size + 1 == n): #or a different condition 
            self.realloc(n*2)
            #double num buckets & reallocate items
        h = key.__hash__()
        bucket_num = (h % n + n) % n
        self.buckets[bucket_num].push([key, val])
        size += 1

    def realloc(self: "HashMap", new_size:int) -> object:
        # note
        #   without a GC, this is kind of wasteful.
        #   maybe the allocation should be in place
        i:int = 0
        new_buckets:["LinkedList"] = None
        h:int = 0
        bucket_num:int = 0
        pair:["Object"] = None
        chain:["LinkedList"] = None

        while (i < new_size):
            new_buckets.append(LinkedList())
            i = i + 1
        for chain in self.buckets:
            for pair in chain:
                h = pair[0].__hash__()
                bucket_num = (h % new_size + new_size) % new_size
                new_buckets[bucket_num].push(pair)
        self.buckets = new_buckets
        self.n = new_size

    def get(self: "HashMap", key: "Object") -> "Object":
        chain:"LinkedList" = None
        h:int = 0
        bucket_num:int = 0
        h = key.__hash__()
        bucket_num = (h % self.n + self.n) % self.n
        chain = self.buckets[bucket_num]
        while (not chain.end):
            if h == chain.value[0].__hash__():
                if key.__eq__(chain.value[0]):
                    return chain.value
            chain = chain.pointer
        return None

class LinkedList:
    end:bool = True
    pointer:"LinkedList" = None
    value:"Object" = None

    def __init__(self: "LinkedList") -> object:
        pass

    def push(self: "LinkedList", to_add: "Object") -> object:
        new_pointer:"LinkedList" = None
        new_pointer = pointer
        self.pointer = LinkedList()
        pointer.value = value
        pointer.pointer = new_pointer
        self.value = to_add
        pointer.end = self.end
        self.end = False

    def get(self: "LinkedList") -> "Object":
        return value

    def get_index(self: "LinkedList", index: int) -> "Object":
        if index < 0:
            return None
        elif index == 0:
            return value
        elif end:
            return None
        else:
            return pointer.get_index(index-1)

    def push_index(self: "LinkedList", to_add: "Object", index: int) -> object:
        if index < 0:
            return None
        elif index == 0:
            self.push(to_add)
        elif end:
            return None
        else:
            pointer.push_index(to_add, index-1)

class Object:
    def __eq__(self:"Object", other:"Object") -> bool:
        return False

    def __hash__(self:"Object") -> int:
        return 0
    
class Integer(Object):
    value:int = 0
    
    def set(self:"Integer", val:int) -> None:
        self.value = val

    def get(self:"Integer") -> int:
        return self.value

    def __eq__(self:"Integer", other:"Integer") -> bool:
        return self.value == other.value

    def __hash__(self:"Integer") -> int:
        #what is the hash of an integer in python?
        #rip it's just the integer
        return self.value

class String(Object):
    value:str = ""

    def set(self:"String", val:str) -> None:
        self.value = val

    def get(self:"String") -> int:
        return self.value

    def __eq__(self:"String", other:"String") -> bool:
        return self.value == other.value

    def char_to_ascii(self:"String", char:str) -> int:
        if (char == " "):
            return 0
        elif (char == "!"):
            return 1
        elif (char == "\""):
            return 2
        elif (char == "#"):
            return 3
        elif (char == "$"):
            return 4
        elif (char == "%"):
            return 5
        elif (char == "&"):
            return 6
        elif (char == "'"):
            return 7
        elif (char == "("):
            return 8
        elif (char == ")"):
            return 9
        elif (char == "*"):
            return 10
        elif (char == "+"):
            return 11
        elif (char == ","):
            return 12
        elif (char == "-"):
            return 13
        elif (char == "."):
            return 14
        elif (char == "/"):
            return 15
        elif (char == "0"):
            return 16
        elif (char == "1"):
            return 17
        elif (char == "2"):
            return 18
        elif (char == "3"):
            return 19
        elif (char == "4"):
            return 20
        elif (char == "5"):
            return 21
        elif (char == "6"):
            return 22
        elif (char == "7"):
            return 23
        elif (char == "8"):
            return 24
        elif (char == "9"):
            return 25
        elif (char == ":"):
            return 26
        elif (char == ";"):
            return 27
        elif (char == "<"):
            return 28
        elif (char == "="):
            return 29
        elif (char == ">"):
            return 30
        elif (char == "?"):
            return 31
        elif (char == "@"):
            return 32
        elif (char == "A"):
            return 33
        elif (char == "B"):
            return 34
        elif (char == "C"):
            return 35
        elif (char == "D"):
            return 36
        elif (char == "E"):
            return 37
        elif (char == "F"):
            return 38
        elif (char == "G"):
            return 39
        elif (char == "H"):
            return 40
        elif (char == "I"):
            return 41
        elif (char == "J"):
            return 42
        elif (char == "K"):
            return 43
        elif (char == "L"):
            return 44
        elif (char == "M"):
            return 45
        elif (char == "N"):
            return 46
        elif (char == "O"):
            return 47
        elif (char == "P"):
            return 48
        elif (char == "Q"):
            return 49
        elif (char == "R"):
            return 50
        elif (char == "S"):
            return 51
        elif (char == "T"):
            return 52
        elif (char == "U"):
            return 53
        elif (char == "V"):
            return 54
        elif (char == "W"):
            return 55
        elif (char == "X"):
            return 56
        elif (char == "Y"):
            return 57
        elif (char == "Z"):
            return 58
        elif (char == "["):
            return 59
        elif (char == "\\"):
            return 60
        elif (char == "]"):
            return 61
        elif (char == "^"):
            return 62
        elif (char == "_"):
            return 63
        elif (char == "`"):
            return 64
        elif (char == "a"):
            return 65
        elif (char == "b"):
            return 66
        elif (char == "c"):
            return 67
        elif (char == "d"):
            return 68
        elif (char == "e"):
            return 69
        elif (char == "f"):
            return 70
        elif (char == "g"):
            return 71
        elif (char == "h"):
            return 72
        elif (char == "i"):
            return 73
        elif (char == "j"):
            return 74
        elif (char == "k"):
            return 75
        elif (char == "l"):
            return 76
        elif (char == "m"):
            return 77
        elif (char == "n"):
            return 78
        elif (char == "o"):
            return 79
        elif (char == "p"):
            return 80
        elif (char == "q"):
            return 81
        elif (char == "r"):
            return 82
        elif (char == "s"):
            return 83
        elif (char == "t"):
            return 84
        elif (char == "u"):
            return 85
        elif (char == "v"):
            return 86
        elif (char == "w"):
            return 87
        elif (char == "x"):
            return 88
        elif (char == "y"):
            return 89
        elif (char == "z"):
            return 90
        elif (char == "{"):
            return 91
        elif (char == "|"):
            return 92
        elif (char == "}"):
            return 93
        elif (char == "~"):
            return 94
        elif (char == "\n"):
            return 95
        else:
            return 96

    def __hash__(self:"String") -> int:
        i:int = 0
        n:int = 0
        hval:int = 0
        n = len(self.value)
        while (i < n):

            hval = hval * 128
            hval = hval % (MAX_INT/256)

            hval += self.char_to_ascii(self.value[i])

            i = i + 1
        
        return hval

class Boolean(Object):
    value:bool = False
    def set(self:"Boolean", val:bool) -> None:
        self.value = val

    def get(self:"Boolean") -> bool:
        return self.value

    def __hash__(self:"Boolean") -> int:
        if value:
            return 1
        return 0

    def __eq__(self:"Boolean", other:"Boolean") -> bool:
        return self.value == other.value

