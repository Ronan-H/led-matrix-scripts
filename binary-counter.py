
import unicornhathd

import threading
from datetime import datetime

def update_counter():
    threading.Timer(1.0, update_counter).start()

    seconds = (datetime(2020, 6, 1) - datetime.now()).total_seconds()
    print(seconds)

update_counter()