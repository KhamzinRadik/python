a = "abcd"
b = (10, 20, 30, 40)

g = ((a[i], b[i]) for i in range(min(len(a), len(b))))

print(g)
print(*g, sep='\n')