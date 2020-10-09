import key,codecs,math

msg = [char for char in open('flag.txt','r').read()]

a,b,c = key.Key()

try:
	d11 = 4*a*c
	d1 = b**2 - d11
	d = math.sqrt(d1)
	r11 = 2*a
	r1 = (-b + d)/r11
	r2 = (-b - d)/r11

except:
	print("No possible solution")

for char in enumerate(msg):

	if(char[0] % 2 == 0):
		msg[char[0]] = chr(ord(msg[char[0]]) ^ int(r1))
	else:
		msg[char[0]] = chr(ord(msg[char[0]]) ^ int(r2))

print(codecs.encode(''.join(msg).encode(),'hex').decode())
