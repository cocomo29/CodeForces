n = int(input())
output = 0
for i in range(n):
    polyhedron = input()
    polyhedron = polyhedron.lower()
    if polyhedron == "tetrahedron":
        output += 4
    elif polyhedron == "cube":
        output += 6
    elif polyhedron == "octahedron":
        output += 8
    elif polyhedron == "dodecahedron":
        output += 12
    elif polyhedron == "icosahedron":
        output += 20
print(output)