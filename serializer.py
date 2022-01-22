from info import Info
from error import ErrorInfo
import serial

class Serializer:
    def __init__(self, baudrate, port):
        Info.infoMsg("Creating serializer ...")
        
        self.ser = serial.Serial()
        
        Info.reportMsg("Setting baudrate to: " + str(baudrate))
        
        self.ser.baudrate = baudrate
        
        Info.reportMsg("Setting port to: " + str(port))
        
        self.ser.port = port
    
    def sendData(self, data):
        if not self.ser.is_open:
            Info.reportMsg("The port is closed. Opening ...")
            
            self.ser.open()
            
        Info.reportMsg("Sending data ...")

        for byte in data:
            Info.reportMsg("Sending byte " + str(byte) + " ...")
            written = self.ser.write(bytes([byte]))
            if written == 1:
                Info.reportMsg("Byte " + str(byte) + " sent successfully!")
            else:
                Info.errorMsg("Check your connection with device!", ErrorInfo.serialError)
        
        Info.reportMsg("Closing port ...")
        
        self.ser.close()

    def receiveData(self, data):
        if not self.ser.is_open:
            Info.reportMsg("The port is closed. Opening...")
             
            self.ser.open()

        Info.reportMsg("Flushing ...")
        
        self.ser.flush()
        
        Info.reportMsg("Reading data ...")
        
        data = self.ser.read_all()
        
        Info.reportMsg("Closing port ...")
        
        self.ser.close()
        
        return data

        
        
