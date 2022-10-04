# Property of forMED
# prepared by: Michelle Rivera
# Part 2: Data Analysis
# openCV - computer vision
# cv2 will not appear on download use openCV-python but commands are the same
import os
import os.path
import cv2
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
# import PIL
import numpy as np
# import image
# import imagesize
from PIL import Image
# import matplotlib
from matplotlib import pyplot as plt
# import scipy
from scipy import stats

# folders = []
files = []
b = []
meanK = []

# Not necessary to uncomment this section if you know your folders match in length
'''
trials = int(input("Sets of Trials Being Analyzed: "))
tests = int(input("Test Runs Being Analyzed: "))
input_string = (input("Enter pressure values separated by space: "))
pressures = input_string.split(" ")
for i in range(len(pressures)):
   pressures[i]=int(pressures[i])
print(pressures)
# while the number of values in pressure array does not match tests incorrect
while len(pressures) != tests:
   print("Incorrect Array Length. Please try again.")
   # we run this again so we dont have to break or re-run the code
   input_string = (input("Enter pressure values separated by space: "))
   pressures = input_string.split(" ")
   # make string variables into int
   for i in range(len(pressures)):
       pressures[i] = int(pressures[i])
# temporary print to ensure program is working
print("Length of Pressures match number of Tests")
'''


trials = int(input("How many trials?: "))
filter = int(input("Remove Noise? 1- yes 0-no: "))
# control no light file
print("Please select control file")
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
print("Please select folder for analysis")
path= filedialog.askdirectory()
print(path)
print(isinstance(path, str))
# assert folder is path
# currently this is working for one folder
# 9/20 appending to read from a bigger file
# 9/20 making an empty array to store results of each file
for folder in os.scandir(path):
    if folder.is_dir():
        sub_folder = folder.path
        print(sub_folder)
        print(folder.name)
        for file in os.listdir(sub_folder):
            if os.path.isfile(os.path.join(sub_folder, file)):
                address = sub_folder + '/' + file
                print(address)
                dataset = Image.open(address)
                h, w = np.shape(dataset)
                contarray = np.zeros((h, w, dataset.n_frames))
                for i in range(dataset.n_frames):
                    dataset.seek(i)
                    contarray[:, :, i] = np.array(dataset)
                expim = contarray.astype(np.double)
                # print(expim)
                # maybe i will include the subtraction within this loop for convenience
            if filter == 1:
                # print(expim)
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
# necessary for reshaping
meanK_array = np.array(meanK)
# later edit to .reshape(trials, pressures)
meanK_values = meanK_array.reshape(trials, 5)
print(meanK_values)
# standard error
standard_error = np.std(meanK_values, axis=0) / np.sqrt(np.size(meanK_values, axis=0))
# avg meanK
avg_meanK_values = np.mean(meanK_values, axis=0)


# graphing
# 9/28/2022
xaxis = [10, 15, 20, 25, 35]
plt.plot(xaxis, avg_meanK_values, 'ro', label= 'Average MeanK')
fitted_graph = np.polyfit(xaxis, avg_meanK_values, 2)
plt.plot(xaxis, np.polyval(fitted_graph, xaxis), color='blue', label='polyfit')
plt.errorbar(xaxis, avg_meanK_values, yerr=standard_error, color="orange", label='Standard Error')
plt.legend()
# r2 value
slope, intercept, r_value, p_value, std_err = stats.linregress(xaxis, avg_meanK_values)
r_squared = r_value**2
print(r_squared)
# plotting
plt.legend()
plt.text(13, 1, r_squared, horizontalalignment='right')
plt.show()






