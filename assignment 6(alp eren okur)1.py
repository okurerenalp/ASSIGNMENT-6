primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
fakePrimeNumbers = []
for i in range(len(primeNumbers) - 1):
    fakePrimeNumber = primeNumbers[i] * primeNumbers[i + 1]
    fakePrimeNumbers.append(fakePrimeNumber)

print(fakePrimeNumbers)