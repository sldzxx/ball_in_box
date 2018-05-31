import math
import validate as val

__all__ = ['ball_in_box']

def divide(n):
    hen = 0.02
    pointList = []
    for i in range(n):
        for j in range(n):
            if (-1)+i*hen < 1 and (-1)+j*hen < 1:
                pointList.append( ((-1)+i*hen, (-1)+j*hen) )
    return pointList

def getDistance(center_1,center_2):
    return math.sqrt((center_1[0]-center_2[0])**2+(center_1[1]-center_2[1])**2)
    
def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """
    allPoints = divide(100)
    circleList=[]
    
    for i in range(m):
        mmaxC=[0,0,0]
        for point in allPoints:
            mminR = min(map(abs,[point[0]-1,point[0]+1,point[1]-1,point[1]+1]))
            for block in blockers:
                mminR = min(mminR,getDistance(point,block))
            for circle in circleList:
                mminR = min(mminR,getDistance(point,circle)-circle[2])
            if  mminR > mmaxC[2]:
                mmaxC[0] = point[0]
                mmaxC[1] = point[1]
                mmaxC[2] = mminR

        circleList.append(mmaxC)   
        allPoints = list(filter(lambda p: getDistance(p,mmaxC) > mmaxC[2] , allPoints))       

    return circleList