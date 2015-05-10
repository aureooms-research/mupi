from matrix import mat , show , subscripts , parse
from information import comparator , Oracle
from math import log

def grid ( m , n ) :

	e = mat( m + 1 , n + 1 , None )

	e[0][0] = 1

	return e

def dynamic ( compare , e , i , j ) :

	"""

		>>> compare = comparator( [ [ 0 , 0 ] , [ 0 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		6

		>>> compare = comparator( [ [ 1 , 0 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		3

		>>> compare = comparator( [ [ -1 , -1 ] , [ -1 , -1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		1

		>>> compare = comparator( [ [ -1 , -1 ] , [ 0 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		3

		>>> compare = comparator( [ [ 1 , 1 ] , [ 1 , 1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		1

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		4

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		2

		>>> compare = comparator( [ [ -1 , -1 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> dynamic( compare , e , 2 , 2 )
		2

	"""

	if e[i][j] is None :

		if   i == 0 : e[i][j] = dynamic( compare , e , i , j - 1 )
		elif j == 0 : e[i][j] = dynamic( compare , e , i - 1 , j )
		else :

			result = compare( i - 1 , j - 1 )

			if result > 0 :

				e[i][j] = dynamic( compare , e , i - 1 , j )

			elif result < 0 :

				e[i][j] = dynamic( compare , e , i , j - 1 )

			else :

				e[i][j] = dynamic( compare , e , i - 1 , j ) + dynamic( compare , e , i , j - 1 )


	return e[i][j]


def fill ( compare , e , m , n ) :

	dynamic( compare , e , m , n )

	for i , j in subscripts ( 0 , m + 1 , 0 , n + 1 ) :

		if e[i][j] is None : e[i][j] = 0

def tableau ( compare , m , n ) :

	e = grid( m , n )

	fill( compare , e , m , n )

	return e

def compute ( compare , m , n ) :

	e = tableau( compare , m , n )

	print( "count of linear extensions" )
	print( show( e ) , end = "" )

	return e[m][n]


def main ( partial ) :

	P , m , n = parse( partial )

	print( "partial information" )
	print( show( P ) , end = "" )

	compare = comparator( P )

	print( compute( compare , m , n ) )


if __name__ == "__main__" :

	import sys , fileinput

	main( *map( fileinput.input , [ [ f ] for f in sys.argv[1:] ] ) )
