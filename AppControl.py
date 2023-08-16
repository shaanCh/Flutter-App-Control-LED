#!usr/bin/env/python3

from flask import Flask, render_template, session, request, redirect, url_for
from threading import Thread
import board
import neopixel
import time
from rpi_ws281x import *
import argparse

app = Flask(__name__)

#LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
strip.begin()
def ledcolor(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
def wheel(pos):
	#Generate rainbow colors across 0-255 positions
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
def rainbowCycle(strip, wait_ms=20, iterations=5):
    #Draw rainbow that uniformly distributes itself across all pixel
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
def script():
	global scriptON
	while True:
		ledcolor(strip, Color(255, 0, 0))
		if scriptON:
			ledcolor(strip, Color(0,0,0))
			break
		ledcolor(strip, Color(0,255,0))
		if scriptON:
			ledcolor(strip, Color(0,0,0))
			break
		ledcolor(strip, Color(0, 0, 255))
		if scriptON:
			ledcolor(strip, Color(0,0,0))
			break
		rainbow(strip)
		if scriptON:
			ledcolor(strip, Color(0,0,0))
			break
		rainbowCycle(strip)
		if scriptON:
			ledcolor(strip, Color(0,0,0))
			break

@app.route("/flutter/test", methods=["GET"])
def test():
	return {'message': 'Hello from Flask!'}

@app.route("/Red", methods=["GET"])
def red():
	ledcolor(strip, Color(255,0,0))
	return {'message': 'SUCCESS'}

@app.route("/Clear", methods=["GET"])
def clear():
	ledcolor(strip, Color(0,0,0))
	return {'message': 'SUCCESS'}

@app.route("/Orange", methods=["GET"])
def Orange():
	ledcolor(strip, Color(255,100,0))
	return {'message': 'SUCCESS'}
@app.route("/Yellow", methods=["GET"])
def Yellow():
	ledcolor(strip, Color(255,255,0))
	return {'message': 'SUCCESS'}
@app.route("/Green", methods=["GET"])
def Green():
	ledcolor(strip, Color(0,255,0))
	return {'message': 'SUCCESS'}
@app.route("/Blue", methods=["GET"])
def Blue():
	ledcolor(strip, Color(0,0,255))
	return {'message': 'SUCCESS'}
@app.route("/Violet", methods=["GET"])
def Violet():
	ledcolor(strip, Color(255,0,255))
	return {"message": "SUCCESS"}
@app.route("/Start", methods=["GET"])
def Start():
	global scriptON
	scriptON = False
	thread = Thread(target=script)
	thread.start()
	return {"message": "start"}

@app.route("/Stop", methods=["GET"])
def Stop():
	global scriptON
	scriptON = True
	return {"message": "Stop"}

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    
