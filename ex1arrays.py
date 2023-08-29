
v = [2,6,8,3,10,9,1,21,33,14]
X = 2
Y = 4

print(f"A: {v[X+1]}")
print(f"B: {v[X+2]}")
print(f"C: {v[X+3]}")
print(f"D: {v[X*4]}")
print(f"E: {v[X*1]}")
print(f"F: {v[X*2]}")
print(f"G: {v[X*3]}")
print(f"H: {v[v[X+Y]]}")
print(f"I: {v[X+Y]}")
print(f"J: {v[8-v[2]]}")
print(f"K: v[v[4]] Fora do range")
print(f"L: v[ v[ v[7]]]  Fora do range")
print(f"M: v[v[1]*v[4]]  Fora do range")
print(f"N: {v[X+4]}")