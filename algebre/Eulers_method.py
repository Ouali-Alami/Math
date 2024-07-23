# source : https://www.youtube.com/watch?v=6yslVB9-nR4
def expApproximation(totalDistance,nbPlots):
    step = totalDistance / nbPlots
    x , y = 0 , 1
    plotsApproximation = []
    for i in range (0, nbPlots):
        x += step
        y += step*y
        plotsApproximation.append( (x,y))
    return plotsApproximation  

#print(expApproximation(1,40))
  
    
