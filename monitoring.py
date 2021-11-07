import psutil

class Monitoring:
    def __init__(self):
        self.ram = psutil.virtual_memory().percent
        self.memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

