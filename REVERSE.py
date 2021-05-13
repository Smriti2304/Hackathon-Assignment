def PrintReverseOrder(N):
	if (N <= 0):
		return
	else:
		print(N, end = " ")
		PrintReverseOrder(N - 1)
N = int(input("Enter number"))
PrintReverseOrder(N)

