import matplotlib.pyplot
import numpy

# Load inflammation data
data = numpy.loadtxt(fname="data/inflammation-01.csv", 
delimiter=",")

# Create figure
fig = matplotlib.pyplot.figure(figsize=(3.0, 10.0))
 
# Add subplots for summaries
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

# Add plot labels
axes1.set_ylabel("average")
axes2.set_ylabel("max")
axes3.set_ylabel("min")

# Plot data
axes1.plot(data.mean(axis=0))
axes2.plot(data.max(axis=0))
axes3.plot(data.min(axis=0))

# Tidy plot
fig.tight_layout()

# Show plot
matplotlib.pyplot.show()
