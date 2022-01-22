import enum

class ErrorOp(enum.Enum):
    gust = 1
    bit = 2
    byte =  3
    removal = 4
    unreachable = 5
    
errDict = {"-b" : ErrorOp.bit,
           "-y" : ErrorOp.byte,
           "-g" : ErrorOp.gust,
           "-r" : ErrorOp.removal}

class ErrorInfo(enum.Enum):
    operation = 1
    dataFile = 2
    noDataFile = 3
    emptyFile = 4
    wrongDataFile = 5
    noErrorArg = 6
    serialDevice = 7
    unreachable = 8

class ErrorSerial(enum.Enum):
    noPortProvided = 1
    closedPort = 2
