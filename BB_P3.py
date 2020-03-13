import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline

def intensity(wavelength, T):
  a=(2*_h*(_c**2))/(wavelength**5)
  b = (_h*_c)/(wavelength*_k*T)
  c=(np.exp(b)-1)**-1
  return a*c
  
def calculate_rms(measured_lambda_metres, measured_intensity, T):
  model_intensity=intensity(measured_lambda_metres, T)
  sq_dev=(measured_intensity-model_intensity)**2
  mean_sum=sum(sq_dev)/len(sq_dev)
  return mean_sum**0.5
  

# Constants
_h=6.626E-34
_c=2.998E8
_k=1.381E-23

measured_lambda=np.array([4.405286344,3.676470588,3.144654088,\
2.754820937,2.450980392,2.004008016,1.834862385,1.377410468,\
0.881834215,0.468823254],float)

# Measured data: intensity in W m**-2 m**-1 sr**-1
measured_intensity=np.array([3.10085E-05,5.53419E-05,8.8836E-05,\
0.000129483,0.000176707,0.000284786,0.00034148,0.000531378,\
0.000561909,6.16936E-05],float)

measured_lambda_metres=measured_lambda*1e-3



# Define the wavelength range in millimetres
model_lambda_range=np.linspace(0.1,5.0,50,endpoint=True)
# convert to metres
model_lambda_range_metres=model_lambda_range*1e-3

temp=float(input("Please enter a value for T"))
errors=[]
temps=[]


while True:
  model_intensity=intensity(model_lambda_range_metres,temp)
  rms=calculate_rms(measured_lambda_metres, measured_intensity, temp)
  errors.append(rms)
  temps.append(temp)
  model_intensity=intensity(model_lambda_range_metres, temp)
  print(f"Error is {rms}")
  print(f"Smallest error is {min(errors)} for a temperature of {temps[errors.index(min(errors))]}")
  plt.clf()
  plt.title("Intensity against wavelength")
  plt.xlabel("wavelength /mm")
  plt.ylabel("Intensity /it's complicated")#doesn't work properly in trinket P2
  plt.plot(measured_lambda,measured_intensity, label="Observed")
  plt.plot(model_lambda_range,model_intensity, label="Model: T= "+ str(temp))
  plt.legend()
  plt.show()
  temp=input("Enter another temperature or type q to finish")
  if temp=="q":
    break
  else:
    temp=float(temp)
    
# Implements a 'brute force' algorithm for finding the temp that gives a minimum error.
# Works on this fairly small range but not really satisfactory. NB using mupy arrays gives
# a much faster speed than standard python lists but it still slows down pretty rapidly
# once we use any more than accracy or range we have here.
    
temp_range=np.linspace(1,5,10000,endpoint=True)
error_array=np.array([])
    
for temperature in temp_range:
  t=calculate_rms(measured_lambda_metres, measured_intensity, temperature)
  error_array=np.append(error_array,t)
  
plt.clf()
plt.subplot(211)
plt.title("Likelihood / Error plotted against temperature")
plt.plot(temp_range,error_array)
plt.yticks([])
#plt.plot(temp_range,error_array)
plt.xlabel("temperature /K")
plt.ylabel("Error", color ='blue')

plt.subplot(212)
#plt.title("Error plotted against temperature")
plt.plot(temp_range,error_array**-1, 'r')
plt.yticks([])
plt.ylabel("Likelihood (1/error)", color='red')
plt.show()

# Finds the smallest error in the error array and uses its index to return 
# the associated temp from the temp_range array
minimising_temp=temp_range[np.where(error_array==np.min(error_array))][0]

print(f"The temperature that gives the closest match to the obsered data is {round(minimising_temp,4)} degrees Kelvin")
