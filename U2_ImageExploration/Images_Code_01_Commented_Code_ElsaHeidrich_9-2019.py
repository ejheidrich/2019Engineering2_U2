# Images_01_Starting_Code
# Kyle Fricke and Cheryl Farmer, Engineer Your World
#Engineering 2 9/27/19
#Edited by Elsa Heidrich
"""This code takes an original image, converts it to grayscale, 
separates the image by a certain grayscale value, and creates a 
new image with the new color values in replace of grayscale values.
"""
#importing libraries needed
import cv2
import numpy
import os.path

#get file from user and checks to see if it exists
print "Save your original image in the same folder as this program."
filename_valid = False
#assumes file does not exist
while filename_valid == False:
    filename = raw_input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
#if the file exists, change the existence the true     
    if os.path.isfile(filename) == True:
        filename_valid = True
#If the file name does not exists, prompts user to try again        
    else:
        print "Something was wrong with that filename. Please try again."

#converts the original image to black and white picture
OGimg = cv2.imread(filename,1)
gs_image_simple = cv2.imread(filename, 0)
gs_image = cv2.cvtColor(gs_image_simple, cv2.COLOR_GRAY2BGR)

#creates/names windows of 5 different parts of image: original, grayscale, red, yellow, and new
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Color0 Parts of Image')
cv2.namedWindow('Color1 Parts of Image')
cv2.namedWindow('Customized Image')

#defining image height, width, and channels
imgH = OGimg.shape[0]
imgW = OGimg.shape[1]
imgC = OGimg.shape[2]

# creates numpy arrays (papers) that has the same dimensions and channels for image
color0_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color1_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
#colors the paper with BGR
color0_paper[0:imgH,0:imgW, 0:imgC] = [0,0,255]
color1_paper[0:imgH,0:imgW, 0:imgC] = [0,255,255]

# defines break between gray shades for color0 and color1 
gs_break = 100

# defines which intervals of grayscale values are for yellow(color1) and red(color0)
min_gs_color0 = [0,0,0]
max_gs_color0 = [gs_break,gs_break,gs_break]
min_gs_color1 = [gs_break+1,gs_break+1,gs_break+1]
max_gs_color1 = [255,255,255]

#make sure array is the right data type
min_gs_color0 = numpy.array(min_gs_color0, dtype = "uint8")
max_gs_color0 = numpy.array(max_gs_color0, dtype = "uint8")
min_gs_color1 = numpy.array(min_gs_color1, dtype = "uint8")
max_gs_color1 = numpy.array(max_gs_color1, dtype = "uint8")

#defines color0 and color1 parts of image separately using masks
color0mask = cv2.inRange(gs_image, min_gs_color0, max_gs_color0)
color1mask = cv2.inRange(gs_image, min_gs_color1, max_gs_color1)

# separates color0 (red) and color1(yellow) parts of image
color0parts = cv2.bitwise_or(color0_paper, color0_paper, mask = color0mask)
color1parts = cv2.bitwise_or(color1_paper, color1_paper, mask = color1mask)

#defines what the new image will be (color0 plus color1)
custom_img = cv2.bitwise_or(color0parts, color1parts)

#displays different aspects of the images on different windows
cv2.imshow('Original Image', OGimg)
cv2.imshow('Grayscale Image',gs_image)
cv2.imshow('Color0 Parts of Image',color0parts)
cv2.imshow('Color1 Parts of Image',color1parts)
cv2.imshow('Customized Image',custom_img)

#allows user to view image until they either saave or escape the images
keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',gs_image)
    cv2.imwrite('photo_RY_1.jpg',custom_img)
    cv2.destroyAllWindows()
