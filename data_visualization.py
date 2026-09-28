import matplotlib.pyplot as plt
import numpy as np # faster than python lists

# x=[2023, 2024, 2025, 2026]
# y=[15,20,19,40]

x=np.array([2023, 2024, 2025, 2026])
y=np.array([15,20,19,40])

plt.plot(x,y, marker="*", ms=20, markerfacecolor="blue", markeredgecolor="red", 
        linestyle="dashdot", width=2) 
plt.show()


