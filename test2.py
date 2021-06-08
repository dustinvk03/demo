import matplotlib.pyplot as plt 
from random import choice
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from matplotlib.pyplot import imshow

# plt.rc('figure', figsize = (12,6))

# values = list(range(0,55,5))

# x_axis = list(i/10 for i in range(0, 11, 1))
# print(x_axis)

# plt.plot(x_axis, values, 'o--')
# plt.xlim(0,1)
# plt.ylim(0,100)
# plt.title('The plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

file_name = 'MMR.jpg'
im = Image.open(file_name)
imshow(im)
