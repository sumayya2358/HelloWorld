class Range:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.iterator = None

    def __iter__(self):
        self.iterator = RangeIterator(self.start, self.stop, self.step)
        return self

    def __next__(self):
        return self.iterator.__next__()


class RangeIterator:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = self.start

    def __next__(self):

        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration
        self.current += self.step
        return self.current - self.step






