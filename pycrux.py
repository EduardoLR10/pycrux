import sys
from error import ErrorInfo
from error import ErrorOp
from utils import parseDataFile
from utils import parseErrorType
from randomizer import Randomize
from info import Info
from serializer import Serializer

def main():
    
    if len(sys.argv) < 2:
        Info.errorMsg("No data file!", ErrorInfo.dataFile)
        return
        
    Info.infoMsg("Loading and parsing data file ...")
    data = parseDataFile(sys.argv[1])

    if data == []:
        return

    Info.infoMsg("Checking error operation ...")

    if len(sys.argv) < 3:
        Info.errorMsg("No error introduction argument!", ErrorInfo.noErrorArg)
        return
    
    err = parseErrorType(sys.argv[2])

    if err == ErrorOp.unreachable:
        return

    Info.infoMsg("Setting up randomizer ...")
    random = Randomize(err, data)

    Info.infoMsg("Original data: " + str(random.dataBytes))
    random.applyError()
    Info.infoMsg("New data: " + str(random.dataBytes))

    serial = Serializer(19200, 'COM6')

    serial.sendData(random.dataBytes)

if __name__ == "__main__":
    main()
