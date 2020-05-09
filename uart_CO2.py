from ctypes import *
import struct
import time
import serial
import binascii
import test_1
ser = serial.Serial( port='/dev/ttyS0',baudrate = 19200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
#counter=0
checkdata='0001'
co2_32=0xFFFF
def convert(s):
	i = int(s, 16)                   # convert from hex to a Python int
	cp = pointer(c_int(i))           # make this into a c integer
	fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
	return fp.contents.value         # dereference the pointer, get the float

def readystatus(): #to get data ready status from the sensor 
	packet = bytearray() 
	packet.append(0x61)
	packet.append(0x03)
	packet.append(0x00)
	packet.append(0x27)
	packet.append(0x00)
	packet.append(0x01)
	packet.append(0x3D)
	packet.append(0xA1)

	ser.write(packet) #writing bytearray
	s = ser.read(7) #reading response
	hex_string = binascii.hexlify(s).decode('utf-8')#converting to unicode string('utf-8')
	device_ready_bit=hex_string[6:10]
	if device_ready_bit==checkdata: #checking data ready bit 00 or 001
		return 1 #true
	else :
		return 0 #false

def measurement(): #reading measurement from sensor
	measurement_packet = bytearray()
	measurement_packet.append(0x61)
	measurement_packet.append(0x03)
	measurement_packet.append(0x00)
	measurement_packet.append(0x28)
	measurement_packet.append(0x00)
	measurement_packet.append(0x06)
	measurement_packet.append(0x4C)
	measurement_packet.append(0x60)

	ser.write(measurement_packet)#writing
	s = ser.read(17)#reading response
	measurement_string = binascii.hexlify(s).decode('utf-8')#convert to utf-8 string
	co2=measurement_string[6:14]
	co2_hex=binascii.unhexlify(co2)#string to decimal
	co2_32=co2_hex[0]<<24 | co2_hex[1]<<16 | co2_hex[2]<<8 |co2_hex[3]
	co2_conv=hex(co2_32)#decimal to hex
	if float(convert(co2_conv))>0:
		s=convert(co2_conv)/10000 #ppm to percentage conversion
		g=float("{0:.2f}".format(s)) 
		#print(g)
		return g 
def co2_value():
	while 1:
		if(readystatus()==1): #checking data ready status
			time.sleep(2)
			m= measurement() #start measurement reading
			return m
		else:
			print("waiting")
			#reset()
			return 'a'

