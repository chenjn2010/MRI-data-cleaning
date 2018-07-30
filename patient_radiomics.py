# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 13:28:54 2018

@author: JChen
"""
import SimpleITK as sitk
import numpy as np
import os
import csv
from radiomics import featureextractor
import six

class Patient:
    """Hold information at patient level.
    
    Keeps track of image volume and segmentation mask

    Currently extract features from a large segmentation containing all lesions
    
    Attributes:
    -----------
        imageFile: string 
            3D volume image filename
        maskFile: string 
            3D volume containing mask corresponding to image
        patientdict: dictionary
            contains patient level information                
    """
    
    def __init__(self,filename,maskfilename):
        
        """ initialize Patient
        
        Reads in image file and mask file.   
        Identifies a large segmentation containing all lesions in mask file and 
        extractes relevent image data. 
        Patient level meta info is stored in 'patientdict'
        
        Parameters
        -----------
        filename: String 
            containing original image filename - format must be ITK readable
        maskfilename: 
            String containing mask filename - format must be ITK readable
           
        """    
        
        self.filename=str(filename)  #make sure filename is proper string
        self.maskfilename=str(maskfilename)
  
        image=sitk.ReadImage(self.filename)
        mask=sitk.ReadImage(self.maskfilename)
        
        # need to match image information of images and their corresponding masks
        mask=sitk.Cast(mask,sitk.sitkInt8)
        mask.SetSpacing(image.GetSpacing())
        mask.SetOrigin(image.GetOrigin())
        
        # need to save some patient level info to dictinary for lesion tracking       
        self.patientDict={}        
        fName=os.path.basename(self.filename)
        ftxt=(fName.split('.'))[0]
        self.patientDict['_image']=ftxt
        fName=os.path.basename(self.maskfilename)
        ftxt=(fName.split('.'))[0]
        self.patientDict['_segmentation']=ftxt
     
        self.features={}
        self.image=image
        self.mask=mask
            
    def generate_features(self,csvFile):
        """go through each patient lesion and extract features, writing result to a csv file
            
        Parameters
        -----------
            csvFile: string 
                name of csv file created to hold feature information
                
        """
        extractor = featureextractor.RadiomicsFeaturesExtractor()
        a=extractor.settings.values
#        extractor.loadParams("D:\\jc\\pyradiomics\\examples\\exampleSettings\\Original_MR_5mm.yaml")
        extractor.loadParams("D:\\jc\\pyradiomics\\examples\\exampleSettings\\exampleMR_5mm.yaml")
        results = extractor.execute(self.image, self.mask)
        
        pDict={}
        pDict['_orginal_filename']=self.filename
        pDict['_mask_filename']=self.maskfilename
        
        self.features.update(pDict)

        for key, value in six.iteritems(results):
            eDict={}
            eDict[key]=value
            self.features.update(eDict)
        
        csv_file= open(str(csvFile),'a')   
#        for key, value in six.iteritems(result):
#            writer=csv.writer(csv_file)
#            writer.writerow([key,value])
        fieldnames = np.sort(self.features.keys())          
        csvwriter = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
        
        csvwriter.writerow(self.features)            
##        for lesion in self.ax_lesionList:
#        csvwriter.writerow(self.features)
#            
#        csv_file.close()      
#        # extract information about lesions from segmentation mask
#        
#        #first generate a label image - 1 label for each connected region
#        ccomp_filter = sitk.ConnectedComponentImageFilter()
#        component_image = ccomp_filter.Execute(mask)
#        #now use the LabelShapeStatisticsFilter to get no of lesions
#        
#        label_filter = sitk.LabelShapeStatisticsImageFilter()
#        label_filter.Execute(component_image)
#        num_components =  label_filter.GetNumberOfLabels()
#        self.ax_lesionList=[]
