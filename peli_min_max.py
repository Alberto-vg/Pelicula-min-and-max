import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

minimos = []
maximos = []

for i in range(1, 632):
    image_path = "frame" + str(i).rjust(4, "0") + ".png"
    image = mpimg.imread(image_path)
    recorte = image[750:1000, 300:600]
    minimos.append(np.min(recorte))
    maximos.append(np.max(recorte))

plt.plot(minimos)
plt.plot(maximos)
plt.show()

