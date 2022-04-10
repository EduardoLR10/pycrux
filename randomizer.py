from error import ErrorOp
from error import ErrorInfo
from target import Target
from info import Info
import random

class Randomizer:
    def __init__(self, errType, target, dataBytes):
        self.errType = errType
        self.dataBytes = dataBytes
        self.target = target

    def __pickTarget(self, function):

        if self.target == Target.allBytes:
            Info.infoMsg("Chosen target: All Bytes")
            self.dataBytes = function(self.dataBytes)
        elif self.target == Target.header:
            Info.infoMsg("Chosen target: Header")
            newHeader = function(self.dataBytes[0:2])
            self.dataBytes[0] = newHeader[0]
            self.dataBytes[1] = newHeader[1]
        elif self.target == Target.payload:
            Info.infoMsg("Chosen target: Payload")
            newPayload = function(self.dataBytes[2:(len(self.dataBytes))])
            for i in range(0, len(newPayload)):
                self.dataBytes[i + 2] = newPayload[i]
        else:
            Info.errorMsg("Unreachable in pickTarget()", ErrorInfo.unreachable)

    def applyError(self):
        if self.errType == ErrorOp.burst:
            self.__pickTarget(self.__execBurst)
        elif self.errType == ErrorOp.bit:
            self.__pickTarget(self.__execBit)
        elif self.errType == ErrorOp.byte:
            self.__pickTarget(self.__execByte)
        elif self.errType == ErrorOp.removal:
            self.__pickTarget(self.__execRemoval)
        elif self.errType == ErrorOp.noError:
            self.__noError()
        else:
            Info.errorMsg("Unreachable in applyError()", ErrorInfo.unreachable)

    def __noError(self):
        Info.infoMsg("No error will be applied to data ...")
        return
            
    def __execBurst(self, byteArray):
        Info.infoMsg("Randomly applying burst error within data ...")

        Info.reportMsg("Chosen error operation: Burst")
        
        size = len(byteArray)

        if size < 2:
            Info.errorMsg("It is necessary 2 or more bytes to use Burst error!", ErrorInfo.notEnoughBytes)
            return
        
        howmany = 0
        
        while howmany < 1:
            howmany = random.randint(0, size - 1)

        first = random.randint(0, size - howmany)
        
        Info.reportMsg(str(howmany) + " bytes will be changed, starting from byte " + str(first))

        for i in range(first, first + howmany):
            previous = byteArray[i]
            byteArray[i] = int.from_bytes(random.randbytes(1), byteorder = 'big')
            printIndex = (i + 2) if self.target == Target.payload else i
            Info.reportMsg("Byte " + str(printIndex) + " changed from value " + str(previous) + " to value " + str(byteArray[i]))

        return byteArray
        
    def __execBit(self, byteArray):
        Info.infoMsg("Randomly applying bit error within data ...")

        Info.reportMsg("Chosen error operation: Bit")

        size = len(byteArray)
        chosenByteIndex = random.randint(0, size - 1)

        Info.reportMsg("Byte " + str(chosenByteIndex) + " with value " + str(byteArray[chosenByteIndex]) + " was chosen to apply bit error")

        bitstring = format(byteArray[chosenByteIndex], 'b').zfill(8)

        Info.reportMsg("Original bit string of byte " + str(chosenByteIndex) + ": " + bitstring)

        chosenBitIndex = random.randint(0, 7)

        Info.reportMsg("Bit " + str(chosenBitIndex) + " with value " + str(bitstring[chosenBitIndex]) + " was flipped")

        newBitstring = ""

        for i in range(0, 8):
            if i == chosenBitIndex:
                if bitstring[i] == '1':
                    newBitstring += "0"
                else:
                    newBitstring += "1"
            else:
                newBitstring += bitstring[i]

        printIndex = (chosenByteIndex + 2) if self.target == Target.payload else chosenByteIndex
        Info.reportMsg("New bit string of byte " + str(printIndex) + ": " + newBitstring)

        byteArray[chosenByteIndex] = int(newBitstring, 2)

        return byteArray

    def __execByte(self, byteArray):
        Info.infoMsg("Randomly applying byte error within data ...")       

        Info.reportMsg("Chosen error operation: Byte")

        size = len(byteArray)
        chosenByteIndex = random.randint(0, size - 1)

        previous = byteArray[chosenByteIndex]
        byteArray[chosenByteIndex] = int.from_bytes(random.randbytes(1), byteorder = 'big')

        printIndex = (chosenByteIndex + 2) if self.target == Target.payload else chosenByteIndex
        Info.reportMsg("Byte " + str(printIndex) + " changed from value " + str(previous) + " to value " + str(byteArray[chosenByteIndex]))

        return byteArray
        
    def __execRemoval(self, byteArra):
        Info.infoMsg("Randomly applying removal of byte error within data ...")

        Info.reportMsg("Chosen error operation: Removal")
        
        size = len(byteArray)
        chosenByteIndex = random.randint(0, size - 1)

        newByteArray = []

        for i in range(0, size):
            if i != chosenByteIndex:
                newByteArray.append(byteArray[i])
        
        Info.reportMsg("Byte " + str(chosenByteIndex) + " with value " + str(byteArray[chosenByteIndex]) + " was removed")
        byteArray = newByteArray

        return byteArray
        
        
        
