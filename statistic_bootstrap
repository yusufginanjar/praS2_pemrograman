import random
# create graph of mean bootstrap samples
import matplotlib.pyplot as plt
import numpy as np

array = [165,160,155,170,163,175,154,158,160,163,161,172,170,156,152,167,171,166]


# bootstrap statistics
def bootstrap(data, n=1000):
    # n is the number of bootstrap samples to take
    # data is the data to sample from
    # returns a list of bootstrap samples
    # each sample is a list of n random values from data
    samples = []
    for i in range(n):
        sample = []
        for j in range(len(data)):
            sample.append(random.choice(data))
        samples.append(sample)
    return samples

def graph(data, n=1000):
    samples = bootstrap(data, n)
    means = []
    for sample in samples:
        means.append(np.mean(sample))
    plt.hist(means, bins=20)
    plt.show()

graph(bootstrap(array))

# calculate mean bootstrap confidence interval 95% of the time
def mean_confidence_interval(data, n=1000):
    samples = bootstrap(data, n)
    means = []
    for sample in samples:
        means.append(np.mean(sample))
    mean = np.mean(means)
    std = np.std(means)/np.sqrt(n)
    return mean - std*1.96, mean + std*1.96

mean_confidence_interval(bootstrap(array))

# calculate confidence interval 95% of the time
def confidence_interval(data, n=1000):
    samples = bootstrap(data, n)
    means = []
    for sample in samples:
        means.append(np.mean(sample))
    means.sort()
    return means[int(n*0.025)], means[int(n*0.975)]

confidence_interval()
