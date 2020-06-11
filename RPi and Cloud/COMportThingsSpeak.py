import serial
import requests
import io
# import pyserial

from pprint import pprint
from serial import SerialException


url = "https://api.thingspeak.com/update?api_key="
apiKey = "K7M9UXMSLQPD5CDO"

# print("Hello there...")

while True:
    geturl_f1 = url + apiKey + "&"
    # print(geturl_f1)
    try:
        if True:
            print("Internet is connected!")
        with serial.Serial('COM3', 115200) as ser:
            line = ser.readline()
            # print(line.decode())
            line = line.decode()
            line = line[0:len(line) - 1]
            print(line)
            geturl_f1 += line
            print(geturl_f1)
            try:
                r = requests.get(geturl_f1)
                print(r.status_code)
                pprint(r.json())
                if (r.status_code == 200):
                    ser.write(b'ACK')
            except requests.ConnectionError:
                print("Internet is NOT connected")
                break

    except SerialException:
        print("Port is already open")
        break
