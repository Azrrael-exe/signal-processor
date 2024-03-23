from domain.processor import AggregatorProcessor
from domain.values import InputRead

from datetime import datetime
from time import sleep
from random import random
import json

from serial import Serial

port = Serial("/dev/ttyACM0", 115200)

class Comm:
    def __init__(self, port: Serial, header: int):
        self._port = port
        self._header = header
        self._input_buffer = []

    def has_message(self) -> bool:
        if self._port.in_waiting > 0:
            input_header = ord(self._port.read())
            if self._header == input_header:
                length = ord(self._port.read())
                data = [byte for byte in self._port.read(size=length)]
                checksum = ord(self._port.read())
                calculated_checksum = ~sum(data) & 0xFF
                if checksum != calculated_checksum:
                    print("Checksum error")
                    return False
                self._input_buffer += data
                return True
        return False
    
    def get_queue(self) -> list[int]:
        return self._input_buffer

comm = Comm(port, 0x7e)

def main():
    for i in range(20):
        if comm.has_message():
            print(f"Message: {comm.get_queue()}")
        sleep(1)



if __name__ == "__main__":

    main()