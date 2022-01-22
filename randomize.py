from error import ErrorOp
from error import ErrorInfo
from info import Info
import random

class Randomize:
    def __init__(self, errType, dataBytes):
        self.errType = errType
        self.dataBytes = dataBytes

    def applyError(self):
        if self.errType == ErrorOp.gust:
            self.__execGust()
        elif self.errType == ErrorOp.bit:
            self.__execBit()
        elif self.errType == ErrorOp.byte:
            self.__execByte()
        elif self.errType == ErrorOp.removal:
            self.__execRemoval()
        else:
            Info.errorMsg("Unreachable in applyError()", ErrorInfo.unreachable)

    def __execGust(self):
        Info.infoMsg("Applying gust error inside data randomly ...")
        
        Info.reportMsg("Chosen error operation: Gust")
        
        size = len(self.dataBytes)
        howmany = 0
        
        while howmany == 0:
            howmany = random.randint(0, size - 1)

        first = random.randint(0, size - howmany)
        
        Info.reportMsg(str(howmany) + " byte(s) will be changed, starting from byte " + str(first))

        for i in range(first, first + howmany):
            previous = self.dataBytes[i]
            self.dataBytes[i] = int.from_bytes(random.randbytes(1), byteorder = 'big')
            Info.reportMsg("Byte " + str(i) + " changed from value " + str(previous) + " to value " + str(self.dataBytes[i]))
        
    def __execBit(self):
        Info.infoMsg("Applying bit error inside data randomly ...")
        print("TODO: Make random algorithm to do bit error")

    def __execByte(self):
        Info.infoMsg("Applying byte error inside data randomly ...")

        Info.reportMsg("Chosen error operation: Byte")

        size = len(self.dataBytes)
        chosenByte = random.randint(0, size - 1)

        previous = self.dataBytes[chosenByte]
        self.dataBytes[chosenByte] = int.from_bytes(random.randbytes(1), byteorder = 'big')

        Info.reportMsg("Byte " + str(chosenByte) + " changed from value " + str(previous) + " to value " + str(self.dataBytes[chosenByte]))
        
    def __execRemoval(self):
        Info.infoMsg("Applying removal of byte error inside data randomly ...")

        Info.reportMsg("Chosen error operation: Removal")
        
        size = len(self.dataBytes)
        chosenByte = random.randint(0, size - 1)

        newByteArray = []

        for i in range(0, size):
            if i != chosenByte:
                newByteArray.append(self.dataBytes[i])
        
        Info.reportMsg("Byte " + str(chosenByte) + " with value " + str(self.dataBytes[chosenByte]) + " was removed")
        self.dataBytes = newByteArray
        
        
        
