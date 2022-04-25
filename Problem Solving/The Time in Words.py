# The object of this program is to transform a numerical hour into words, just like
# humans says which hour is it.
# Input:
# First line -> integer h, where 1<= h <= 12
# Second line -> two integers, which means minutes.
# Ouput format.
# 5:00 -> five o' clock
# if 0 < minutes <= 30 -> 5:15 -> fifteen minutes past five
# if 30 < minutes -> 5:47 -> thirteen minutes to six


numbers = {1:"one",
           2:"two",
           3:"three",
           4: "four",
           5:"five",
           6:"six",
           7:"seven",
           8:"eight",
           9:"nine",
           10:"ten",
           11:"eleven",
           12:"twelve",
           13:"thirteen",
           14:"fourteen",
           15:"fifteen",
           16:"sixteen",
           17:"seventeen",
           18:"eigteen",
           19:"nineteen",
           20:"twenty",
           21:"twenty one",
           22:"twenty two",
           23:"twenty three",
           24:"twenty four",
           25:"twenty five",
           26:"twenty six",
           27:"twenty seven",
           28:"twenty eight",
           29:"twenty nine",
           30: "thirty",
           }

def clock(hour, minutes):
    hour_string = ""
    if minutes == 0:
        hour_string += numbers[hour]
        hour_string += " o' clock"
    elif minutes <= 30:
        if minutes == 1:
            hour_string += ("one minute past " + numbers[hour])
        elif minutes == 15:
            hour_string += ("quarter past " + numbers[hour])
        elif minutes == 30:
            hour_string += ("half past " + numbers[hour])
        else:
            hour_string += (numbers[minutes] + " minutes past " + numbers[hour])
    else:
        minutes_to = 60-minutes
        if minutes_to == 1:
            if hour == 12:
                hour_string += ("one minute to one")
            else:
                hour_string += ("one minute to " + numbers[hour+1])
        elif minutes_to == 15:
            if hour == 12:
                hour_string += ("quarter to one")
            else:
                hour_string += ("quarter to " + numbers[hour+1])
        else:
            if hour == 12:
                hour_string += (numbers[minutes_to] + " minutes to one")
            else:
                hour_string += (numbers[minutes_to] + " minutes to " + numbers[hour+1])
    print(hour_string)


hour = int(input())
minutes = int(input())
clock(hour, minutes)