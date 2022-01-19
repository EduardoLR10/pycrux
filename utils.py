from error import errDict
from error import ErrorInfo
from info import Info

def parseDataFile(filepath):
    handle = open(filepath)
    dataBytes = []
    for byte in ((handle.read()).split(sep = " ")):
        dataBytes.append(int(byte, base = 16))
    
    return dataBytes

def parseErrorType(sErr):
    if sErr in errDict:
        return errDict[sErr]
    else:
        Info.errorMsg("Invalid error operation type!", ErrorInfo.operation)

    

        
