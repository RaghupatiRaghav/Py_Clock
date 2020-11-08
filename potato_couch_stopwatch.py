#! python3
#Potato Couch 'Stop' Watch
import datetime
import time
import subprocess

print('I am an alarm written in Python3.') 
print('I will raise an alarm to alert you of over-sitting.') 
print('When you hear the alarm, go take a break!')

print('How long do you want to wait until the alarm goes off?')

#Takes input for hours and minutes
x = input('Input hours (integer value): ')
y = input('Minutes (integer value): ')
x = int(x)
y = int(y)

#prints start time in HH:MM:SS format
start_time = datetime.datetime.now()
start = start_time.strftime('%H:%M:%S')
print("The start time is " + start)

#prints end time in HH:MM:SS format
stop_after = datetime.timedelta(hours = x, minutes = y)
end_time = start_time + stop_after
end = end_time.strftime('%H:%M:%S')
print("The end time is " + end)

#calculates time_left, updates the user about time left and makes the program go on sleep to save on computing power
time_left = (y*60) + (x*60*60)
while time_left>0:
    #If time left is more than or equal to an hour, give updates every 30 minutes
    if time_left>= (60*60):
        print('Time left until alarm: ' + str(time_left/60) + ' minutes')
        time.sleep(60*30)
        time_left = time_left - (60*30)
    #If time left is more than or equal to 30 mins but less than an hour, give updates every 15 minutes    
    elif (60*30) <= time_left < (60*60):
        print('Time left until alarm: ' + str(time_left/60) + ' minutes')
        time.sleep(60*15)
        time_left = time_left - (60*15)
    #If time left is more than or equal to 15 mins but less than 30 mins, give updates every 5 minutes    
    elif (60*15) <= time_left < (60*30) :
        print('Time left until alarm: ' + str(time_left / 60) + ' minutes')
        time.sleep(60 * 5)
        time_left = time_left - (60 * 5)
    #If time left is less than 15 mins, give updates every minute    
    else:
        print('Time left until alarm: ' + str(time_left / 60) + ' minutes')
        time.sleep(60)
        time_left = time_left - (60)



#opens alarm.mp3 file when time_left = 0    
subprocess.Popen(['start','alarm.mp3'], shell = True)


#Todo: Add snooze option, har minute pe vo time dikhaata hai, can you reduce this for longer alarms? 
