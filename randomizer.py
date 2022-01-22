from error import ErrorOp
from error import ErrorInfo
from info import Info
import random

class Randomizer:
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
        Info.infoMsg("Randomly applying gust error within data ...")

        Info.reportMsg("Chosen error operation: Gust")
        
        size = len(self.dataBytes)
        howmany = 0
        
        while howmany < 2:
            howmany = random.randint(0, size - 1)

        first = random.randint(0, size - howmany)
        
        Info.reportMsg(str(howmany) + " bytes will be changed, starting from byte " + str(first))

        for i in range(first, first + howmany):
            previous = self.dataBytes[i]
            self.dataBytes[i] = int.from_bytes(random.randbytes(1), byteorder = 'big')
            Info.reportMsg("Byte " + str(i) + " changed from value " + str(previous) + " to value " + str(self.dataBytes[i]))
        
    def __execBit(self):
        Info.infoMsg("Randomly applying bit error within data ...")

        Info.reportMsg("Chosen error operation: Bit")

        size = len(self.dataBytes)
        chosenByteIndex = random.randint(0, size - 1)

        Info.reportMsg("Byte " + str(chosenByteIndex) + " with value " + str(self.dataBytes[chosenByteIndex]) + " was chosen to apply bit error")

        bitstring = format(self.dataBytes[chosenByteIndex], 'b').zfill(8)

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

        Info.reportMsg("New bit string of byte " + str(chosenByteIndex) + ": " + newBitstring)

        self.dataBytes[chosenByteIndex] = int(newBitstring, 2)

    def __execByte(self):
        Info.infoMsg("Randomly applying byte error within data ...")       

        Info.reportMsg("Chosen error operation: Byte")

        size = len(self.dataBytes)
        chosenByteIndex = random.randint(0, size - 1)

        previous = self.dataBytes[chosenByteIndex]
        self.dataBytes[chosenByteIndex] = int.from_bytes(random.randbytes(1), byteorder = 'big')

        Info.reportMsg("Byte " + str(chosenByte) + " changed from value " + str(previous) + " to value " + str(self.dataBytes[chosenByteIndex]))
        
    def __execRemoval(self):
        Info.infoMsg("Randomly applying removal of byte error within data ...")

        Info.reportMsg("Chosen error operation: Removal")
        
        size = len(self.dataBytes)
        chosenByteIndex = random.randint(0, size - 1)

        newByteArray = []

        for i in range(0, size):
            if i != chosenByteIndex:
                newByteArray.append(self.dataBytes[i])
        
        Info.reportMsg("Byte " + str(chosenByte) + " with value " + str(self.dataBytes[chosenByteIndex]) + " was removed")
        self.dataBytes = newByteArray
        
        
        
