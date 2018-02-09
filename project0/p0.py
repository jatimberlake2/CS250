import sys

def print_ppm(height):
	print('P3')
	print(2*height, height)
	print('255')
	#print("255 0 0")
	#print("0 255 0")
	#print("0 0 255")
	#print("0 255 0")
	#print("255 0 0")
	red = height
	green = height
	blue = 0
	for i in range(height):
		for j in range(red):
			if (j == i):
				print("80 80 80")
			else:
				print("0 0 0")
		for k in range(green):
			if (k == height - 2*red or k == 2*blue):
				print("80 80 80")
			else:
				print("204 0 0")

		for l in range(blue):
			if (l == height - 2*red):
				print("80 80 80")
			else:
				print("255 245 0")
		red -= 1
		blue += 1
	
def main():
	height = int(sys.argv[1])
	if (height > 1280):
		print("stahhhhp (needs to be less than 1280)!", file=sys.stderr)
	else:
		print_ppm(height)
main()
