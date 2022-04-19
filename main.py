from os import system
import hangman
import imageprocessing
import mastermind
import islandfinder
from PIL import Image
import numpy
import boards
import minesweeper
import random

done = False


def clear():
    _ = system('clear')


def show_menu():
    print("Games: ")
    print("________________________________________")
    print("1. Hangman\n"
          "2. Mastermind\n"
          "3. Island Finder\n"
          "4. Mine Sweeper\n"
          "5. Image Processing")


while not done:
    show_menu()
    selection = input("Select number you'd like to try ('q' to quit): ")
    if selection == "1":
        hm = hangman.Hangman()
        hm.play()
    elif selection == "2":
        mm = mastermind.Mastermind()
        mm.play()
    elif selection == "3":
        i_finder = islandfinder.IslandFinder()
        i_finder.find_islands()
    elif selection == "4":
        size = input("Minesweeper: enter the size of board (5-20): ")
        ms = minesweeper.Minesweeper(int(size))
        ms.play()
    elif selection == "5":
        im = imageprocessing.ImageProcessing()
        im.process()
    elif selection == "q":
        done = True
    else:
        "invalid selection"

# from PIL import Image, ImageDraw
#
# # Load image:
# input_image = Image.open("venv/Images/Michelle_small.jpg")
# input_pixels = input_image.load()
#
# # Box Blur kernel
# box_kernel = [[1 / 9, 1 / 9, 1 / 9],
#               [1 / 9, 1 / 9, 1 / 9],
#               [1 / 9, 1 / 9, 1 / 9]]
#
# high_pass_kernel = [[0, -.5, 0],
#                     [-.5, 3, -.5],
#                     [0, -.5, 0]]
#
# # Gaussian kernel
# gaussian_kernel = [[1 / 128, 4 / 128, 6 / 128, 4 / 128, 1 / 128],
#                    [4 / 128, 16 / 128, 24 / 128, 16 / 128, 4 / 128],
#                    [6 / 128, 24 / 128, 36 / 128, 24 / 128, 6 / 128],
#                    [4 / 128, 16 / 128, 24 / 128, 16 / 128, 4 / 128],
#                    [1 / 128, 4 / 128, 6 / 128, 4 / 128, 1 / 128]]
#
# # Select kernel here:
# kernel = high_pass_kernel
#
# # Middle of the kernel
# offset = len(kernel) // 2
#
# # Create output image
# output_image = Image.new("RGB", input_image.size)
# draw = ImageDraw.Draw(output_image)
#
# # Compute convolution between intensity and kernels
# for x in range(offset, input_image.width - offset):
#     for y in range(offset, input_image.height - offset):
#         acc = [0, 0, 0]
#         for a in range(len(kernel)):
#             for b in range(len(kernel)):
#                 xn = x + a - offset
#                 yn = y + b - offset
#                 # print(x, y, a, b, offset, xn, yn)
#                 pixel = input_pixels[xn, yn]
#                 # print("pixel before: ")
#                 # print(pixel)
#                 acc[0] += pixel[0] * kernel[a][b]
#                 acc[1] += pixel[1] * kernel[a][b]
#                 acc[2] += pixel[2] * kernel[a][b]
#         # print("pixel after: ---------------------------------------")
#         # print(pixel)
#         # print("coords " + str(x) + " " + str(y))
#         print("accumulator: ")
#         print(acc[0], acc[1], acc[2])
#         draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
#         point = (x, y)
#         # print("point coords " + str(point))
#         print("new image pixel from accumulator")
#         print(output_image.getpixel(point))
#
# output_image.show()

# ip = imageprocessing.ImageProcessing("venv/Images/Michelle_bw.jpg", "lighten")
# matrix = [[0, 0, 0, 0, 5, 0, 0, 0, 0],
#           [0, 0, 5, 18, 32, 18, 5, 0, 0],
#           [0, 5, 5, 18, 64, 18, 5, 5, 0],
#           [5, 5, 18, 64, 100, 64, 18, 5, 5],
#           [5, 18, 64, 100, 100, 100, 64, 18, 5],
#           [5, 5, 18, 64, 100, 64, 18, 5, 5],
#           [0, 5, 5, 18, 64, 18, 5, 5, 0],
#           [0, 0, 5, 18, 32, 18, 5, 0, 0],
#           [0, 0, 0, 0, 5, 0, 0, 0, 0]]
# temp = numpy.asarray(matrix)
# kernel = (25 - temp) * 1/1024
# print(kernel)
# # print(kernel)
# # print(len(kernel))
# ip.convolution(kernel)
# mm = minesweeper.Minesweeper(10)
# mm.play()
