#Images_03_Color_Sliders
#Kyle Fricke and Cheryl Farmer, Engineer Your World
#Engineering 2 10/7/19
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

#creates/names windows of for grayscale, color, and custom images and trackbar windows
cv2.namedWindow('Color Sliders', cv2.WINDOW_NORMAL)
cv2.namedWindow('GS Sliders', cv2.WINDOW_NORMAL)
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Grayscale Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color0 Parts of Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color1 Parts of Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color2 Parts of Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Customized Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Customized Image', 600, 600)

#display original and grayscale images
cv2.imshow('Original Image', OGimg)
cv2.imshow('Grayscale Image',gs_image)

#defining image height, width, and channels
imgH = OGimg.shape[0]
imgW = OGimg.shape[1]
imgC = OGimg.shape[2]

# creates numpy arrays (papers) that has the same dimensions and channels for image
color0_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color1_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color2_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)


#create grayscale sliders
cv2.createTrackbar('GS1_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS2_position', 'GS Sliders', 127, 255, lambda x:None)
#create color sliders, each color has 3 sliders (BGR)
cv2.createTrackbar('Color0 B', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color0 G', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color0 R', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color1 B', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color1 G', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color1 R', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color2 B', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color2 G', 'Color Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('Color2 R', 'Color Sliders', 127, 255, lambda x:None)

#initialize while loop - we want to wait for user adjustment
keypressed = 1
while (keypressed != 27 and keypressed !=ord('s')):

    #read in the grayscale break value from the trackbar
    gs_break1 = cv2.getTrackbarPos('GS1_position', 'GS Sliders')
    gs_break2 = cv2.getTrackbarPos('GS2_position', 'GS Sliders')
    
    # defines which intervals of grayscale values are for different colors
    min_gs_color0 = [0,0,0]
    max_gs_color0 = [gs_break1,gs_break1,gs_break1]
    min_gs_color1 = [gs_break1+1,gs_break1+1,gs_break1+1]
    max_gs_color1 = [gs_break2,gs_break2,gs_break2]
    min_gs_color2 = [gs_break2+1,gs_break2+1,gs_break2+1]
    max_gs_color2 = [255,255,255]
    
    #make sure array is the right data type
    min_gs_color0 = numpy.array(min_gs_color0, dtype = "uint8")
    max_gs_color0 = numpy.array(max_gs_color0, dtype = "uint8")
    min_gs_color1 = numpy.array(min_gs_color1, dtype = "uint8")
    max_gs_color1 = numpy.array(max_gs_color1, dtype = "uint8")
    min_gs_color2 = numpy.array(min_gs_color2, dtype = "uint8")
    max_gs_color2 = numpy.array(max_gs_color2, dtype = "uint8")
    
    #create variables defined as the value given from the color sliders (BGR values)
    color0_B = cv2.getTrackbarPos('Color0 B', 'Color Sliders')
    color0_G = cv2.getTrackbarPos('Color0 G', 'Color Sliders')
    color0_R = cv2.getTrackbarPos('Color0 R', 'Color Sliders')
    color1_B = cv2.getTrackbarPos('Color1 B', 'Color Sliders')
    color1_G = cv2.getTrackbarPos('Color1 G', 'Color Sliders')
    color1_R = cv2.getTrackbarPos('Color1 R', 'Color Sliders')
    color2_B = cv2.getTrackbarPos('Color2 B', 'Color Sliders')
    color2_G = cv2.getTrackbarPos('Color2 G', 'Color Sliders')
    color2_R = cv2.getTrackbarPos('Color2 R', 'Color Sliders')
    
    #colors the paper with BGR values from sliders
    color0_paper[0:imgH, 0:imgW, 0:imgC] = [color0_B, color0_G, color0_R]
    color1_paper[0:imgH, 0:imgW, 0:imgC] = [color1_B, color1_G, color1_R]
    color2_paper[0:imgH, 0:imgW, 0:imgC] = [color2_B, color2_G, color2_R]

    #defines different color parts of image separately using masks
    color0mask = cv2.inRange(gs_image, min_gs_color0, max_gs_color0)
    color1mask = cv2.inRange(gs_image, min_gs_color1, max_gs_color1)
    color2mask = cv2.inRange(gs_image, min_gs_color2, max_gs_color2)
    
    #separates different color parts of image
    color0parts = cv2.bitwise_or(color0_paper, color0_paper, mask = color0mask)
    color1parts = cv2.bitwise_or(color1_paper, color1_paper, mask = color1mask)
    color2parts = cv2.bitwise_or(color2_paper, color2_paper, mask = color2mask)
    
    #defines what the new image will be by adding different color parts
    temp_img1 = cv2.bitwise_or(color0parts, color1parts)
    custom_img = cv2.bitwise_or(temp_img1, color2parts)
    
    #displays different aspects of the images on different windows
    cv2.imshow('Color0 Parts of Image', color0parts)
    cv2.imshow('Color1 Parts of Image', color1parts)
    cv2.imshow('Color2 Parts of Image', color2parts)
    cv2.imshow('Customized Image', custom_img)
    
   #updates images consistently
    keypressed = cv2.waitKey(1)
     #allows user to view image until they either save or escape the images
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',gs_image)
    cv2.imwrite('photo_RY_1.jpg',custom_img)
    cv2.destroyAllWindows()
