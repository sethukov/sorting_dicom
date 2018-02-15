# Code by Sethu K. Boopathy Jegathambal
# Sort the dicom files based on the series info
# Creates a folder in the current path and copies the image into the folder

import dicom
import os,sys, numpy
import shutil

try:
	from pythonzenity import FileSelection	
	DicomPath=FileSelection(directory=True)		
except:
	DicomPath = raw_input("Enter directory path: ")

LstDicomFiles=[]

for file in os.listdir(str(DicomPath)):
	LstDicomFiles.append(file)

series=[]
for item in LstDicomFiles:
	ds=dicom.read_file(os.path.join(DicomPath,item))
	if ds.SeriesNumber not in series:
		series.append(ds.SeriesNumber)
		os.mkdir(str('./'+str(ds.SeriesNumber)))
		shutil.copyfile(os.path.join(DicomPath,item), str('./'+str(ds.SeriesNumber)+'/'+str(item)))
	else:
		shutil.copyfile(os.path.join(DicomPath,item), str('./'+str(ds.SeriesNumber)+'/'+str(item)))

print("Number of series sorted: "+str(len(series)))
print("Done sorting :)")









