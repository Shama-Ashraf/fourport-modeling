from snippets import fourportdata
from matplotlib import pyplot as plt
I,V=fourportdata()
# plt.scatter(I,V)
# plt.xlabel('Input, I / Amps')
# plt.ylabel('Output, V/ Volts')
# plt.title('Unknown fourport')


import numpy as np
from sklearn.linear_model import LinearRegression
x=I.reshape(-1,1) #Scikit-learn expects the input X to be 2-D, so we reshape I:
y=V
lrmodel = LinearRegression(fit_intercept = False)
model=lrmodel.fit(x,y)

x=np.linspace(0,5).reshape(-1,1)
y=model.predict(x)

plt.scatter(I,V)
plt.plot(x,y, color='red')
plt.xlabel('Input, I / Amps')
plt.ylabel('Output, V/ Volts')
plt.title('Unknown fourport')
plt.show()
  