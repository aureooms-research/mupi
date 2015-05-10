
def gcd ( a , b ) :

	"""

		>>> gcd( 2 * 3 * 5 * 7 * 13 , 2 * 2 * 2 * 5 * 7 * 11 * 13 * 17 )
		910

	"""

	while True :

		if a == 0 : return b

		b %= a

		if b == 0 : return a

		a %= b

def prod ( iterable ) :

	"""

		>>> prod( [ 4 , 7 , 2 , -9 ] )
		-504

	"""

	p = 1

	for item in iterable : p *= item

	return p

