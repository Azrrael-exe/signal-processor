from domain.processor import AggregatorProcessor
from domain.values import InputRead, AggregtedRead

def process_read(processor: AggregatorProcessor, input_read: InputRead) -> AggregtedRead:
    return processor.process(input_read)