from domain.processor import AggregatorProcessor
from domain.values import InputRead

from datetime import datetime
from time import sleep
from random import random

def main():
    processor = AggregatorProcessor()
    for i in range(10):
        input_read = InputRead(
            value=random() * 100,
            timestamp=datetime.now(),
            source="source"
        )
        print(input_read)
        print(processor.process(input_read))
        sleep(1)



if __name__ == "__main__":

    main()