import pandas as pd
import numpy as np
import sys
df=pd.read_csv("C:/Users/gjc10/Downloads/StationDetails.csv")
df=df.drop(df[df['close year']!='(null)'].index)
def Find_Closest(lat,long):
    distances=[]

    for i in df.index:
        distance=111*np.sqrt((lat-df['latitude'][i])**2+(long-df['longitude'][i])**2)
        distances.append((i,distance))
        min_index=np.argmin([x[1] for x in distances])
    
    return df.name[distances[min_index][0]],distances[min_index][1]
#x=input('Enter lat,long')
lat=float(sys.argv[1])
lon=float(sys.argv[2])
#print(x)
#splitdata=x.split(', ')
#print(splitdata)
#print(Find_Closest(float(splitdata[0]),float(splitdata[1])))
print(Find_Closest(lat,lon))