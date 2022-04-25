# This program receives an integer n, which is between 1700 and 2700 (inclusively). The goal is to compute which day
# of the year is the 256th day of that year. It's important to take in account that from 1700 to 1917 the current
# calendar is the Julian Calendar. From 1919 to 2700 is the Gregorian Calendar. 1918 was a special year, in which right
# after the 31st January was 14th February.
# In the Julian Calendar a leap year (when february have 29 days) is when the year is divisible by 4.
# In the Gregorian Calendar a leap year is when the year is divisible by 400 or is divisible by 4 and not by 100
# Sample output -> 13.09.2017

year = int(input())
if(year >= 1917):
    if(year % 4) == 0:
        print("12.09.{}".format(year))
    else:
        print("13.09.{}".format(year))
if(year == 1918):
    print("26.09.{}".format(year))
else:
    if(((year % 400) == 0) or (((year % 4) == 0) and ((year % 100) != 0))):
        print("12.09.{}".format(year))
    else:
        print("13.09.{}".format(year))