from matplotlib.pyplot import show
import seaborn as sns
import numpy as np
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt

#norm = [float(i)/max(ar2) for i in ar2]
#print(norm)

ar1 = input("Array para T1:\n")
#ar2 = input("Array para T2:\n")
#ar3 = input("Array para T3:\n")
#ar4 = input("Array para T4:\n")


# seaborn histogram

sns.distplot(ar1, hist=True, kde=False, bins=len(ar1)/2, color = 'blue', hist_kws={'edgecolor':'black'})
# Add labels
plt.title('Agrupamento amostral por segundo')
plt.ylabel('Frequencia')
plt.xlabel('Tempo')
plt.grid(True)

#plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

plt.show()

n, bins, patches = plt.hist(ar1, bins=int(len(ar1)/4), color='green', alpha=0.5)
#n, bins, patches = plt.hist(queue_wait_time_list, 10, density=True)

plt.title('Agrupamento amostral por segundo')
plt.ylabel('Frequencia')
plt.xlabel('Tempo')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(0, 600)
#plt.ylim(0, 0.003)
plt.legend()
plt.grid(True)

#plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

