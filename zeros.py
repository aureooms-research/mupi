

def main ( m , n ) :

	from matrix import mat , show

	M = mat( m , n , 0 )
	print( show( M ) , end = "" )


if __name__ == "__main__" :

	import sys

	main( *map( int , sys.argv[1:] ) )
