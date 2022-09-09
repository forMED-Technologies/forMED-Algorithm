#Part 2: Data Analysis
#openCV - computer vision
#cv2 will not appear on download use openCV-python but commands are the same
import os
import os.path
import cv2
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
#prompt for the use of numpy and image libraries
#these extensions have to be downloaded: view > tool window > python packages
import PIL
import numpy as np
import image
import imagesize
from PIL import Image
import matplotlib
from matplotlib import pyplot as plt
import scipy
from scipy import stats

# folders = []
files = []
b = []
meanK = []
filter = int(input(("Remove Noise? 1- yes 0-no: ")))

'''
#open analysis folder
analysis_folder = filedialog.askdirectory()
print(analysis_folder)
for folder in os.listdir(analysis_folder):
    if os.analysis_folder.isdir(os.analysis_folder.join(path, folder)):
        print(folder)
'''

# control_nolight file
control_file = filedialog.askopenfilenames()
for i in range(len(control_file)):
    control_dataset = Image.open(control_file[i])
    h, w = np.shape(control_dataset)
    contarray = np.zeros((h, w, control_dataset.n_frames))
    for i in range(control_dataset.n_frames):
        control_dataset.seek(i)
        contarray[:, :, i] = np.array(control_dataset)
    # 3d array: used for the subtraction
    expim1 = contarray.astype(np.double)


# start of folder reading
path= filedialog.askdirectory()
print(path)
print(isinstance(path, str))
# assert folder is path
# currently this is working for one folder
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
       # yield file
        # print(path)
        # print(file)
        address = path + '/'+file
        print(address)
        dataset = Image.open(address)
        h, w = np.shape(dataset)
        contarray = np.zeros((h, w, dataset.n_frames))
        for i in range(dataset.n_frames):
            dataset.seek(i)
            contarray[:, :, i] = np.array(dataset)
        expim = contarray.astype(np.double)
        #print(expim)
# maybe i will include the subtraction within this loop for convenience
    if filter == 1:
        print(expim)
        filter_1 = np.subtract(expim, expim1)
        # print(filter_1)
        flat_filter = filter_1.flatten(order='C')
        meanK_formula = np.std(flat_filter) / np.mean(flat_filter)
        meanK.append(meanK_formula)
        print("noise filtered")
    else:
        print("No noise filtering")
        meanK_formula = np.std(b) / np.mean(b)
        # print(meanK_formula)
        meanK.append(meanK_formula)
print(meanK)

# files = files + list(file.split(" "))
# print(files)

# graphing
xaxis = [10, 15, 20, 25, 35]

# for i in range(len(xaxis)):
   # for i in range(len(meanK)):
plt.plot(xaxis, meanK, 'ro', label= 'Average MeanK')
fitted_graph = np.polyfit(xaxis, meanK, 2)
plt.plot(xaxis, np.polyval(fitted_graph, xaxis), color = 'blue', label = 'polyfit') # mark w x
#r2 value
slope, intercept, r_value, p_value, std_err = stats.linregress(xaxis, meanK)
r_squared = r_value**2
print(r_squared)
# plotting
plt.legend()
plt.text(13, 0.25, r_squared, horizontalalignment = 'right')
plt.show()


'''
#start of code
#user inputs
trials = int(input("Sets of Trials Being Analyzed: "))
tests = int(input("Test Runs Being Analyzed: "))


#user input array for pressures
#might be cleaner to makes lines 12-17 a def
input_string = (input("Enter pressure values separated by space: "))
pressures = input_string.split(" ")
#make string variables into int
for i in range(len(pressures)):
    pressures[i]=int(pressures[i])
print(pressures)

#while the number of values in pressure array does not match tests incorrect
while len(pressures) != tests:
    print("Incorrect Array Length. Please try again.")
    # we run this again so we dont have to break or re-run the code
    input_string = (input("Enter pressure values separated by space: "))
    pressures = input_string.split(" ")
    # make string variables into int
    for i in range(len(pressures)):
        pressures[i] = int(pressures[i])
#temporary print to ensure program is working
print("Length of Pressures match number of Tests")


# values needed to be stored
import ipdb
# ipdb.set_trace()
meanK = []
# open directory
filter_noise = 1
testing_files = []

control_file = filedialog.askopenfilenames()
for i in range(len(control_file)):
    control_dataset = Image.open(control_file[i])
    h, w = np.shape(control_dataset)
    contarray = np.zeros((h, w, control_dataset.n_frames))
    for i in range(control_dataset.n_frames):
        control_dataset.seek(i)
        contarray[:, :, i] = np.array(control_dataset)
    # 3d array: used for the subtraction
    expim1 = contarray.astype(np.double)

    # prints the pixels and the number of slices
    # print(expim1.shape)
    # convert to 1d array for each
    # no_light = expim1.flatten(order='C')
    # print so we can check
    # print(no_light)

while filter_noise == 1:
    selected_files = filedialog.askopenfilenames()
    testing_files = testing_files + list(selected_files)
    filter_noise = int(input("Enter 1 to input enter 0 to continue: "))

# now that we have the files and their respective directory find a way to iterate through them
# step one just see if you can read them: accomplished
# step two see if you can extract the data: accomplished
# step three meanK values for more than one file: accomplished

filter_process = int(input("To subtract control (1) to not (0): "))

for i in range(len(testing_files)):
    print(testing_files[i])
    dataset = Image.open(testing_files[i])
    # do the 3d array for each
    h, w = np.shape(dataset)
    tiffarray = np.zeros((h, w, dataset.n_frames))
    for i in range(dataset.n_frames):
            dataset.seek(i)
            tiffarray[:, :, i] = np.array(dataset)
    # 3d array
    expim = tiffarray.astype(np.double)
    # prints the pixels and the number of slices
    print(expim.shape)
    # convert to 1d array for each
    b = expim.flatten(order='C')
    # print so we can check
    print(b)
    # subtract the control no light from the other selected files: if filtering for noise
    if filter_process == 1:
        filter_1 = np.subtract(expim, expim1)
        # print(filter_1)
        flat_filter = filter_1.flatten(order = 'C')
        meanK_formula = np.std(flat_filter)/np.mean(flat_filter)
        meanK.append(meanK_formula)
    else:
        meanK_formula = np.std(b) / np.mean(b)
        # print(meanK_formula)
        meanK.append(meanK_formula)

print(meanK)

# part 3
# graphing
xaxis = [10, 15, 20, 25, 35]

# for i in range(len(xaxis)):
   # for i in range(len(meanK)):
plt.plot(xaxis, meanK, 'ro', label= 'Average MeanK')
fitted_graph = np.polyfit(xaxis, meanK, 2)
plt.plot(xaxis, np.polyval(fitted_graph, xaxis), color = 'blue', label = 'polyfit') # mark w x
#r2 value
slope, intercept, r_value, p_value, std_err = stats.linregress(xaxis, meanK)
r_squared = r_value**2
print(r_squared)
# plotting
plt.legend()
plt.text(13, 0.25, r_squared, horizontalalignment = 'right')
plt.show()
'''