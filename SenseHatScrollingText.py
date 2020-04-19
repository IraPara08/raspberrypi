# Scrolling Text
from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
sense.clear()

while True:
    sense.show_message("Astro PPi is awesome!" , text_colour=yellow, back_colour=blue, scroll_speed=1.0)
    
