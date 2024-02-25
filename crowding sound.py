import matplotlib.pyplot as plt
from statistics import mean
from scipy import stats

estimate=[10,50,42,56,54,236,484,58,59,54]
y=[]
estimate.sort()
print(estimate)
tv=int(0.1*(len(estimate)))#10% of estimate ke liye
estimate=estimate[tv:]
estimate=estimate[:len(estimate)-tv]
for i in range(len(estimate)):
    y.append(5)
plt.plot(estimate,y,'ro')
print(mean(estimate))
m=stats.trim_mean(estimate,0.1)
print(m)