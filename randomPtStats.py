from qgis import processing
#from statistics import mean
import matplotlib.pyplot as plt #for plotting the results in a histogram
from scipy.stats import norm #for fitting a normal (Gaussian) distribution
Dmean = [] #mean distance
inFile = '/Users/andrew_s/Library/Mobile Documents/com~apple~CloudDocs/APL/strat ed/Lesson 6 exercise/WY/WY.shp'
#rndpts= '/Users/andrew_s/Library/Mobile Documents/com~apple~CloudDocs/APL/strat ed/Lesson X exercise/randompts.shp'
niter = 1000 #number of iterations
nrndpt = 100 #number of random points in polygon
nbins = 40 #number of bins for histogram

for i in range(niter):
    #step 1 is to run the random pts in polygon algorithm
    #parameters for step 1
    param1 = {'INPUT':inFile,
                'STRATEGY':0,
                'VALUE':nrndpt,
                'MIN_DISTANCE':None,
                'OUTPUT':'TEMPORARY_OUTPUT'
                }
    step1 = processing.run("qgis:randompointsinsidepolygons", param1)
    #QgsProject.instance().addMapLayer(step1['OUTPUT'])
    #print(step1)
    #step 2 is to run the nearest neighbor algorithm
    # using the output from step 1
    param2 = {'INPUT':step1['OUTPUT'],
                'OUTPUT_HTML_FILE':'TEMPORARY_OUTPUT'}
    result = processing.run("native:nearestneighbouranalysis", param2)
    #add value of this iteration to the Dmean list (array)
    Dmean.append(result['OBSERVED_MD'])
    #print(Dmean, ' ' , sum(Dmean),mean(Dmean))
    #QgsProject.instance().removeMapLayer(step1['OUTPUT'])
#plot the results in a histogram
plt.hist(Dmean, bins=nbins)
plt.show()
#fit results into a normal distribution calculating mean and std dev
(mu, sigma) = norm.fit(Dmean)
print(mu)
print(sigma)
    
