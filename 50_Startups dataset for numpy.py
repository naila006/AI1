#numpy

import numpy as np
Spend,Administration,Marketing_Spend,State,Profit=np.genfromtxt('50_Startups.csv', delimiter=',' ,usecols=(0,1,2,3,4),unpack=True,dtype=None,skip_header=1)

print(Spend)
print(Administration)
print(Marketing_Spend)
print(State)
print(Profit)

#statics operations on Spend
print("50_Startups.csv mean:", np.mean(Spend))
print("50_Startups.csv average:", np.average(Spend))
print("50_Startups.csv std:", np.std(Spend))
print("50_Startups.csv mod:", np.median(Spend))
print("50_Startups.csv percentile - 50:", np.percentile(Spend,50))
print("50_Startups.csv min:", np.min(Spend))
print("50_Startups.csv max:", np.max(Spend))

#statics price on Profit
print("50_Startups.csv mean:", np.mean(Profit))
print("50_Startups.csv average:", np.average(Profit))
print("50_Startups.csv std:", np.std(Profit))
print("50_Startups.csv mod:", np.median(Profit))
print("50_Startups.csv percentile - 50:", np.percentile(Profit,50))
print("50_Startups.csv min:", np.min(Profit))
print("50_Startups.csv max:", np.max(Profit))

#maths opeartions on arrays
addition= Spend+Profit
subtraction= Spend-Profit
multiplication= Spend*Profit
division= Spend/Profit

print("50_Startups.csv Spend-Profit-adition", addition)
print("50_Startups.csv Spend-Profit-subtration", subtraction)
print("50_Startups.csv Spend-Profit-multiplication", multiplication)
print("50_Startups.csv Spend-Profit-division", division)

#2 dimentional arrary
D2_array = np.array([Spend,Profit])
print ("50_Startups Spend plus Profit - 2 dimentional arrary - " ,D2_array)

#3 dimentional array
D3_array= np.array([[Spend,Profit]])
print ("50_Startups Spend plus Profit - 3 dimentional arrary - " ,D3_array)

#using np.nditer()
for item in np.nditer(D2_array):
    print(item)

#using np,ndenumerate()
for index, elem in np.ndenumerate(D2_array):
    print(index, elem) 

#common prperties of array
#ndim
print("ndim",D2_array.ndim)
#shape
print("shape",D2_array.shape)
#size
print("size",D2_array.size)
#dtype
print("dtye",D2_array.dtype)
#itemsize
print("itemsize",D2_array.itemsize)
#nbytes
print("nbytes",D2_array.nbytes)
#tranpose
print("T",D2_array.T)

#slicing array
D2_arraySlice= D2_array[1:3, 2:4]
print(D2_arraySlice)

D2_arraySlice2= D2_array[2:8, 3:5]
print(D2_arraySlice2)

#geometric operations
SpendPie = (Spend/np.pi)+1
sine_values = np.sin(SpendPie)
cosine_values = np.cos(SpendPie)
tangent_values = np.tan(SpendPie)
print(sine_values)
print(cosine_values)
print(tangent_values)

sinh_values = np.sinh(SpendPie)
print(sinh_values)
cosh_values = np.cosh(SpendPie)
print(cosh_values)
tanh_values = np.tanh(SpendPie)
print(tanh_values)