import math
import numpy as np
import matplotlib.pyplot as plt

#Functions############################################################################################

#Calculates the amount of substance remaining given half_life, initial amount and time
def amount_left(tau, p_nought, time):
  return  p_nought*np.exp(-math.log(2)*time/tau)
  
#Calculates the amount of substance needed for 5 grams to be lef after 30 seconds given the half_life
def amount_needed(tau):
     return 5*np.exp(math.log(2)*30/tau)
     
# Returns a tuple of numpy arrays for the x and y values to use in drawing graphs
def build_time_series(half_life,p_nought, max_time=10):
    ar = np.linspace(0,max_time)
    return (ar, amount_left(half_life, p_nought, ar)) #(x,y)

#Builds a graph for decay of isotope over time.
def do_graph(name, time_series,single=True):
    x, y = time_series
    plt.plot(x, y)
    if single:
        plt.title("Decay of " + name +" over time")
    else:
        plt.title("Decay of isotopes studied over time")

  
#Returns a tuple of inputed and calculated isotope data
def get_input():
  isotope_name=input("Please enter the name of the isotope");
  half_life=float(input("Please enter the half-life of the isotope in seconds"))
  p_nought = float(input("Please enter the initial amount in grams"))
  time=float(input("Please enter a time in seconds"))
  #max_time=float(input("Please enter the maximum time for the graph.  Default is 10s") or 10)
  max_time=10
  time_series=build_time_series(half_life, p_nought, max_time )
  return(isotope_name,half_life,p_nought,time,time_series )

###################################################################################################

#Initialise list to keep isotope data in
isotopes=[]

#Main loop to process each isotope
while True:
  plt.clf() #clears any current graphs
  data=get_input() # Gets a tuple of the isotope data
  isotope, half_life,p_nought,time,time_series= data #Decomposes the tuple into its bits
  p=amount_left(half_life,p_nought,time) #Calculates the amount left at the given time
  start_amount = amount_needed(half_life)  # Calculates the starting amount.
  do_graph(isotope, time_series) #Creates a graph
  isotopes.append((isotope,half_life,p_nought,time,time_series))#Builds the list used in doing the final graph
  #output stuff
  print ""
  print "Starting with ", p_nought, "grams of",isotope, "after", time, "seconds there will be", round(p, 2), "grams remaining \n"
  print "In order to have 5 grams left after 30 seconds you should start with", round(start_amount, 2), "grams \n"
  plt.show() #displays the graph
  if input("Do you want to do another isotope y/n")=="n":
    print ""
    break
  else: 
    print ""

#Processes the final list and does the graph of multiple isotopes
for isotope in isotopes:
  name=isotope[0]
  time_series=isotope[4]
  do_graph(name, time_series, False)
plt.show()

# Output list of isotopes studied, tweak to get commas right (yes I am that sad).
iso_string = ""
for n in range(len(isotopes)):
    if n < len(isotopes)-2:
        iso_string += isotopes[n][0]+", "
    elif n==len(isotopes)-2:
        iso_string+=isotopes[n][0]+" and "
    else:
        iso_string += isotopes[n][0]
  

print "Isotopes studied:", iso_string


  
