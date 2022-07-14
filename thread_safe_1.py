from threading import Thread, Lock


class WordCounter:
    def __init__(self):
        self.lock = Lock()
        self.words = {}

    def process_text(self, text):
        words_list = text.split(" ")
        for word in words_list:
            self._counter(word)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.words.get(word, 0)
        self.lock.release()
        return count

    def _counter(self, word):
        self.lock.acquire()
        self.words[word] = self.words.get(word, 0) + 1
        self.lock.release()

