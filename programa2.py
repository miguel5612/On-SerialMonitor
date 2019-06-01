
import sys, os, serial, threading
from datetime import datetime

now = datetime.now()
headers = 'MQ-2, MQ-3, MQ-4, MQ-5, MQ-6, MQ-7, MQ-8, MQ-9'
NombreImpresion = "Calibracion sensores MQ"

def monitor():

    ser = serial.Serial(COMPORT, BAUDRATE, timeout=100)
    printFile("SEP = ," + CARRIAGE_RETURN)
    print(headers)
    printFile(headers)

    while (1):
        line = readData(ser) + ',' + str(datetime.now()) + ',' + str(NombreImpresion)
        print(line)
        printFile(line + CARRIAGE_RETURN)

    print("Stop Monitoring")



def readData(ser):
    return ser.readline().decode("utf-8").strip()
def printFile(line):
    text_file = open(FOLDER + FILENAME, "a")
    text_file.write(line)
    text_file.close()

print("Start Serial Monitor")

COMPORT = "COM7"
BAUDRATE = 115200
EXTENSION = "csv"
CARRIAGE_RETURN = "\r"
FILENAME = str(now.strftime("%Y_%m_%d_%H_%M") + "_log_" + str(NombreImpresion) + "." + EXTENSION)
FOLDER = "Resultados/"
print(FILENAME)


monitor()