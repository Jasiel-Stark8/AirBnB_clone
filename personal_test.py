try:
	n = int(input())
	print(n * 10)
except EOFError:
  print("Nothing was read")
except ValueError:
    print("No number entered")
