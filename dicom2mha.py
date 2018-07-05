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

outputfile	= "Z:\liver_MRI\Gad Surgical\inventory2.txt"	# file to save the results to
inputfile	= "Z:\liver_MRI\Gad Surgical\cleaninventory.txt"	# file to save the results to
folder		= "Z:\liver_MRI\Gad Surgical"	 # the folder to inventory



origin_name_file = "Z:\liver_MRI\Gad Surgical\originnames.txt"
#originnames = [(j[0] + '\\' + j[0] + "_Original") for j in origins]
#with open(origin_name_file, 'w') as ofile:
#    for i in originnames:
#        ofile.write(i+'\n')
#################################read lines from txt
with open(inputfile) as f:
    lines = [line.rstrip('\n') for line in f]

with open(origin_name_file) as ofile:
    originnames = [originn for originn in ofile]    
    
for index,names in enumerate(lines):

    if index >= 158:
        data_directory = folder+"\\"+lines[index]
        print (index,names,data_directory)
        series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(data_directory)
        if not series_IDs:
            print("ERROR: given directory \""+data_directory+"\" does not contain a DICOM series.")
            for filename in os.listdir(data_directory):
                filepath=os.path.join(data_directory,filename)
                print("checking:"+filepath)
                data_directory = filepath
                series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(data_directory)
# Get the list of files belonging to a specific series ID.
        reader = sitk.ImageSeriesReader()
# Use the functional interface to read the image series.
        series_file_names = reader.GetGDCMSeriesFileNames(data_directory, series_IDs[0])
        reader.SetFileNames(series_file_names)
        reader.MetaDataDictionaryArrayUpdateOn()
        reader.LoadPrivateTagsOn()
        image3D = reader.Execute()
# Write the image.
        output_file_name_3D = os.path.join("Z:\liver_MRI\Gad Surgical",lines[index]+ '.mha')
        sitk.WriteImage(image3D, output_file_name_3D)

# Read it back again.
        written_image = sitk.ReadImage(output_file_name_3D)

# Check that the original and written image are the same.
        statistics_image_filter = sitk.StatisticsImageFilter()
        statistics_image_filter.Execute(image3D - written_image)

# Check that the original and written files are the same
        print('Max, Min differences are : {0}, {1}'.format(statistics_image_filter.GetMaximum(), statistics_image_filter.GetMinimum()))

#################################save filename to txt
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
#data_directory = folder+"\\"+lines[0]
#series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(data_directory)
#if not series_IDs:
#    print("ERROR: given directory \""+data_directory+"\" does not contain a DICOM series.")
#
## Get the list of files belonging to a specific series ID.
#reader = sitk.ImageSeriesReader()
## Use the functional interface to read the image series.
#series_file_names = reader.GetGDCMSeriesFileNames(data_directory, series_IDs[0])
#reader.SetFileNames(series_file_names)
#reader.MetaDataDictionaryArrayUpdateOn()
#reader.LoadPrivateTagsOn()
#image3D = reader.Execute()
## Write the image.
#output_file_name_3D = os.path.join(data_directory, '3DImage.mha')
#sitk.WriteImage(image3D, output_file_name_3D)
#
## Read it back again.
#written_image = sitk.ReadImage(output_file_name_3D)
#
## Check that the original and written image are the same.
#statistics_image_filter = sitk.StatisticsImageFilter()
#statistics_image_filter.Execute(image3D - written_image)
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
