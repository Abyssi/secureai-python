import os
from datetime import datetime


class Stat:

    def __init__(self, file_path):
        self.history = []

        if os.path.exists(file_path):
            os.remove(file_path)
        self.f = open(file_path, "w+")

    def append(self, value):
        t = [datetime.now(), value]
        self.history.append(t)
        self.f.write(str(t[0]) + ", " + str(t[1]) + "\n")

    def close(self):
        self.f.close()
