#Images_06_Color_Sliders_Naming_Custom_Image_Saving_Color_Combo
#Kyle Fricke and Cheryl Farmer, Engineer Your World
#Engineering 2 10/28/19
#Edited by Elsa Heidrich
"""This code takes an original image, converts it to grayscale, 
separates the image by a certain grayscale value, and creates a 
new image with the new color values in replace of grayscale values
using BGR values and grayscale breaks from trackbar position provided
by the user.
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

#if the file name does not exists, prompts user to try again        
    else:
        print "Something was wrong with that filename. Please try again."

#opens text file for the color combo 
ColorC = open('Color Combo.txt','w')

#converts the original image to grayscale image
OGimg = cv2.imread(filename,1)
gs_image_simple = cv2.imread(filename, 0)
gs_image = cv2.cvtColor(gs_image_simple, cv2.COLOR_GRAY2BGR)

#creates/names windows for grayscale, and custom images and trackbar (color and grayscale) windows
cv2.namedWindow('Color0 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color1 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color2 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color3 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color4 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color5 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color6 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color7 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color8 Slider', cv2.WINDOW_NORMAL)
cv2.namedWindow('GS Sliders')
cv2.resizeWindow('GS Sliders', 350, 420)
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Grayscale Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Customized Image', cv2.WINDOW_NORMAL)

#display original and grayscale images
cv2.imshow('Original Image', OGimg)
cv2.imshow('Grayscale Image',gs_image)

#defining image height, width, and channels
imgH = OGimg.shape[0]
imgW = OGimg.shape[1]
imgC = OGimg.shape[2]

#creates numpy arrays (papers) that has the same dimensions and channels for image for each color
color0_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color1_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color2_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color3_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color4_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color5_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color6_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color7_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)
color8_paper = numpy.zeros((imgH,imgW,imgC), numpy.uint8)

#create grayscale sliders (values from 0 to 255)
cv2.createTrackbar('GS1_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS2_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS3_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS4_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS5_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS6_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS7_position', 'GS Sliders', 127, 255, lambda x:None)
cv2.createTrackbar('GS8_position', 'GS Sliders', 127, 255, lambda x:None)

#create color sliders, each color has 3 sliders (BGR values for each color (0 to 255))
cv2.createTrackbar('Color0 B', 'Color0 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color0 G', 'Color0 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color0 R', 'Color0 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color1 B', 'Color1 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color1 G', 'Color1 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color1 R', 'Color1 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color2 B', 'Color2 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color2 G', 'Color2 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color2 R', 'Color2 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color3 B', 'Color3 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color3 G', 'Color3 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color3 R', 'Color3 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color4 B', 'Color4 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color4 G', 'Color4 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color4 R', 'Color4 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color5 B', 'Color5 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color5 G', 'Color5 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color5 R', 'Color5 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color6 B', 'Color6 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color6 G', 'Color6 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color6 R', 'Color6 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color7 B', 'Color7 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color7 G', 'Color7 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color7 R', 'Color7 Slider', 127, 255, lambda x:None)

cv2.createTrackbar('Color8 B', 'Color8 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color8 G', 'Color8 Slider', 127, 255, lambda x:None)
cv2.createTrackbar('Color8 R', 'Color8 Slider', 127, 255, lambda x:None)


#initialize while loop - we want to wait for user adjustment
keypressed = 1
while (keypressed != 27 and keypressed !=ord('s')):

    #read in the grayscale break value from the trackbar
    gs_break1 = cv2.getTrackbarPos('GS1_position', 'GS Sliders')
    gs_break2 = cv2.getTrackbarPos('GS2_position', 'GS Sliders')
    gs_break3 = cv2.getTrackbarPos('GS3_position', 'GS Sliders')
    gs_break4 = cv2.getTrackbarPos('GS4_position', 'GS Sliders')
    gs_break5 = cv2.getTrackbarPos('GS5_position', 'GS Sliders')
    gs_break6 = cv2.getTrackbarPos('GS6_position', 'GS Sliders')
    gs_break7 = cv2.getTrackbarPos('GS7_position', 'GS Sliders')
    gs_break8 = cv2.getTrackbarPos('GS8_position', 'GS Sliders')
   
    #using if statements preventsconsecutive grayscale breaks from being less than previous break
    if gs_break1 >=gs_break2:
        cv2.setTrackbarPos('GS1_position', 'GS Sliders', gs_break2-1)
    if gs_break2 >=gs_break3:
        cv2.setTrackbarPos('GS2_position', 'GS Sliders', gs_break3-1)
    if gs_break3 >=gs_break4:
        cv2.setTrackbarPos('GS3_position', 'GS Sliders', gs_break4-1)
    if gs_break4 >=gs_break5:
        cv2.setTrackbarPos('GS4_position', 'GS Sliders', gs_break5-1)
    if gs_break5 >=gs_break6:
        cv2.setTrackbarPos('GS5_position', 'GS Sliders', gs_break6-1)
    if gs_break6 >=gs_break7:
        cv2.setTrackbarPos('GS6_position', 'GS Sliders', gs_break7-1)
    if gs_break7 >=gs_break8:
        cv2.setTrackbarPos('GS7_position', 'GS Sliders', gs_break8-1)
        
    #defines which intervals of grayscale values are for different colors using grayscale trackbar positions
    min_gs_color0 = [0,0,0]
    max_gs_color0 = [gs_break1,gs_break1,gs_break1]
    
    min_gs_color1 = [gs_break1+1,gs_break1+1,gs_break1+1]
    max_gs_color1 = [gs_break2,gs_break2,gs_break2]
    
    min_gs_color2 = [gs_break2+1,gs_break2+1,gs_break2+1]
    max_gs_color2 = [gs_break3,gs_break3,gs_break3]
    
    min_gs_color3 = [gs_break3+1,gs_break3+1,gs_break3+1]
    max_gs_color3 = [gs_break4,gs_break4,gs_break4]
    
    min_gs_color4 = [gs_break4+1,gs_break4+1,gs_break4+1]
    max_gs_color4 = [gs_break5,gs_break5,gs_break5]
    
    min_gs_color5 = [gs_break5+1,gs_break5+1,gs_break5+1]
    max_gs_color5 = [gs_break6,gs_break6,gs_break6]
    
    min_gs_color6 = [gs_break6+1,gs_break6+1,gs_break6+1]
    max_gs_color6 = [gs_break7,gs_break7,gs_break7]
    
    min_gs_color7 = [gs_break7+1,gs_break7+1,gs_break7+1]
    max_gs_color7 = [gs_break8,gs_break8,gs_break8]
    
    min_gs_color8 = [gs_break8+1,gs_break8+1,gs_break8+1]
    max_gs_color8 = [255,255,255]
    
    #make sure array is the right data type for each color
    min_gs_color0 = numpy.array(min_gs_color0, dtype = "uint8")
    max_gs_color0 = numpy.array(max_gs_color0, dtype = "uint8")
    
    min_gs_color1 = numpy.array(min_gs_color1, dtype = "uint8")
    max_gs_color1 = numpy.array(max_gs_color1, dtype = "uint8")
    
    min_gs_color2 = numpy.array(min_gs_color2, dtype = "uint8")
    max_gs_color2 = numpy.array(max_gs_color2, dtype = "uint8")
    
    min_gs_color3 = numpy.array(min_gs_color3, dtype = "uint8")
    max_gs_color3 = numpy.array(max_gs_color3, dtype = "uint8")
    
    min_gs_color4 = numpy.array(min_gs_color4, dtype = "uint8")
    max_gs_color4 = numpy.array(max_gs_color4, dtype = "uint8")
    
    min_gs_color5 = numpy.array(min_gs_color5, dtype = "uint8")
    max_gs_color5 = numpy.array(max_gs_color5, dtype = "uint8")
    
    min_gs_color6 = numpy.array(min_gs_color6, dtype = "uint8")
    max_gs_color6 = numpy.array(max_gs_color6, dtype = "uint8")
    
    min_gs_color7 = numpy.array(min_gs_color7, dtype = "uint8")
    max_gs_color7 = numpy.array(max_gs_color7, dtype = "uint8")
    
    min_gs_color8 = numpy.array(min_gs_color8, dtype = "uint8")
    max_gs_color8 = numpy.array(max_gs_color8, dtype = "uint8")
    
    #create variables defined as the value given from the color sliders (BGR values) for each color
    color0_B = cv2.getTrackbarPos('Color0 B', 'Color0 Slider')
    color0_G = cv2.getTrackbarPos('Color0 G', 'Color0 Slider')
    color0_R = cv2.getTrackbarPos('Color0 R', 'Color0 Slider')
    
    color1_B = cv2.getTrackbarPos('Color1 B', 'Color1 Slider')
    color1_G = cv2.getTrackbarPos('Color1 G', 'Color1 Slider')
    color1_R = cv2.getTrackbarPos('Color1 R', 'Color1 Slider')

    color2_B = cv2.getTrackbarPos('Color2 B', 'Color2 Slider')
    color2_G = cv2.getTrackbarPos('Color2 G', 'Color2 Slider')
    color2_R = cv2.getTrackbarPos('Color2 R', 'Color2 Slider')

    color3_B = cv2.getTrackbarPos('Color3 B', 'Color3 Slider')
    color3_G = cv2.getTrackbarPos('Color3 G', 'Color3 Slider')
    color3_R = cv2.getTrackbarPos('Color3 R', 'Color3 Slider')
    
    color4_B = cv2.getTrackbarPos('Color4 B', 'Color4 Slider')
    color4_G = cv2.getTrackbarPos('Color4 G', 'Color4 Slider')
    color4_R = cv2.getTrackbarPos('Color4 R', 'Color4 Slider')
    
    color5_B = cv2.getTrackbarPos('Color5 B', 'Color5 Slider')
    color5_G = cv2.getTrackbarPos('Color5 G', 'Color5 Slider')
    color5_R = cv2.getTrackbarPos('Color5 R', 'Color5 Slider')
    
    color6_B = cv2.getTrackbarPos('Color6 B', 'Color6 Slider')
    color6_G = cv2.getTrackbarPos('Color6 G', 'Color6 Slider')
    color6_R = cv2.getTrackbarPos('Color6 R', 'Color6 Slider')
    
    color7_B = cv2.getTrackbarPos('Color7 B', 'Color7 Slider')
    color7_G = cv2.getTrackbarPos('Color7 G', 'Color7 Slider')
    color7_R = cv2.getTrackbarPos('Color7 R', 'Color7 Slider')

    color8_B = cv2.getTrackbarPos('Color8 B', 'Color8 Slider')
    color8_G = cv2.getTrackbarPos('Color8 G', 'Color8 Slider')
    color8_R = cv2.getTrackbarPos('Color8 R', 'Color8 Slider')

    #colors the paper with BGR values from color value sliders using variables from above
    color0_paper[0:imgH, 0:imgW, 0:imgC] = [color0_B, color0_G, color0_R]
    color1_paper[0:imgH, 0:imgW, 0:imgC] = [color1_B, color1_G, color1_R]
    color2_paper[0:imgH, 0:imgW, 0:imgC] = [color2_B, color2_G, color2_R]
    color3_paper[0:imgH, 0:imgW, 0:imgC] = [color3_B, color3_G, color3_R]
    color4_paper[0:imgH, 0:imgW, 0:imgC] = [color4_B, color4_G, color4_R]
    color5_paper[0:imgH, 0:imgW, 0:imgC] = [color5_B, color5_G, color5_R]
    color6_paper[0:imgH, 0:imgW, 0:imgC] = [color6_B, color6_G, color6_R]
    color7_paper[0:imgH, 0:imgW, 0:imgC] = [color7_B, color7_G, color7_R]
    color8_paper[0:imgH, 0:imgW, 0:imgC] = [color8_B, color8_G, color8_R]

    #defines different color parts of image separately using masks
    color0mask = cv2.inRange(gs_image, min_gs_color0, max_gs_color0)
    color1mask = cv2.inRange(gs_image, min_gs_color1, max_gs_color1)
    color2mask = cv2.inRange(gs_image, min_gs_color2, max_gs_color2)
    color3mask = cv2.inRange(gs_image, min_gs_color3, max_gs_color3)
    color4mask = cv2.inRange(gs_image, min_gs_color4, max_gs_color4)
    color5mask = cv2.inRange(gs_image, min_gs_color5, max_gs_color5)
    color6mask = cv2.inRange(gs_image, min_gs_color6, max_gs_color6)
    color7mask = cv2.inRange(gs_image, min_gs_color7, max_gs_color7)
    color8mask = cv2.inRange(gs_image, min_gs_color8, max_gs_color8)
    
    #separates different color parts of image using masks from above
    color0parts = cv2.bitwise_or(color0_paper, color0_paper, mask = color0mask)
    color1parts = cv2.bitwise_or(color1_paper, color1_paper, mask = color1mask)
    color2parts = cv2.bitwise_or(color2_paper, color2_paper, mask = color2mask)
    color3parts = cv2.bitwise_or(color3_paper, color3_paper, mask = color3mask)
    color4parts = cv2.bitwise_or(color4_paper, color4_paper, mask = color4mask)
    color5parts = cv2.bitwise_or(color5_paper, color5_paper, mask = color5mask)
    color6parts = cv2.bitwise_or(color6_paper, color6_paper, mask = color6mask)
    color7parts = cv2.bitwise_or(color7_paper, color7_paper, mask = color7mask)
    color8parts = cv2.bitwise_or(color8_paper, color8_paper, mask = color8mask)
    
    #defines what the new image will be by adding different color parts using variables and bitwise
    #because bitwise can only add 2 items together at a time
    temp_img1 = cv2.bitwise_or(color0parts, color1parts)
    temp_img2 = cv2.bitwise_or(temp_img1, color2parts)
    temp_img3 = cv2.bitwise_or(temp_img2, color3parts)
    temp_img4 = cv2.bitwise_or(temp_img3, color4parts)
    temp_img5 = cv2.bitwise_or(temp_img4, color5parts)
    temp_img6 = cv2.bitwise_or(temp_img5, color6parts)
    temp_img7 = cv2.bitwise_or(temp_img6, color7parts)
    custom_img = cv2.bitwise_or(temp_img7, color8parts)
    
    #displays custom image
    cv2.imshow('Customized Image', custom_img)
    
   #updates images consistently
    keypressed = cv2.waitKey(1)
    #allows user to view image until they either save or escape the images by pressing either s for save of esc to close
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.destroyAllWindows()
    
    #prompts user to input chosen name of custom image
    custom_image = raw_input("Enter a file name for the custom image, including the extension, and then press 'enter': ")
    cv2.imwrite(custom_image, custom_img)
    
    #defines variables of saving color combos of each color by BGR values given by the trackbar positions
    SavTxt0 = str(color0_B)+" "+str(color0_G)+" "+str(color0_R)+" \n"
    SavTxt1 = str(color1_B)+" "+str(color1_G)+" "+str(color1_R)+" \n"
    SavTxt2 = str(color2_B)+" "+str(color2_G)+" "+str(color2_R)+" \n"
    SavTxt3 = str(color3_B)+" "+str(color3_G)+" "+str(color3_R)+" \n"
    SavTxt4 = str(color4_B)+" "+str(color4_G)+" "+str(color4_R)+" \n"
    SavTxt5 = str(color5_B)+" "+str(color5_G)+" "+str(color5_R)+" \n"
    SavTxt6 = str(color6_B)+" "+str(color6_G)+" "+str(color6_R)+" \n"
    SavTxt7 = str(color7_B)+" "+str(color7_G)+" "+str(color7_R)+" \n"
    SavTxt8 = str(color8_B)+" "+str(color8_G)+" "+str(color8_R)+" \n"
    
    #in the saved text file writes lines for each variable above
    ColorC.write(SavTxt0)
    ColorC.write(SavTxt1)
    ColorC.write(SavTxt2)
    ColorC.write(SavTxt3)
    ColorC.write(SavTxt4)
    ColorC.write(SavTxt5)
    ColorC.write(SavTxt6)
    ColorC.write(SavTxt7)
    ColorC.write(SavTxt8)
    
    #in the saved text file writes values for each grayscale break then closes text file
    ColorC.write(str(gs_break1)+" \n")
    ColorC.write(str(gs_break2)+" \n")
    ColorC.write(str(gs_break3)+" \n")
    ColorC.write(str(gs_break4)+" \n")
    ColorC.write(str(gs_break5)+" \n")
    ColorC.write(str(gs_break6)+" \n")
    ColorC.write(str(gs_break7)+" \n")
    ColorC.close()