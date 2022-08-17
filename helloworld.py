
# %%
print('Hello World!')


# %%
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
y = np.sin(t)

plt.figure()
plt.plot(t, y)
plt.show()
