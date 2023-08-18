import time

from percentage import Percentage, PercentageCaption


class PercentageTinyTimeSpanCaption(PercentageCaption):
    def __init__(self):
        self.start = time.time()

    def register(self, percentage: Percentage) -> PercentageCaption:
        self.start = time.time()
        return self

    def process(self, round_n: int = 2) -> str:
        return f"{round(time.time() - self.start, round_n)} s"


class PercentageValueCaption(PercentageCaption):
    def __init__(self):
        self.percentage = None

    def register(self, percentage: Percentage) -> PercentageCaption:
        self.percentage = percentage
        return self

    def process(self) -> str:
        maximum = self.percentage.get_maximum()
        value = self.percentage.get_value()
        return f"[{value}/{maximum}]"
