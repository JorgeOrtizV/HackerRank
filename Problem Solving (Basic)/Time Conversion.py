# This program receives a 12 AM/PM hour, the goal is to convert it into a 24 hr clock

def conversor(hour):
    converted = ""
    Stunde = ""
    if((hour.find("AM") != -1) and (hour[0:2] == "12")):
        converted = "00"+hour[2:8]
    elif(hour.find("AM") != -1) or (hour[0:2] == "12"):
        converted = hour[0:8]
    else:
        Stunde = str(int(hour[0:2])+12)
        converted = Stunde[0:2] + hour[2:8]
    print(converted)

hour = input()
conversor(hour)