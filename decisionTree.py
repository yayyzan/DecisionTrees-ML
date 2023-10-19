import numpy as np

def getData(path):
    data=[]
    for line in open(path):
        if line.strip() !='':
            row = line.strip().split()
            #maybe something to make sure data is 8 elemnts long
            datum = list(map(float,row[:]))
            data.append(datum)
    data=np.array(data)
    return data

data=getData("C:/Users/james/Desktop/Imperial/year 3/ML/mlcourseworkone/CW1 60012/wifi_db/clean_dataset.txt")

#function for random testing

def calcEntropy(data):
    roomNumbers=[]
    numSamples=len(data)
    entropyArray=[]
    for line in data:
        roomNumbers.append(line[-1])
    distinctRoomNums=np.unique(roomNumbers)
    for roomNumber in distinctRoomNums:
        counter=0
        for line in data:
            if roomNumber == line[-1]:
                counter+=1
        entropyArray.append(weightedInfoPerSymbol(counter,numSamples))
    return sum(entropyArray)

def weightedInfoPerSymbol(numerator,denominator):
    return (-numerator/denominator)*np.log2(numerator/denominator)





def findSplit(data):
    maxIG=[]
    #sort data by each attribute val
    for router in range (0,6):
        sortedRouter=data[data[:, router].argsort()]
        #need to iterate through sorted column in array to find optimum split for each attribute (store it in smthn)
    #choose best split out of all attributes
    print(sortedRouter)
    
print(findSplit(data))


#def drawTree():
