from error import ErrorOp
from error import ErrorInfo
from info import Info

class Randomize:
    def __init__(self, errType, dataBytes):
        self.errType = errType
        self.dataBytes = dataBytes

    def applyError(self):
        if self.errType == ErrorOp.gust:
            self.__execGust()
        elif self.errType == ErrorOp.bit:
            self.__execBit()
        elif self_errType == ErrorOp.byte:
            self.__execByte()
        elif self.errType == ErrorOp.removal:
            self.__execRemoval()
        else:
            Info.errorMsg("Unreachable in applyError()", ErrorInfo.unreachable)

    def __execGust(self):
        Info.infoMsg("Applying gust error across data randomly ...")
        print("TODO: Make random algorithm to do gust error")

    def __execBit(self):
        Info.infoMsg("Applying bit error inside data randomly ...")
        print("TODO: Make random algorithm to do bit error")

    def __execByte(self):
        Info.infoMsg("Applying byte error inside data randomly ...")
        print("TODO: Make random algorithm to do byte error")

    def __execRemoval(self):
        Info.infoMsg("Applying removal of byte error inside data randomly ...")
        print("TODO: Make random algorithm to do removal of byte error")
            
        
        
