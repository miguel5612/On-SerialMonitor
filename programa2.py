
import sys, os, serial, threading
from datetime import datetime

now = datetime.now()
headers = 'MQ-2, MQ-3, MQ-4, MQ-5, MQ-6, MQ-7, MQ-8, MQ-9'
NombreImpresion = "mq"

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
    try:
        text_file = open(r'C:/Users/Rocio/Desktop/On-SerialMonitor/' + FOLDER + FILENAME, mode = 'w', encoding='utf-8')
        text_file.write(line)
        text_file.flush()
        text_file.close()
    except IOError:
        print("I/O error(" + IOError)
print("Start Serial Monitor")

COMPORT = "COM3"
BAUDRATE = 115200
EXTENSION = "txt"
CARRIAGE_RETURN = "\r"
FILENAME = str(now.strftime("%Y%m%d%H%M") + "log" + str(NombreImpresion) + "." + EXTENSION)
FOLDER = "Resultados/"
print(FILENAME)


monitor()