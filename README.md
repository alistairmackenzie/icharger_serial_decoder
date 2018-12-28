
# icharger_serial_decoder
iCharger serial decoder

Decodes serial output from Junsi iCharger and various clones.

![image of iCharger 106B+](https://images.amain.com/images/large/jun/jun-106b+.jpg?width=475)

## Hardware
Confirmed working on the following chargers.

* iCharger 106B+
* [Turnigy Reaktor 250W 10A 1-6S Balance Charger](https://hobbyking.com/en_us/turnigy-reaktor-250w-10a-1-6s-balance-charger.html)

## Usage

```
$ ./decode_data.py --help         
usage: decode_data.py [-h] -p PORT [-f FILE]

Decodes serial output from iCharger and clones

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial port the charger is on (Usually /dev/ttyUSB0)
  -f FILE, --file FILE  Log output to file as CSV

```

## example output

```
06:59:20 28-12-2018, Mode: Charging, Vin: 15.89 V, Vout: 16.84 V, Iout: 0.51 A, C1: 4.21 V, C2: 4.20 V, C3: 4.20 V, C4: 4.20 V, C5: 0.00 V, C6: 0.00 V, Int temp: 27.40 °C, Ext temp: 0.10 °C, Cout: 4.000000 mAh
06:59:22 28-12-2018, Mode: Charging, Vin: 15.89 V, Vout: 16.84 V, Iout: 0.48 A, C1: 4.21 V, C2: 4.20 V, C3: 4.20 V, C4: 4.20 V, C5: 0.00 V, C6: 0.00 V, Int temp: 27.40 °C, Ext temp: 0.10 °C, Cout: 5.000000 mAh
06:59:24 28-12-2018, Mode: Charging, Vin: 15.89 V, Vout: 16.85 V, Iout: 0.48 A, C1: 4.21 V, C2: 4.20 V, C3: 4.20 V, C4: 4.20 V, C5: 0.00 V, C6: 0.00 V, Int temp: 27.40 °C, Ext temp: 0.10 °C, Cout: 5.000000 mAh
06:59:26 28-12-2018, Mode: Charging, Vin: 15.90 V, Vout: 16.84 V, Iout: 0.48 A, C1: 4.21 V, C2: 4.20 V, C3: 4.20 V, C4: 4.20 V, C5: 0.00 V, C6: 0.00 V, Int temp: 27.40 °C, Ext temp: 0.10 °C, Cout: 5.000000 mAh
06:59:28 28-12-2018, Mode: Charging, Vin: 15.91 V, Vout: 16.80 V, Iout: 0.44 A, C1: 4.21 V, C2: 4.20 V, C3: 4.20 V, C4: 4.20 V, C5: 0.00 V, C6: 0.00 V, Int temp: 27.40 °C, Ext temp: 0.10 °C, Cout: 5.000000 mAh
06:59:30 28-12-2018, Mode: Charging, Vin: 15.89 V, Vout: 16.84 V, Iout: 0.44 A, C1: 4.21 V, C2: 4.20 V, C3: 4.20 V, C4: 4.20 V, C5: 0.00 V, C6: 0.00 V, Int temp: 27.40 °C, Ext temp: 0.10 °C, Cout: 6.000000 mAh
06:59:32 28-12-2018, Mode: Charging, Vin: 15.90 V, Vout: 16.84 V, Iout: 0.44 A, C1: 4.20 V, C2: 4.20 V, C3: 4.20 V, C4: 4.20 V, C5: 0.00 V, C6: 0.00 V, Int temp: 27.40 °C, Ext temp: 0.10 °C, Cout: 6.000000 mAh
```