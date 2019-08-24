
import unicornhathd

import threading
from datetime import datetime
import math

unicornhathd.rotation(0)
unicornhathd.brightness(0.6)
u_width, u_height = unicornhathd.get_shape()

def seconds_to_times(seconds):
    time_seconds = [86400, 3600, 60, 1]
    quantities = []

    for i in range(len(time_seconds)):
        time = time_seconds[i]
        quantity = seconds // time
        seconds -= quantity * time
        quantities.append(quantity)

    return quantities

def update_counter():
    threading.Timer(1.0, update_counter).start()

    seconds = math.ceil((datetime(2020, 6, 1) - datetime.now()).total_seconds())
    quantities = [str(bin(sec))[2:] for sec in seconds_to_times(seconds)]

    unicornhathd.clear()
    for i in range(len(quantities)):
        quantity = quantities[i]
        for j in range(len(quantity)):
            if quantity[j] == "1":
                # x is inverted because pixel indexing is bugged
                unicornhathd.set_pixel(15 - j, i, 255, 255, 255)
            else:
                unicornhathd.set_pixel(15 - j, i, 50, 50, 50)

    unicornhathd.show()

update_counter()