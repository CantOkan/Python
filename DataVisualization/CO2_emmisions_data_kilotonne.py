import pandas as pd
from matplotlib import pyplot

data=pd.read_csv('UN_CO2_emmisions_data_kilotonne.csv')



print(data["Austria"].mean())
#mean value of Austria

print(len(set(data.Year)))

y=data.Year==2014

print(data["Austria"].tail(10))
print(data[y]["Austria"])

pyplot.title("CO2_emmisions_data_kilotonne")
pyplot.hist(data["Austria"].tail(10),bins='auto',range=(60000,80000),edgecolor='red')
pyplot.show()
