import time
import board
import neopixel
from mcstatus import MinecraftServer

colors = {
    'mxc42': (70, 221, 255),
    'starflash1000200': (245, 117, 66),
    'Wilaphant': (18, 255, 22)
}

# Server config.
server_hostname = "mc.mxc42.com"
# The port for the query server is running on a different port than the world server.
server_port = 4243
# Make a server object with the right connection properties.
server = MinecraftServer(server_hostname, server_port)
# Frequency of server queries (in seconds).
refresh_delay = 5

# Brightness of the LEDs.
bright = 0.5
# Pi pin that the LEDs are connected to.
pixel_pin = board.D18
# Number of LEDs (There are 8 on the PCB, you can turn some off if you want though).
num_pixels = 8
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

# Object defining the LED lights.
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=bright, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def blank_colors():
    pixels.fill((0, 0, 0))
    pixels.show()
    pixels.show()


def set_colors(names: list):
    if not names:
        blank_colors()
        return

    num_online = len(names)
    for i in range(num_pixels):
        pixels[i] = colors[names[i % num_online]]

    pixels.show()
    pixels.show()


def main():
    currentState: list = []
    blank_colors()

    while True:
        try:
            query = server.query()
            print(query.players.names)
            if (set(query.players.names) != set(currentState)):
                currentState = query.players.names
                set_colors(currentState)

        except Exception as e:
            print(e)
        finally:
            time.sleep(refresh_delay)


main()
