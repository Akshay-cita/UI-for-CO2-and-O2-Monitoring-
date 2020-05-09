from ctypes import *
import struct
import time
import serial
import binascii

ser = serial.Serial( port='/dev/ttyS0',baudrate = 19200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
#counter=0
checkdata='0001'
co2_32=0xFFFF
global a,b
c=0
def convert(s):
	i = int(s, 16)                   # convert from hex to a Python int
	cp = pointer(c_int(i))           # make this into a c integer
	fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
	return fp.contents.value         # dereference the pointer, get the float
def reset():
	packet = bytearray()
	packet.append(0x61)
	packet.append(0x06)
	packet.append(0x00)
	packet.append(0x34)
	packet.append(0x00)
	packet.append(0x01)
	packet.append(0x00)
	packet.append(0x64)
	ser.write(packet)
	s = ser.read(7)
	hex_string = binascii.hexlify(s).decode('utf-8')
	print("reset  ",hex_string)


def readystatus():
	packet = bytearray()
	packet.append(0x61)
	packet.append(0x03)
	packet.append(0x00)
	packet.append(0x27)
	packet.append(0x00)
	packet.append(0x01)
	packet.append(0x3D)
	packet.append(0xA1)

	ser.write(packet)
	s = ser.read(7)
	hex_string = binascii.hexlify(s).decode('utf-8')
#	print(hex_string)
	device_ready_bit=hex_string[6:10]
#	print((device_ready_bit))
#if device_ready_bit[2]==checkdata[0] and device_ready_bit[3]==checkdata[1]:
	if device_ready_bit==checkdata:
		#print("device is ready")
		return 1
	else :
		#print("error")
		return 0

def measurement():
	if(readystatus()==1):
		measurement_packet = bytearray()
		measurement_packet.append(0x61)
		measurement_packet.append(0x03)
		measurement_packet.append(0x00)
		measurement_packet.append(0x28)
		measurement_packet.append(0x00)
		measurement_packet.append(0x06)
		measurement_packet.append(0x4C)
		measurement_packet.append(0x60)

		ser.write(measurement_packet)
		s = ser.read(17)
		measurement_string = binascii.hexlify(s).decode('utf-8')
		print(measurement_string)
		co2=measurement_string[6:14]
	#print("co2 value",co2)
	#s=repr(co2.encode('utf-8'))
	#i = int(co2, 16)
		co2_hex=binascii.unhexlify(co2)
#	print(co2_hex)
#	print(hex(co2_hex[0]))
	#temp=measurement_string[14:22]
	#hum=measurement_string[22:30]
	#print("humidity",hum)
	#print("temperature",temp)
	#temp_hex=binascii.unhexlify(temp)
	#hum_hex=binascii.unhexlify(hum)

	#hum_32=hum_hex[0]<<24 | hum_hex[1]<<16 | hum_hex[2]<<8 |hum_hex[3]

	#temp_32=temp_hex[0]<<24 | temp_hex[1]<<16 | temp_hex[2]<<8 |temp_hex[3]

		co2_32=co2_hex[0]<<24 | co2_hex[1]<<16 | co2_hex[2]<<8 |co2_hex[3]

		co2_conv=hex(co2_32)
	#temp_conv=hex(temp_32)
	#hum_conv=hex(hum_32)

	#print(convert(co2_conv))
		if float(convert(co2_conv))>0:
		#print("co2 value = %.2f" %((convert(con1))/10000))
			c=convert(co2_conv)/10000
		#t=convert(temp_conv)
		#h=convert(hum_conv)

			a=float("{0:.1f}".format(c))
		#b=float("{0:.1f}".format(t))
		#c=float("{0:.1f}".format(h))
			return a
	else:
		print("waiting")
		#return g
def Humidity():
	if(readystatus()==1):
		measurement_packet = bytearray()
		measurement_packet.append(0x61)
		measurement_packet.append(0x03)
		measurement_packet.append(0x00)
		measurement_packet.append(0x28)
		measurement_packet.append(0x00)
		measurement_packet.append(0x06)
		measurement_packet.append(0x4C)
		measurement_packet.append(0x60)

		ser.write(measurement_packet)
		s = ser.read(17)
		measurement_string = binascii.hexlify(s).decode('utf-8')
		hum=measurement_string[22:30]
		hum_hex=binascii.unhexlify(hum)
		hum_32=hum_hex[0]<<24 | hum_hex[1]<<16 | hum_hex[2]<<8 |hum_hex[3]
		hum_conv=hex(hum_32)
		if float(convert(hum_conv))>0:
			h=convert(hum_conv)
			d=float("{0:.1f}".format(h))
			print("humidity    ",d)
			return d
		else:
			print("waiting Humidity")

def Temperature():
	if(readystatus()==1):
		measurement_packet = bytearray()
		measurement_packet.append(0x61)
		measurement_packet.append(0x03)
		measurement_packet.append(0x00)
		measurement_packet.append(0x28)
		measurement_packet.append(0x00)
		measurement_packet.append(0x06)
		measurement_packet.append(0x4C)
		measurement_packet.append(0x60)

		ser.write(measurement_packet)
		s = ser.read(17)
		measurement_string = binascii.hexlify(s).decode('utf-8')
		temp=measurement_string[14:22]
		temp_hex=binascii.unhexlify(temp)
		temp_32=temp_hex[0]<<24 | temp_hex[1]<<16 | temp_hex[2]<<8 |temp_hex[3]
		temp_conv=hex(temp_32)
		if float(convert(temp_conv))>0:
			h=convert(temp_conv)
			c=float("{0:.1f}".format(h))
			print("Temperature    ",c)
			return c

	else:
		print("waiting Temperature")
#while 1:
	#measurement()
	#time.sleep(3)
	#Humidity()
	#time.sleep(3)
	#Temperature()
	#time.sleep(3)

