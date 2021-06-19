letters= {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

letters ["A"] = 0
letters ["B"] -= 1
letters ["C"] -= 1
letters ["D"] -= 1
letters ["E"] -= 1

letter_A = letters["A"]
print(letter_A)
letter_A2 = letters["A"]

letter_B = letters["B"]
print(letter_B)
letter_B2 = letters["B"]

letter_C = letters["C"]
print(letter_C)
letter_C2 = letters["C"]

letter_D = letters["D"]
print(letter_D)

letter_E = letters["E"]
print(letter_E)

del letters["A"]
del letters["B"]

print(letter_A)
print(letter_B)
print(letter_C)
print(letter_D)
print(letter_E)
