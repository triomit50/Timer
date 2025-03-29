# importing the libraries
import time
from playsound import playsound
#defining the function
def timer(t):
    
    # running the clock timer
    while t:

        # converting the seconds into hours and mins and secs, how we wanna present in the timer 
        mins,secs = divmod(t,60)
        hrs,mins = divmod(mins,60)

        #setting up the timer display using the format function
        timer = "{:02d}:{:02d}:{:02d}".format(hrs,mins,secs)
        print(timer,end="\r")
        
        # pasuing the code for 1 sec before running the next line of code
        time.sleep(1)

        t=t-1
    playsound("E:\IMPORTANT STUFF\PYTHON\PYTHON CODES\Timer\microwave-timer-117077.mp3")



