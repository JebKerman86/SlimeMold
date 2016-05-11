from PIL import Image
import numpy as np



def ImageToArray(imName):
    im = Image.open(imName)    
    imArray = np.array(im)
    return imArray


def ColorToBW(imArrayColor):
    
    imShape = imArrayColor.shape    
    imArrayBW = np.zeros((imShape[0],imShape[1]))
        
    #Durchschnitt der drei Farben bilden
    for i in range(0,imShape[0]):
        for j in range(0,imShape[1]):
            avgVal = 0
            for k in [0,1,2]:
                avgVal = avgVal + imArrayColor[i][j][k]
            avgVal = avgVal/3
            imArrayBW[i][j] = avgVal
            
    return imArrayBW


def FindCenter(imArray):
    imShape = imArray.shape
    imCenter = np.array([imShape[0]/2,imShape[1]/2])
    return imCenter


#Koordinationsystem Ursprung oben links im Bild (Y-Axe Zeigt nach unten!!)
def kymograph(imArray,Start,R,Phi):
    #Input: Länge R(in Pixel), Richtung Phi (Winkel in degree)

    StepSize = 0.1
    NumberOfSteps = R/StepSize
    Phi = Phi * (2.0*np.pi) / 360.0
    imDirection = np.array([np.cos(Phi),-np.sin(Phi)])*StepSize
     
    imSlice = []    
    imCoords_round_previous = [-1,-1]
    
    for t in range(0,int(NumberOfSteps)):
        imCoords = Start + imDirection*t
        imCoords_round = np.round(imCoords,decimals=0)
        if (np.array_equiv(imCoords_round,imCoords_round_previous) == False and imCoords_round[0] > 0 and imCoords_round[1] > 0):
            print(imCoords_round)
            imSlice.append(imArray[imCoords_round[0],imCoords_round[1]])
            imCoords_round_previous = imCoords_round
             
    NumberOfPixels = len(imSlice)
    print("NumberOfPixels:  " + str(NumberOfPixels))
    if(NumberOfPixels != 0):
        AvgPixelDist = R/(NumberOfPixels-1)
     
    return [imSlice,AvgPixelDist]
     
 
     
 
TestArray = ColorToBW(ImageToArray("test.tif"))
Out = kymograph(TestArray,np.array([50,50]),100.0,0)
 
print("Average Pixel Distance:  " + str(Out[1]))
print(Out[0])




#im_mod = Image.fromarray(imarray)



