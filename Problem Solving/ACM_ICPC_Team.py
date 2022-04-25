from itertools import combinations

def team_aranger(atendees, atendees_expertise):
    atendees_list = combinations(range(1, atendees+1),2)
    possible_teams = list(atendees_list)
    max = 0
    counter = 0
    for i in possible_teams:
        expertise1 = atendees_expertise[i[0]-1]
        expertise2 = atendees_expertise[i[1]-1]
        combined_expertise = str(bin((expertise1 | expertise2)))
        combined_expertise = sum(list(map(int, list(combined_expertise[2:]))))
        if combined_expertise > max:
            max = combined_expertise
            counter = 1
        elif combined_expertise == max:
            counter += 1
        else:
            pass        
    return max, counter


if __name__ == "__main__":
    attendees, topics = list(map(int, input().split()))
    attendees_expertise = []
    for i in range(attendees):
        attendees_expertise.append(int(input(), 2))
    max, counter = team_aranger(attendees, attendees_expertise)
    print(max)
    print(counter)
    