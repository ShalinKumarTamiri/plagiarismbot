#importing packages
from datetime import datetime
import random
	
	
#function for welcoming 
def welcome_greeting():
	#creating multiple welcomes 
	welcome_responses = ["Nice to meet you ","Lets have some good time ","I am happy to have you ","I am so glad to welcome you "]
	
	#geeting current time
	current_time = datetime.now().hour
	greeting = "Good Morning !"
	#finding greeting according to time 
	if current_time > 22:
		greeting = "It is too late but I can help you in any time"
	elif current_time > 16:
	   greeting = "Good Evening !"
	elif current_time > 12:
	   	greeting = "Good Afternoon !"
	return f"{greeting}, {random.choice(welcome_responses)}"
    
