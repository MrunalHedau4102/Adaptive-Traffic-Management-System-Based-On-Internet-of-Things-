
import vehicle_1 as v
#import RPi.GPIO as GPIO
import time






def FindMaxDir() :
	dirr=[0,1,2,3]
	priority=[0,0,0,0]
	#send the video for each lane
	count = {"0":0 , "1":0,"2":0,"3":0}
	lane1_cnt=v.detectCars('lane1.mp4')
	count["0"]=lane1_cnt+5
	# lane2_cnt=v.detectCars('lane2.mp4')
	count["1"]=12
	lane3_cnt=v.detectCars('lane3.mp4')
	count["2"]=lane3_cnt
	# lane4_cnt=v.detectCars('lane4.mp4')
	count["3"]=8
	# cnnt=v.detectCars('lane1.mp4')
	# for i in range(4):
	# 	#cnt=v.detectCars()
		
	# 	count[str(i)]=count[str(i)]+cnnt
	# 	cnnt=cnnt+1
	Selected_Dir=int(max(count,key=count.get))
	for i in dirr:
		if(priority[i] == -10):
			Selected_Dir=i
		else:
			if(priority[Selected_Dir]<10):

				for i in dirr:

					if(Selected_Dir==i):
						priority[i]=priority[i]+5
					else:
						priority[i]=priority[i]-5
			else:
				count.pop(Selected_Dir)
				Max_Traffic=max(count,key=count.get)
				Selected_Dir=Max_Traffic
    # print(count[Selected_Dir])
	# return count[Selected_Dir]
	return count[str(Selected_Dir)]

					 
					 
	
def CalculateTime(TRAFFIC_COUNT):
	LENGTH=3
	
	lenn=TRAFFIC_COUNT/LENGTH
	TIME=15+lenn
	if(TIME<=90):
		return TIME
	else:
		TIME=90
		return TIME
		
	
	
	
	
	
	
def main() :
	while(1):
		TRAFFIC_COUNT = FindMaxDir()
		print(TRAFFIC_COUNT)
		if(TRAFFIC_COUNT==0) :
			continue
		else:
			break
	
	calculatedTime=CalculateTime(TRAFFIC_COUNT)
	print(calculatedTime)
	return calculatedTime
	
	#generateSignals(calculatedTime)


if __name__ == "__main__" :
	main()	


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
