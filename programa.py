
import sys, os, serial, threading
from datetime import datetime

now = datetime.now()

def monitor():

    ser = serial.Serial(COMPORT, BAUDRATE, timeout=0)
    
    printFile("SEP = ," + CARRIAGE_RETURN)

    while (1):
        line = readData(ser)
        print(line)
        printFile(line + CARRIAGE_RETURN)

    print("Stop Monitoring")



def readData(ser):
    buffer = ""
    while True:
        oneByte = ser.read(1)
        if oneByte == b"\r":    #method should returns bytes
            return buffer.split(":")[1].strip()
        else:
            buffer += oneByte.decode("ascii")

def printFile(line):
    text_file = open(FOLDER + FILENAME, "a")
    text_file.write(line)
    text_file.close()

print("Start Serial Monitor")

COMPORT = "COM3"
BAUDRATE = 115200
EXTENSION = "csv"
CARRIAGE_RETURN = "\r"
FILENAME = str(now.strftime("%Y_%m_%d_%H_%M") + "_log_" + "bogohack" + "." + EXTENSION)
FOLDER = "Resultados/"
print(FILENAME)


monitor()
			