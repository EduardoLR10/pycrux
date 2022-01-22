from error import errDict
from error import ErrorInfo
from error import ErrorOp
from info import Info
from os import stat

def parseDataFile(filepath):
    try:
        handle = open(filepath)
    except FileNotFoundError:
        Info.errorMsg("Data file not found!", ErrorInfo.noDataFile)
        return []

    if stat(filepath).st_size == 0:
        Info.errorMsg("Data file is empty!", ErrorInfo.emptyFile)
        return []
    
    dataBytes = []
    parsedData = (handle.read()).split(sep = " ")

    if parsedData == []:
        Info.errorMsg("Data file is not formatted correctly!", ErrorInfo.wrongDataFile)
        return []
    
    for byte in parsedData:
        dataBytes.append(int(byte, base = 16))
    
    return dataBytes

def parseErrorType(sErr):
    if sErr in errDict:
        return errDict[sErr]
    else:
        Info.errorMsg("Invalid error operation type!", ErrorInfo.operation)
        return ErrorOp.unreachable

    

        
