
import sys, os, serial, threading
from datetime import datetime

now = datetime.now()
headers = 'Hotbed, Extruder, Motor X, Motor Y, Motor Z1, Motor Z2, Voltaje, Corriente, Potencia electrica (W), Potencia electrica(KW/h), Objeto 3D (Descripcion)'
NombreImpresion = "Clase impresion 3D Vivelab"

def monitor():

    ser = serial.Serial(COMPORT, BAUDRATE, timeout=0)
    
    printFile("SEP = ," + CARRIAGE_RETURN)
    print(headers)
    printFile(headers)

    while (1):
        line = readData(ser) + ',' + str(datetime.now()) + ',' + str(NombreImpresion)
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

COMPORT = "COM5"
BAUDRATE = 115200
EXTENSION = "csv"
CARRIAGE_RETURN = "\r"
FILENAME = str(now.strftime("%Y_%m_%d_%H_%M") + "_log_" + str(NombreImpresion) + "." + EXTENSION)
FOLDER = "Resultados/"
print(FILENAME)


monitor()
			