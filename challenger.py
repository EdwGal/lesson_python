import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x= np.linspace(-5, 5, 100)
y= np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()


nums = [5, 2, 8, 1]
r = 0
for i in range(len(nums)):
    r += nums[i] -i

print(r)
#numero2
rows = 8
cols = 8
for i in range(rows):
    for j in range(cols):
        if ( i + j ) % 2 == 0:
            print("X", end="-")
        else:
            print("O", end=".")
    print()
#numero3
rows = 10
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
#numero4
message = "   Feliz Navidad"
edge = "*" * len(message)
print(edge)
print(message)
print(edge)
#numero5

from barcode import Code128
from barcode.writer import ImageWriter
from IPython.display import Image, display

clcoding = Code128("123456789012", writer=ImageWriter())
filename = clcoding.save("barcode_image")
display(Image(filename="barcode_image.png"))
 
<<<<<<< HEAD
=======
#numero 6
def misterio(palabra):
    parte1 = palabra[:2]
    parte2 = palabra[2:]
    return parte2 + parte1

print(misterio("PYTHON"))

name = "edward galvez     "
print(name.title())
print(name.upper())
print(name.lower())
print(name.rstrip())
>>>>>>> 477b8e0c54424a327e36e79b84c409dd186cfc4f
