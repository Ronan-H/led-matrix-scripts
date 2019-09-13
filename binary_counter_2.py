
import unicornhathd

import threading
from datetime import datetime
import math

unicornhathd.rotation(0)
unicornhathd.brightness(0.5)
unicornhathd.rotation(270)
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
    # add padding bits to the left
    longest = max(len(q) for q in quantities)
    quantities = [q.rjust(longest, "0") for q in quantities]


    unicornhathd.clear()
    for i in range(len(quantities)):
        quantity = quantities[i]
        for j in range(len(quantity)):
            if quantity[j] == "1":
                # x is inverted because pixel indexing is bugged
                unicornhathd.set_pixel(15 - j, i, 200, 0, 0)
            else:
                unicornhathd.set_pixel(15 - j, i, 20, 0, 0)

    unicornhathd.show()

update_counter()