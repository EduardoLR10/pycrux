import enum

class Target(enum.Enum):
    header = 1
    payload = 2
    allBytes = 3
    unreachable = 4
    
targetDict = {"-h" : Target.header,
              "-p" : Target.payload,
              "-a" : Target.allBytes}
