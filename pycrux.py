import sys
from utils import parseDataFile
from utils import parseErrorType
from randomize import Randomize
from info import Info

def main():

    Info.infoMsg("Loading and parsing data file ...")
    data = parseDataFile(sys.argv[1])

    Info.infoMsg("Checking error operation ...")
    err = parseErrorType(sys.argv[2])

    Info.infoMsg("Setting up randomize ...")
    random = Randomize(err, data)

    random.applyError()
    

if __name__ == "__main__":
    main()
