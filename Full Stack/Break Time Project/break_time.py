import time
import webbrowser

number_of_breaks = 3 
break_count = 0 

while break_count < number_of_breaks:
    time.sleep(1) # time in seconds before opening a browser 
    webbrowser.open('https://www.youtube.com/watch?v=N9nUsxbKu2A&index=45&list=PLCC51BF0C94BE62E8', new=1)
    break_count = (break_count + 1)
print "3 breaks are up"
