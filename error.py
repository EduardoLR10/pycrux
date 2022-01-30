import enum

class ErrorOp(enum.Enum):
    burst = 1
    bit = 2
    byte =  3
    removal = 4
    unreachable = 5
    
errDict = {"-b" : ErrorOp.bit,
           "-y" : ErrorOp.byte,
           "-u" : ErrorOp.burst,
           "-r" : ErrorOp.removal}

class ErrorInfo(enum.Enum):
    operation = 1
    dataFile = 2
    noDataFile = 3
    emptyFile = 4
    wrongDataFile = 5
    noErrorArg = 6
    serialDevice = 7
    notEnoughBytes = 8
    unreachable = 9

class ErrorSerial(enum.Enum):
    noPortProvided = 1
    closedPort = 2
