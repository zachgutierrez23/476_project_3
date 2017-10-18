# Author: Zach Gutierrez
# Course: TCMG 476 - Project 3
# Date: 10/17/17
# Objective: write a code to inspect a log file on the internet

from datetime import datetime

def main():
    f = open('http_access_log', 'r')
    count = 0 
    allLine = []
    by_weekday = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    by_month = {}
    
    for line in f:
        count += 1
        allLine.append(line)
        split_data = line.split()
        
        try:
            str_date = line.split()[3][1:].split(':')[0]
        except:
            pass
        date = datetime.strptime( str_date, "%d/%m/%y" )
        by_weekday[date.weekday()] += 1
        
        if count > 20000:
            print by_weekday
            return 0
        print ("1. How many total request were made in the time period represented in the log?")
        
        print len(allLine)
        
main()
               
