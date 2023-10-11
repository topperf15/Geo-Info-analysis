from qgis import processing
#from statistics import mean
import matplotlib.pyplot as plt #for plotting the results in a histogram
Dmean = [] #mean distance
inFile = '/Users/andrew_s/Library/Mobile Documents/com~apple~CloudDocs/APL/strat ed/Lesson X exercise/WY.shp|layername=WY'
#rndpts= '/Users/andrew_s/Library/Mobile Documents/com~apple~CloudDocs/APL/strat ed/Lesson X exercise/randompts.shp'
niter = 1000 #number of iterations
nrndpt = 100 #number of random points in polygon
nbins = 40 #number of bins for histogram

for i in range(niter):
    
    param1 = {'INPUT':inFile,
                'STRATEGY':0,
                'VALUE':nrndpt,
                'MIN_DISTANCE':None,
                'OUTPUT':'TEMPORARY_OUTPUT'
                }
    step1 = processing.run("qgis:randompointsinsidepolygons", param1)
    #QgsProject.instance().addMapLayer(step1['OUTPUT'])
    #print(step1)
    param2 = {'INPUT':step1['OUTPUT'],
                'OUTPUT_HTML_FILE':'TEMPORARY_OUTPUT'}
    result = processing.run("native:nearestneighbouranalysis", param2)
    Dmean.append(result['OBSERVED_MD'])
    #print(Dmean, ' ' , sum(Dmean),mean(Dmean))
    #QgsProject.instance().removeMapLayer(step1['OUTPUT'])
plt.hist(Dmean, bins=nbins)
plt.show()
    
