#numpy
import numpy as np

brokered_by,price,acre_lot,city,house_size=np.genfromtxt('RealEstate-USA.csv',delimiter=',',usecols=(0,4,5,8,9),unpack=True,dtype=None,skip_header=1)

print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

#statics operations on price
print("RealEstate-USA.csv mean:", np.mean(price))
print("RealEstate-USA.csv average:", np.average(price))
print("RealEstate-USA.csv std:", np.std(price))
print("RealEstate-USA.csv mod:", np.median(price))
print("RealEstate-USA.csv percentile - 50:", np.percentile(price,50))
print("RealEstate-USA.csv min:", np.min(price))
print("RealEstate-USA.csv max:", np.max(price))

#statics price on house_size
print("RealEstate-USA.csv mean:", np.mean(house_size))
print("RealEstate-USA.csv average:", np.average(house_size))
print("RealEstate-USA.csv std:", np.std(house_size))
print("RealEstate-USA.csv mod:", np.median(house_size))
print("RealEstate-USA.csv percentile - 50:", np.percentile(house_size,50))
print("RealEstate-USA.csv min:", np.min(house_size))
print("RealEstate-USA.csv max:", np.max(house_size))

#maths opeartions on arrays
addition= price+house_size
subtraction= price-house_size
multiplication=price*house_size
division=price/house_size

print("RealEstate-USA.csv price-house_size-adition", addition)
print("RealEstate-USA.csv price-house_size-subtration", subtraction)
print("RealEstate-USA.csv price-house_size-multiplication", multiplication)
print("RealEstate-USA.csv price-house_size-division", division)

#2 dimentional arrary
D2_array = np.array([price,house_size])
print ("RealEstate-USA price plus house_size - 2 dimentional arrary - " ,D2_array)

#3 dimentional array
D3_array= np.array([[house_size,acre_lot]])
print ("RealEstate-USA price plus house_size - 3 dimentional arrary - " ,D3_array)

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
pricePie = (price/np.pi)+1
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)
print(sine_values)
print(cosine_values)
print(tangent_values)

sinh_values = np.sinh(pricePie)
print(sinh_values)
cosh_values = np.cosh(pricePie)
print(cosh_values)
tanh_values = np.tanh(pricePie)
print(tanh_values)