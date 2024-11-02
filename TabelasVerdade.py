import ttg

# Tabela verdade cenario 1
answer = ttg.Truths(
    ["p", "r", "s", "c", "u", "h", "m"],
    ["(p and r and c and m and u and h) and not s"],
    ints=False,
)
print(answer)
print(answer.valuation())

# Tabela verdade cenario 2
answer =  ttg.Truths(
    ["e", "q", "a", "n", "u"],
    ["(q and a and n and u) and (not e)"],
    ints=False,
)
print(answer)
print(answer.valuation())

# Tabela verdade cenario 3
answer = ttg.Truths(
    ["q", "r", "c", "s", "m", "o"],
    ["(r and c and s and m and o) and (not q)"],
    ints=False,
)
print(answer)
print(answer.valuation())
