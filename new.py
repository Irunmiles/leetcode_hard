#https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
def main():

	A = [
	  [9,9,4],
	  [6,6,8],
	  [2,1,1]
	]

	matrix = {row_index + column_index*1j: value
				for row_index, row in enumerate(A) for column_index, value in enumerate(row)}

	length = dict.fromkeys(matrix.keys(), 1)

	for z in sorted(matrix, key=matrix.get):
		length[z] = 1 + max([
						length[Z] for Z in (z+1, z-1, z+1j, z-1j)
						if Z in matrix and matrix[z] > matrix[Z]
						]  or  [0])
	print(max(length.values()   or   [0]))





if __name__ == "__main__":
	main()
