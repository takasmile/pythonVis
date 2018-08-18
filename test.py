import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# % matplotlib inline
import matplotlib.style as psl


df = pd.DataFrame(np.random.randn(1000, 3), index = pd.date_range('1/1/2010',periods=1000), columns=['alex', 'tina', 'monica'])
df = df.cumsum()
df.plot(style='--.',
        alpha=0.8,
        ylim=[-100,100],
        figsize=(10,8),
        grid=True,
        yticks=list(range(-100, 125,25)),
        title='text',
        subplots=True,   #是否将每个系列分成不同的子图
        )
plt.grid(True, linestyle='--', axis='both')
print(list('abcd'))
plt.show()