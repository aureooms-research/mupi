
from random import randint
from information import fix

def erase ( M , m , n ) :

	for row in M :

		i = 0

		x = randint( 0 , 1 )

		while i < n and row[i] > 0 :
			row[i] = x
			i += 1

		while i < n and row[i] == 0 : i += 1

		x = randint( -1 , 0 )

		while i < n and row[i] < 0 :
			row[i] = x
			i += 1

	fix( M , m , n )

	return M


def main ( lines ) :

	from matrix import mat , show , parse

	M , m , n  = parse( lines )

	erase( M , m , n )
	print( show( M ) , end = "" )


if __name__ == "__main__" :

	import fileinput

	main( fileinput.input( ) )
