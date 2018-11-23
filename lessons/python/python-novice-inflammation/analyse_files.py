import matplotlib.pyplot as plt
import numpy as np
import os

# Detect problems with a dataset
def detect_problems(data):
    # Test for suspicious maxima
    if np.max(data, axis=0)[0] == 0 and np.max(data, axis=0)[20] == 20:
        print("Suspicious-looking maxima!")
    elif np.sum(data.min(axis=0)) == 0:
        print("Minima sum to zero!")
    else:
        print("Seems OK!")


# Plot dataset
def plot_data(data, fname):
    # Create figure
    fig = plt.figure(figsize=(10.0, 3.0))
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    # Decorate axes
    axes1.set_ylabel('average')
    axes2.set_ylabel('maximum')
    axes3.set_ylabel('minimum')

    # Plot data
    axes1.plot(data.mean(axis=0))
    axes2.plot(data.max(axis=0))
    axes3.plot(data.min(axis=0))

    # Tidy plot and write file
    fig.tight_layout()
    print("Writing image to:", imgname)
    plt.savefig(imgname)


# Get a list of data files
files = []
for fname in os.listdir('data'):
    if ('inflammation' in fname) and ('.csv' in fname):
        files.append(os.path.join('data', fname))
print("inflammation data files:", files)

# Loop over files and analyse each file
for fname in files:
    print("Analysing:", fname)

    # load data
    data = np.loadtxt(fname, delimiter=",")

    # Detect problems
    detect_problems(data)

    # Plot data
    imgname = fname[:-4] + '.png'
    plot_data(data, imgname)

