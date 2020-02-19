import pandas as pd 
from PIL import Image
import numpy as np
data_csv = pd.read_csv('./MNIST_test_small.csv')
data_filtered = data_csv[data_csv['7'] == 3]
print(data_filtered)


for t in range(10):

    firstrow = data_filtered.iloc[t]
 
    w, h = 28, 28
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[0:256, 0:256] = [0, 0, 0] # red patch in upper left


    image = []
    for s in range(len(firstrow)):
        if s > 0:
            image.append(firstrow[s])

    b=0
    for i in range(w):
        for a in range(h):
            data[i,a] = [int(image[b]), 0, 0]
            b = b + 1

    img = Image.fromarray(data, 'RGB')
    img.save('my.png')
    img.show()
