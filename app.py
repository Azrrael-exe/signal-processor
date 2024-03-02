from domain.processor import AggregatorProcessor
from domain.values import InputRead

from datetime import datetime
from time import sleep
from random import random
import json

def main():
    processor = AggregatorProcessor()
    for i in range(10):
        input_read = InputRead(
            value=random() * 100,
            timestamp=datetime.now(),
            source="source"
        )

        with open("output.txt", "a") as file:
            result = processor.process(input_read)
            output = {
                "timestamp": str(input_read.timestamp),
                "value": input_read.value,
                "source": input_read.source,
                "mean": result.mean_value,
                "change_rate": result.change_rate,
            }
            file.write(json.dumps(output) + "\n")
            print(output)
        sleep(1)



if __name__ == "__main__":

    main()