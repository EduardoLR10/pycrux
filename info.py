from error import ErrorInfo
from error import errDict


class Info :

    @staticmethod
    def printHelpOps():
        ops = ""
        for op in errDict:
            ops += str(op) + " " + str(errDict[op]) + " | "

        print("[ERROR] Available operations to introduce error: " + ops)

    
    @staticmethod
    def errorMsg(msg, err):

        print("[ERROR] " + msg)
        
        if err == ErrorInfo.operation:
            Info.printHelpOps()
        elif err == ErrorInfo.noDataFile:
            print("[ERROR] Provide a data file in the command line!")
        elif err == ErrorInfo.emptyFile:
            print("[ERROR] The data file cannot be empty!")
        elif err == ErrorInfo.wrongDataFile:
            print("[ERROR] Format example: 0x00 0x01 0x02 0x03 ...")
        elif err == ErrorInfo.noErrorArg:
            print("[ERROR] Provide an error argument in the command line!")
        else:
            print("[ERROR] Unreachable state! Program is nuked!")

    @staticmethod
    def infoMsg(msg):
        print("[INFO] " + msg)

    
            


            
    
