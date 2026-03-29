from datetime import datetime

class Host:
    def __init__(self, address:str, name: str, port = 80):
        self.address = address
        self.name = name
        self.is_alive = False
        self.port = port
        self.last_checked = None

    def update_status(self, alive: bool):
        self.is_alive = alive
        self.last_checked = datetime.now()

    def __str__(self):
        state = "UP" if self.is_alive else "DOWN"
        return f'{self.name}:{self.address}, {self.port} - {state}'
