#We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
#In the Gregorian calendar three criteria must be taken into account to identify leap years:

#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years




from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    #n = 10
    value = 0
    for i in range(1,n+1):
        print (i, end="")

   # print (value)
