import pandas as pd

from matplotlib import pyplot as plt

data=pd.read_csv('KaggleCSV/LifeExpectancyData.csv')

tr=data['Country']=="Turkey"

print(data[tr])

plt.plot(data[tr].Year,data[tr].Schooling)
plt.title("Turkey")
plt.show()
