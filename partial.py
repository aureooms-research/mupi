
from combinatorics import choose
from random import randint
from information import fix

def partial ( M , m , n ) :

	# fill M
	# we assume that for all j > i --> ai < aj and bi < bj
	# M[i][j] = -1 means ai < bj
	# M[i][j] =  1 means ai > bj
	# M[i][j] =  0 means ai and bj are incomparable

	# generate random partial info

	positions = sorted( choose( m + n , m ) )

	for i , j in enumerate( positions ) :

		M[i][:j-i] = [ randint(  0 , 1 ) ] * ( j - i )
		M[i][j-i:] = [ randint( -1 , 0 ) ] * ( n - j + i )

	fix( M , m , n )

	return M


def main ( m , n ) :

	from matrix import mat , show

	M = mat( m , n )
	partial( M , m , n )
	print( show( M ) , end = "" )


if __name__ == "__main__" :

	import sys

	main( *map( int , sys.argv[1:] ) )
