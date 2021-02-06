import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


mu, sigma = 100, 15
x_gaussian = mu + sigma * np.random.randn(10000)
mu, sigma_2 = 100, 5
y = mu + sigma_2 * (np.random.randn(10,10000) ** 2).sum(0)


np.savetxt('file_data.csv', x_gaussian, delimiter=',')
np.savetxt('nongaussian.csv', y, delimiter=',')
