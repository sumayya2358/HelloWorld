def generate_string(string, frequency):
    position = 0
    current_count = 0
    while position < len(string):
        if current_count >= frequency:
            if position == len(string) - 1:
                break
            current_count = 0
            position += 1
        result = string[position]
        yield result
        current_count += 1


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.position = 0
        self.current_count = 0
        return self

    def __next__(self):
        if self.current_count >= self.frequency:
            self.current_count = 0
            self.position += 1
        if self.position >= len(self.string):
            raise StopIteration
        self.current_count += 1
        return self.string[self.position]


