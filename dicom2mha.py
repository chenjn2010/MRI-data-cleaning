# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:20:17 2018

@author: Jianan
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
import SimpleITK as sitk
import os

outputfile	= "Z:\inventory2.txt"	# file to save the results to
folder		= "Z:\"	 # the folder to inventory
###########################################detect filename
#dirf = os.getcwd()
#subdir = os.listdir(folder)
#with open(outputfile, "w") as txtfile:
#    for i in subdir:
#        if os.path.isdir(folder+"\\"+i):
#            subsubdir=os.listdir(folder+"\\"+i)
#            for j in subsubdir:
#                print(i,j)
#                txtfile.write("%s\\%s\n" % (i,j))

## start editable vars #
#outputfile	= "D:\jc\inventory.txt"	# file to save the results to
#folder		= "D:\jc\liverMRI"	 # the folder to inventory
#exclude		= ['Thumbs.db','.tmp']	# exclude files containing these strings
#pathsep		= "\"			# path seperator ('/' for linux, '\' for Windows)
## end editable vars #
#
#with open(outputfile, "w") as txtfile:
#	for path,dirs,files in os.walk(folder):
#		sep = "\n---------- " + path.split(pathsep)[len(path.split(pathsep))-1] + " ----------"
#		print(sep)
#		txtfile.write("%s\n" % sep)
#
#		for fn in sorted(files):
#			if not any(x in fn for x in exclude):
#				filename = os.path.splitext(fn)[0]
#				
#				print(filename)
#				txtfile.write("%s\n" % filename)
#
#txtfile.close()




#data_directory = os.path.dirname(fdata("CIRS057A_MR_CT_DICOM/readme.txt"))
#series_ID = '1.2.840.113619.2.290.3.3233817346.783.1399004564.515'
#
## Get the list of files belonging to a specific series ID.
#reader = sitk.ImageSeriesReader()
## Use the functional interface to read the image series.
#original_image = sitk.ReadImage(reader.GetGDCMSeriesFileNames(data_directory, series_ID))
#
## Write the image.
#output_file_name_3D = os.path.join(data_directory, '3DImage.mha')
#sitk.WriteImage(original_image, output_file_name_3D)
#
## Read it back again.
#written_image = sitk.ReadImage(output_file_name_3D)
#
## Check that the original and written image are the same.
#statistics_image_filter = sitk.StatisticsImageFilter()
#statistics_image_filter.Execute(original_image - written_image)
#
## Check that the original and written files are the same
#print('Max, Min differences are : {0}, {1}'.format(statistics_image_filter.GetMaximum(), statistics_image_filter.GetMinimum()))








###################################### BUILD 3D ANNOTATIONS
#IMAGE_DIR = 'Z:\liver_MRI\Gad Surgical'
#
#def readmha(mid):
#    filename = os.path.join(IMAGE_DIR,str(mid),str(mid)+"_origin.mha")
#    im = sitk.ReadImage(str(filename))
#    im_array = sitk.GetArrayFromImage(im)
#
#
#    filenamemask = os.path.join(IMAGE_DIR,"5",str(mid)+"_mask_T4.mha")
#    imask = sitk.ReadImage(str(filenamemask))
#    mask_array = sitk.GetArrayFromImage(imask)
#    return im_array, mask_array
#
#im_array, mask_array = readmha(5)
#
#
#midlower=83
#midupper=86
#totalnum=136
#xfront = np.zeros(shape=(midlower-1,384,384))
#xend = np.zeros(shape=(totalnum-midupper,384,384))
#i=0
#newmha = np.concatenate((xfront,mask_array,xend),axis=0)
##newmha = np.transpose(newmha,(0,1,2))
#OUTPUT_DIR = 'D:\jc'
#img = sitk.GetImageFromArray(newmha)
#output_file_name_3D = os.path.join(OUTPUT_DIR, '5_label.mha')
#sitk.WriteImage(img,output_file_name_3D)
