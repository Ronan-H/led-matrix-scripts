
import unicornhathd

import threading
from datetime import datetime
import math

unicornhathd.rotation(0)
unicornhathd.brightness(0.6)
u_width, u_height = unicornhathd.get_shape()

def update_counter():
    threading.Timer(1.0, update_counter).start()

    seconds = math.ceil((datetime(2020, 6, 1) - datetime.now()).total_seconds())
    bin_seconds = str(bin(seconds))[2:]

    unicornhathd.clear()
    for i in range(len(bin_seconds)):
        x, y = i % u_width, i / u_width
        unicornhathd.set_pixel(x, y, 255, 255, 255)


update_counter()