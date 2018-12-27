MAX_INT:int = 4294967295
MIN_INT:int = -4294967296

class HashMap:
    # this is a hashmap
    # this will be a hashmap*
    n:int = 8

class Object:
    def __eq__(self:"Object", other:"Object") -> bool:
        return False

    def __hash__(self:"Object", other:"Object") -> int:
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

