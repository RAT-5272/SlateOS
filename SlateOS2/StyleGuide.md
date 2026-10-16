# Naming Conventions

### Rough priority list <small><small><small>(Lower is higher)</small></small></small>
1. flatcase
2. snake_case
3. camelCase
4. PascalCase
5. FULLCASE (unused)
6. SCREAMING_SNAKE_CASE

# Encouraged practices
- Modules and submodules: PascalCase.PascalCase (e.g. Renderer.Interface)
- Types: PascalCase (Structs, enums, generics, classes, or normal types) (e.g. DatabaseManager)
- Functions: PascalCase (e.g. LoadFilesFromPath)
- Variables
  - Short term: snake_case (e.g. iterators, this is just optional though) (e.g. i, slot_index)
  - Bools: Should have some word beforehand like is, has, contains (e.g. isPrime, hasChild, containsSubstring)
  - Regular variables: camelCase
  - Constants: SCREAMING_SNAKE_CASE
- Types / extra placed AFTER variable name (hungarian notation, optional): variableName_PascalCase (e.g. UnrollAndFMA_512)
- If something is private, it should be prepended with an underscore.

### Comments & Documentation

```py
"""
Documentation comments should ideally be used in nearly every function or class, they are placed at the beginning and detail what the function does at a high level, as well as what is inputted or returned.
"""

#Inline comments give some information about what the code around it is doing. Kinda obvious
```

# Full Example Styled Code

```py
import math

class PrimesManager:
	"""
	Shush I just wanted to include a class

	Methods:
	IsPrime(number)
	SieveOfEratosthenes_Naive(n)
	"""

	def IsPrime_Naive(number: int) -> bool:
		"""
		Naively iterates through 2 to sqrt(number) checking for primality.
		"""
		isPrime = True
		for i in range(2, int(math.sqrt(number)) + 1):
			if (number / i).is_integer():
				isPrime = False
		return isPrime

	def SieveOfEratosthenes_Naive(n: int) -> list[int]:
		"""
		Returns a list of all prime numbers up to some integer n (inclusive)
		"""

		numbers: list[bool] = [True] * (n+1)
		numbers[0] = False
		numbers[1] = False

		# Iterate up to sqrt(n)
		# Set all multiples of i to false if i is not prime
		for i in range(2, int(math.sqrt(n)) + 1):
			if numbers[i]:
				for j in range(i*i, n+1, i):
					numbers[j] = False

		# List comprehension to extract all primes from the array
		allPrimes = [p for p in range(0, n + 1) if numbers[p]]

		return allPrimes
```