from sense_hat import SenseHat
sense = SenseHat()

# Define Colors
red = (255, 0, 0)
green = (0, 255, 0)

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    message = "T:" + str(t) + "P:" + str(p) + " H:" + str(h)

    sense.show_message(message, scroll_speed=1)
