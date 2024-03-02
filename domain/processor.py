from domain.values import InputRead, AggregtedRead

class AggregatorProcessor:
    def __init__(self):
        self.__repository = {}
    
    def __get_historical_values(self, source: str) -> list[InputRead]:
        if source not in self.__repository:
            self.__repository[source] = []
        return self.__repository[source]

    def process(self, input_read: InputRead) -> AggregtedRead:
        historical_values = self.__get_historical_values(
            source=input_read.source
        )
        if len(historical_values) == 0:
            self.__repository[input_read.source].append(input_read)
            return AggregtedRead(
                mean_value=input_read.value,
                change_rate=0,
                source=input_read.source
            )
        else:
            previous_value = historical_values[-1]
            change_rate = (input_read.value - previous_value.value) / (input_read.timestamp - previous_value.timestamp).total_seconds()
            self.__repository[input_read.source].append(input_read)
            return AggregtedRead(
                mean_value=sum([x.value for x in historical_values]) / len(historical_values),
                change_rate=change_rate,
                source=input_read.source
            )



