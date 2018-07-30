from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
import SimpleITK as sitk
import os
import re 




label_array=np.zeros((135,640,640))
filename= "Z:\\liver_MRI\\Gad Surgical\\239\\239_Mask_T4_a.mha"
im=sitk.ReadImage(filename)
im_array = sitk.GetArrayFromImage(im)
for i,v in enumerate(im_array):
    label_array[i+38] = label_array[i+38]+im_array[i]
i1=0
j1=0
k1=0
while i1 < len(label_array[0]):
    while j1 < len(label_array[1]):
        while k1 < len(label_array[2]):
            if label_array[i1][j1][k1]==510:
                label_array[i1][j1][k1]=255
            k1=k1+1
        j1=j1+1
    i1=i1+1
print('done')
filename= "Z:\\liver_MRI\\Gad Surgical\\239\\239_Mask_T4_b.mha"
im=sitk.ReadImage(filename)
im_array = sitk.GetArrayFromImage(im)
for i,v in enumerate(im_array):
    label_array[i+93] = label_array[i+93]+im_array[i]
i1=0
j1=0
k1=0
while i1 < len(label_array[0]):
    while j1 < len(label_array[1]):
        while k1 < len(label_array[2]):
            if label_array[i1][j1][k1]==510:
                label_array[i1][j1][k1]=255
            k1=k1+1
        j1=j1+1
    i1=i1+1
print('done')
filename= "Z:\\liver_MRI\\Gad Surgical\\239\\239_Mask_T8.mha"
im=sitk.ReadImage(filename)
im_array = sitk.GetArrayFromImage(im)
for i,v in enumerate(im_array):
    label_array[i+73] = label_array[i+73]+im_array[i]
i1=0
j1=0
k1=0
while i1 < len(label_array[0]):
    while j1 < len(label_array[1]):
        while k1 < len(label_array[2]):
            if label_array[i1][j1][k1]==510:
                label_array[i1][j1][k1]=255
            k1=k1+1
        j1=j1+1
    i1=i1+1
print('done')
img=sitk.GetImageFromArray(label_array)
OUTFN="Z:\\liver_MRI\\Gad Surgical\\239\\fixed239label.mha"
#        ,mhasplitfinal[ind][0]
print('saving...')
sitk.WriteImage(img,OUTFN)
