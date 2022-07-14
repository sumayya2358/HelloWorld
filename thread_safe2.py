from threading import Thread, Lock


class WordCounter:
    def __init__(self):
        self.lock = Lock()
        self.words = {}

    def process_text(self, text):
        temp_dict = {}
        words_list = text.split(" ")
        for word in words_list:
            if not word in temp_dict:
                temp_dict[word] = 0
            temp_dict[word] += 1
        self._dict_changer(temp_dict)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.words.get(word, 0)
        self.lock.release()
        return count

    def _dict_changer(self, data_dict):
        self.lock.acquire()
        for word in data_dict:
            self.words[word] = self.words.get(word, 0) + data_dict[word]
        self.lock.release()

