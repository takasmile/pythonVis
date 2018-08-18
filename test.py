import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# % matplotlib inline
import matplotlib.style as psl

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2010',periods=1000))
ts = ts.cumsum()
ts.plot(kind='line',  #图表类型
        color='r',
        style='-gx',
        alpha=0.5,
        use_index=True,  #是否使用数据中给出的index
        rot=0,    # 旋转刻度标签
        ylim=[-50, 50],
        yticks=list(range(-50, 50,10)),
        title='time series',
        legend=True,
        label='cad')
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'both')  # 网格

plt.show()