alphabet = list(map(chr, range(97, 123)))

def bon(w):
	count = 0
	for index in range(len(w)):
		if w[index] == w[index + 1]:
			for letter in alphabet:
				if w[index] == letter:
					res = (1 + count) * 4
				count += 1
			return res

secretCode = input("Enter secret code : ")
print(bon(secretCode))