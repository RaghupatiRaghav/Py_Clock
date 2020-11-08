# alarm_clock 

## About
This is an alarm clock written in Python3. The code uses [datetime](https://docs.python.org/3/library/datetime.html), [time](https://docs.python.org/3/library/time.html) and [subprocess](https://docs.python.org/3/library/subprocess.html) modules. The user inputs the duration for the alarm. The program then sleeps to optimize system's computing resources, giving user an occasional update on the time left. Longer the duration of alarm, longer the program sleeps and fewer the number of times it updates. As the duration draws to zero, the number of updates increase. Finally, the program opens alarm.mp3 file to alert the user. The motivation for the project is Al Sweigart's book titled ['Automate The Boring Stuff With Python'](https://automatetheboringstuff.com/2e/chapter17/).     

_Author's Note_: I wrote this alarm clock to alert me of oversitting while working. I have since used it for a variety of purposes. Notably, I SSHed the script to a Raspberry Pi 4 connected to a BT speaker to wake me up when September ends. I am serious!.     

## Getting Started:

#### Downloading Script:

1. Clone the repository or directly download file *alarm_clock.py*.
2. Drag and drop the downloaded file into a python environment (such as Anaconda Terminal or Bash).
3. The terminal will now ask you to input the duration in hours and minutes (both of these inputs should be positive integer values) for which you want the script to run. For instance, if I want the script to run for half an hour, my input would be *Input hours (positive integer values only): 0* and *Input minutes (positive integer values only): 30*
4. The terminal will now show you the start time, the end time 
5. To stop the script prematurely, simply press *Ctrl* and *c* simultaneously. 


#### Changing alarm sound:

1. Delete the existing file named _'alarm.mp3'_.
2. Copy paste preferred mp3 file in the same directory as the script *alarm_clock.py*.
3. Rename the file to _'alarm.mp3'_.







