n = 5
arr = [2, 3, 6, 6, 5]

highest = arr[0]
runnerUp = None

for i in range(0, n):
    if(arr[i] > highest):
        highest  = arr[i]
        runnerUp = highest
    elif(runnerUp == None and arr[i] < highest):
        runnerUp = arr[i] 
    elif(runnerUp != None):
        if(arr[i] > runnerUp and arr[i] < highest):
            runnerUp = arr[i]                   
    
if(runnerUp == None):
    runnerUp = highest

print(runnerUp)
        
    