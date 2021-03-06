import sys
from error import ErrorInfo
from error import ErrorOp
from utils import parseDataFile
from utils import parseErrorType
from utils import parseTargetType
from randomizer import Randomizer
from serializer import Serializer
from info import Info
from target import Target
import info


def main():

    if len(sys.argv) < 5:
        info.__REPORT__ = False
    else:
        if sys.argv[4] == "--report":
             info.__REPORT__ = True
        else:
             info.__REPORT__ = False

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
    
    target = parseTargetType(sys.argv[3])

    if target == Target.unreachable:
        return

    Info.infoMsg("Creating randomizer ...")
    random = Randomizer(err, target, data)

    Info.infoMsg("Original data: " + str(random.dataBytes))
    random.applyError()
    Info.infoMsg("New data: " + str(random.dataBytes))

    Info.infoMsg("Creating serializer ...")
    serial = Serializer(19200, 'COM6')

    Info.infoMsg("Sending data using serial port ...")
    serial.sendData(random.dataBytes)
    Info.infoMsg("Data was sent successfully!")

    Info.infoMsg("Receiving data using serial port ...")
    data = serial.receiveData()
    Info.infoMsg("Received: " + str(data))
    # data = serial.receiveData()
    # Info.infoMsg("Received: " + str(data))
    # data = serial.receiveData()
    # Info.infoMsg("Received: " + str(data))
    # data = serial.receiveData()
    # Info.infoMsg("Received: " + str(data))
    Info.infoMsg("Data was received successfully!")

if __name__ == "__main__":
    main()
