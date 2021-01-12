#https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import time
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
adc0 = AnalogIn(mcp, MCP.P0)

#print('Raw ADC Value: ', adc0.value) #adafruit example code
#while True:
#	print(adc0.voltage)#print('ADC Voltage: ' + str(adc0.voltage) + 'V')
#	time.sleep(0.5)
#count = 0
print("Logging!")
while True:
	f = open("data.csv", "a") #open file in append mode to keep all data in same place. File continually opened and closed to protect contents
	for i in range(100): #save file every 100 readings
		f.write(str(adc0.voltage) + ',' + str(time.time()))
		f.write('\n')
		time.sleep(1/100) #wait 10 miliiseconds (or so - timing isn't great on rpi)
		#count = count + 1
	f.close()
