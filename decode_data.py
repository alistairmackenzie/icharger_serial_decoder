#!/usr/bin/env python3

import serial
import datetime
import argparse

ap = argparse.ArgumentParser(description="Decodes serial output from iCharger and clones")
ap.add_argument("-p", "--port", required=True, help="Serial port the charger is on (Usually /dev/ttyUSB0)")
ap.add_argument("-f", "--file", help="Log output to file as CSV")

args = ap.parse_args()
time_format = "%H:%M:%S %d-%m-%Y"

states = {
    '1': 'Charging',
    '2': 'Discharging',
    '3': 'Monitor',
    '4': 'Waiting',
    '5': 'Motor test',
    '6': 'Done',
    '7': 'Error',
    '8': 'LiXX trickle',
    '9': 'NiXX trickle',
    '10': 'Foam cut',
    '11': 'Info',
    '12': 'External discharging'
}

def log_csv(line):
    if not args.file:
        return
    with open(args.file, 'a') as output:
        output.write(line + "\n")

if args.file:
    csv_header = "Time,Mode,Vin,Vout,Iout,C1,C2,C3,C4,C5,C6,Int temp,Ext temp,Cout"
    log_csv(csv_header)
    

## Start


ser = serial.Serial(args.port, 9600, bytesize=serial.SEVENBITS)
time_prev = datetime.datetime.now()

b = ser.read()
while b is not None:
    line = ser.readline().strip().decode().split(';')
    time_now = datetime.datetime.now()

    mode = states[line[1]] # Map the state to something readable from dict
    Vin = float(line[3]) * 0.001 # Voltage is in mv
    Vout = float(line[4]) * 0.001 # Voltage is in mv
    Iout = float(line[5])  * 0.01 # Current is in odd format
    C1 = float(line[6]) * 0.001 # Voltage is in mv
    C2 = float(line[7]) * 0.001 # Voltage is in mv
    C3 = float(line[8]) * 0.001 # Voltage is in mv
    C4 = float(line[9]) * 0.001 # Voltage is in mv
    C5 = float(line[10]) * 0.001 # Voltage is in mv
    C6 = float(line[11]) * 0.001 # Voltage is in mv
    intTemp = float(line[12]) * 0.1 # Temp is in odd format
    extTemp = float(line[13]) * 0.1 # Temp is in odd format
    Cout = float(line[14]) # Cout is mAh


    output = "%s, Mode: %s, Vin: %0.2f V, Vout: %0.2f V, Iout: %0.2f A, C1: %0.2f V, C2: %0.2f V, C3: %0.2f V, C4: %0.2f V, C5: %0.2f V, C6: %0.2f V, Int temp: %0.2f °C, Ext temp: %0.2f °C, Cout: %f mAh" %\
     (time_now.strftime(time_format), mode, Vin, Vout, Iout, C1, C2, C3, C4, C5, C6, intTemp, extTemp, Cout)
    print(output)

    if args.file:
        csv_output = "%s,%s,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%f" % \
         (time_now.strftime(time_format), mode, Vin, Vout, Iout, C1, C2, C3, C4, C5, C6, intTemp, extTemp, Cout)
        log_csv(csv_output)