import enum

class ErrorOp(enum.Enum):
    gust = 1
    bit = 2
    byte =  3
    removal = 4

errDict = {"-b" : ErrorOp.bit,
           "-y" : ErrorOp.byte,
           "-g" : ErrorOp.gust,
           "-r" : ErrorOp.removal}

class ErrorInfo(enum.Enum):
    operation = 1
    dataFile = 2
    emptyFile = 3
    wrongDataFile = 4
    unreachable = 5
