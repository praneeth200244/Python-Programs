class Vector:
    def __init__(self, i, j, k) -> None:
        self.x = i
        self.y = j
        self.z = k

    def __str__(self) -> str:
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __add__(self, x):
        return Vector(self.x+x.x, self.y+x.y, self.z+x.z)


v1 = Vector(1, 2, 3)
print(v1)

v2 = Vector(4, 5, 6)
print(v2)

print(v1 + v2)
