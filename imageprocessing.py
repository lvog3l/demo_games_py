from PIL import Image
import numpy

# Box Blur kernel
from numpy import sqrt

box_kernel = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]

# high pass kernel
sharpen = [[0, -1, 0],
           [-1, 5, -1],
           [0, -1, 0]]

# emboss
emboss = [[-2, -1, 0],
          [-1, 1, 1],
          [0, 1, 2]]

# Gaussian kernel small
blur_small = [[1 / 256, 4 / 256, 6 / 256, 4 / 256, 1 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [1 / 256, 4 / 256, 6 / 256, 4 / 256, 1 / 256]]

# Gaussian kernel large
blur_large = [[0, 0, 0, 0, 5, 0, 0, 0, 0],
              [0, 0, 5, 18, 32, 18, 5, 0, 0],
              [0, 5, 5, 18, 64, 18, 5, 5, 0],
              [5, 5, 18, 64, 100, 64, 18, 5, 5],
              [5, 18, 64, 100, 100, 100, 64, 18, 5],
              [5, 5, 18, 64, 100, 64, 18, 5, 5],
              [0, 5, 5, 18, 64, 18, 5, 5, 0],
              [0, 0, 5, 18, 32, 18, 5, 0, 0],
              [0, 0, 0, 0, 5, 0, 0, 0, 0]]


def display_menu():
    print("Available Filters: ")
    print("________________________________________")
    print("1. Brightness\n"
          "2. Box Blur\n"
          "3. Gaussian Blur\n"
          "4. Gaussian Blur - larger\n"
          "5. Sharpen\n"
          "6. Emboss\n"
          "7. Custom processing")


class ImageProcessing:
    def __init__(self):
        self.img = None
        self.img_array = None
        self.height = None
        self.width = None
        self.channels = None

    def process(self):
        image_path = input("Enter the path to your image: ")  # venv/Images/Michelle_small.jpg
        self.img = Image.open(image_path)
        self.img_array = numpy.asarray(self.img)
        self.height = self.img_array.shape[0]
        self.width = self.img_array.shape[1]
        self.channels = self.img_array.shape[2]
        display_menu()
        filter_choice = input("Select number of filter to apply: ")
        choice = int(str(filter_choice))
        if choice == 1:
            factor = float(input("Enter value from -10.0 to 10.0, to darken or lighten: "))
            self.lighten(factor)
        elif choice == 2:
            self.convolution(box_kernel)
        elif choice == 3:
            self.convolution(blur_small)
        elif choice == 4:
            self.convolution(blur_large)
        elif choice == 5:
            self.convolution(sharpen)
        elif choice == 6:
            self.convolution(emboss)
        elif choice == 7:
            print('enter your own custom [n x n] kernel (where n is odd). '
                  'Enter \n'
                  '[0 ,0 ,0]\n'
                  '[1, 1, 1]\n'
                  '[0, 0, 0]\n'
                  'as: 0,0,0,1,1,1,0,0,0\n')
            input_string = input("Custom Kernel: ")
            temp = list(map(float, input_string.split(",")))
            inner = len(temp)
            outer = int(sqrt(len(temp)))
            custom_kernel = []
            for i in range(outer):
                temp2 = []
                for j in range(0+i, outer + i):
                    temp2.append(temp[i])
                custom_kernel.append(temp2)
            if inner > 3: print("This might take a while . . . . ")
            self.convolution(custom_kernel)

    def lighten(self, factor):
        im2 = self.img_array.copy()
        for h in range(self.height):
            for w in range(self.width):
                for c in range(self.channels):
                    val = min(self.img_array[h, w, c] * factor, 255)
                    if val > 255:
                        val = 255
                    im2[h, w, c] = val
        Image.fromarray(im2.astype('uint8'), 'RGB').show()

    def convolution(self, kernel):
        im2 = self.img_array.copy()
        offset = len(kernel) // 2
        for x in range(offset, self.width - offset):
            for y in range(offset, self.height - offset):
                acc = [0, 0, 0]
                for a in range(len(kernel)):
                    for b in range(len(kernel)):
                        xn = x + a - offset
                        yn = y + b - offset
                        # print(x, y, a, b, offset, xn, yn)
                        pixel = self.img_array[yn, xn]
                        # print("before: ")
                        # print(pixel)
                        acc[0] += pixel[0] * kernel[a][b]
                        acc[1] += pixel[1] * kernel[a][b]
                        acc[2] += pixel[2] * kernel[a][b]
                        # print(acc[0], acc[1], acc[2])
                # pixel     = acc
                # print("after: ")
                # print(pixel)
                acc[0] = max(0, min(255, acc[0]))
                acc[1] = max(0, min(255, acc[1]))
                acc[2] = max(0, min(255, acc[2]))
                im2[y, x] = [int(acc[0]), int(acc[1]), int(acc[2])]
        Image.fromarray(im2.astype('uint8'), 'RGB').show()

# im = Image.open("venv/Images/KellyKlass.png")
# nm = numpy.asarray(im)
# height, width, channels = nm.shape
# for i in range(10):
#     for j in range(10):
#         print(nm[i, j])
# # height = 10
# # width = 10
# print(height, width, channels)
