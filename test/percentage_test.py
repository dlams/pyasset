import unittest

from percentage.captions import PercentageValueCaption, PercentageTinyTimeSpanCaption
from percentage.bar import BarPercentage
from time import sleep


class PercentageTestModel(unittest.TestCase):
    def test_bar_runs(self):
        # make percentage bar from 0 to 100.
        bar = BarPercentage(0, 100)
        # caption - print value like [1/100].
        bar.add_caption(PercentageValueCaption)
        # caption - print time like 0.42 s.
        bar.add_caption(PercentageTinyTimeSpanCaption)

        for _ in range(100):
            # sleep(0.05)
            # percentage += 1
            bar.add_value(1)
            # print percentage bar
            bar.update()

        # clear bar state ( value, captions data )
        # but, not "\n" print
        # bar.clear()

    def test_percentage_50(self):
        bar = BarPercentage(0, 100)
        for _ in range(50):
            bar.add_value(1)
        bar.update()


    def test_percentage_75(self):
        bar = BarPercentage(0, 4)
        bar.add_value(3)
        bar.update()

if __name__ == '__main__':
    unittest.main()
