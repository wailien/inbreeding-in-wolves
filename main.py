import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

df = pd.read_csv('data.csv')

x = df['inbreeding.coefficient']
y = df['pups']

# correlation coefficients
print('Pearson\'s correlation coefficient (r) =', st.pearsonr(x, y).statistic, '\nTwo-tailed p-value =', st.pearsonr(x, y).pvalue)
# Pearson correlation coefficient (r) = -0.6 - Moderate negative correlation
# p-value = 0.0016330410641975481 -> since p-value is less than .05, we conclude that
# there is a statistically significant association between the two variables.
# print('Spearman\'s rho:', x.corr(y, method='spearman'))
# print('Kendall\'s tau: ', x.corr(y, method='kendall'))

x_ticks = [i for i in range(len(x))]

plt.rcParams["figure.figsize"] = (len(x) / 1.7, max(y) / 1.7)
plot = plt.subplot()

plot.bar(x_ticks, y)  #plt.plot()
plot.set_xticks(x_ticks, x)

plot.set_title('inbreeding in wolves')
plot.set_xlabel('inbreeding coefficient')
plot.set_ylabel('pups')

plt.show()