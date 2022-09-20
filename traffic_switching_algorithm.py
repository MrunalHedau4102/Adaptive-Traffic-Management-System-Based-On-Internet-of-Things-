
import vehicle_1 as v


def main() :
	while(true):
		TRAFFIC_COUNT = FindMaxDir()
		if(TRAFFIC_COUNT==0) :
			continue
		else:
			break
	
	calculatedTime=CalculateTime(TRAFFIC_COUNT)
	generateSignals(calculatedTime)


if __name__ == "__main__" :
	main()




def FindMaxDir() :
	dirr=[0,1,2,3]
	priority=[0,0,0,0]
	#send the video for each lane
	count = []
	for i in range(4):
		cnt=v.detectCars()
		count.append(cnt)
		cnt=cnt+1
	Selected_Dir=max(count)
	for i in dirr:
		if(priority[i] == -10):
			Selected_Dir=i
		else:
			if(priority[i]<10):
				 for i in dirr:
					 
					 
	




def detectVehicles():
	
	
	
	
	
	
	
	
def generateCount():
	
	
	
	
	
	
	
def CalculateTime(TRAFFIC_COUNT):
	LENGTH=3
	
	lenn=TRAFFIC_COUNT/LENGTH
	TIME=15+lenn
	if(TIME<=90):
		return TIME
	else:
		TIME=90
		return TIME
		
	
	
	
	
	
	
	

def generateSignals():
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
