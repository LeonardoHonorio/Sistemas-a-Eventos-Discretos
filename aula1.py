import numpy as np
import matplotlib.pyplot as plt

a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]


# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'b--', label='Model length')
ax.plot(a, d, 'r:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')

#legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
#legend.get_frame().set_facecolor('#00FFCC')

plt.show()

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


