from matrix import mat , show , subscripts , parse
from information import comparator


def grid ( m , n ) :

	e = mat( m + 1 , n + 1 , [ ] )

	e[0][0] = [ [ ] ]

	for i in range ( 1 , m + 1 ) :

		e[i][0] = [ [ "a[%d]" % k for k in range( 1 , i + 1 ) ] ]

	for j in range ( 1 , n + 1 ) :

		e[0][j] = [ [ "b[%d]" % k for k in range( 1 , j + 1 ) ] ]

	return e

def gen ( compare , e , i , j ) :

	"""

		>>> compare = comparator( [ [ 0 , 0 ] , [ 0 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		6

		>>> compare = comparator( [ [ 1 , 0 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		3

		>>> compare = comparator( [ [ -1 , -1 ] , [ -1 , -1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		1

		>>> compare = comparator( [ [ -1 , -1 ] , [ 0 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		3

		>>> compare = comparator( [ [ 1 , 1 ] , [ 1 , 1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		1

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		4

		>>> compare = comparator( [ [ 0 , -1 ] , [ 1 , 1 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		2

		>>> compare = comparator( [ [ -1 , -1 ] , [ 1 , 0 ] ] )
		>>> e = grid( 2 , 2 )
		>>> len( gen( compare , e , 2 , 2 ) )
		2

	"""

	if not e[i][j] :

		result = compare( i - 1 , j - 1 )

		if result > 0 :

			e[i][j] = [ ext + [ "a[%d]" % i ] for ext in gen( compare , e , i - 1 , j ) ]

		elif result < 0 :

			e[i][j] = [ ext + [ "b[%d]" % j ] for ext in gen( compare , e , i , j - 1 ) ]

		else :

			e[i][j]  = [ ext + [ "a[%d]" % i ] for ext in gen( compare , e , i - 1 , j ) ]
			e[i][j] += [ ext + [ "b[%d]" % j ] for ext in gen( compare , e , i , j - 1 ) ]

	return e[i][j]


def compute ( compare , m , n ) :

	e = grid( m , n )

	gen( compare , e , m , n )

	return e[m][n]


def main ( lines ) :

	M , m , n = parse( lines )

	compare = comparator( M )

	for ext in compute( compare , m , n ) :

		print( *ext , sep = " < " )


if __name__ == "__main__" :

	import fileinput

	main( fileinput.input( ) )
