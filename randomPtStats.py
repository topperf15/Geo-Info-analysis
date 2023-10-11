from qgis import processing
#from statistics import mean
import matplotlib.pyplot as plt
Dmean = []
inFile = '/Users/andrew_s/Library/Mobile Documents/com~apple~CloudDocs/APL/strat ed/Lesson X exercise/WY.shp|layername=WY'
#rndpts= '/Users/andrew_s/Library/Mobile Documents/com~apple~CloudDocs/APL/strat ed/Lesson X exercise/randompts.shp'
for i in range(1000):
    
    param1 = {'INPUT':inFile,
                'STRATEGY':0,
                'VALUE':100,
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
plt.hist(Dmean, bins=40)
plt.show()
    