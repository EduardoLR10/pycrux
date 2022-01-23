from error import ErrorInfo
from error import ErrorOp
from error import errDict

global __REPORT__

class Info :

    @staticmethod
    def helpMsg(msg):
        print("[HELP] " + msg)

    @staticmethod
    def printHelpOps():
        Info.helpMsg("Available operations to introduce error: ")

        ops = ""
        for op in errDict:
            Info.helpMsg(str(op) + " " + str(errDict[op]))
    
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
        elif err == ErrorInfo.serialDevice:
            print("[ERROR] Error with serial device!")
        else:
            print("[ERROR] Unreachable state! Program is nuked!")

    @staticmethod
    def infoMsg(msg):
        print("[INFO] " + msg)

    @staticmethod
    def reportMsg(msg):
        if __REPORT__:
            print("[REPORT] " + msg)
        
            


            
    
