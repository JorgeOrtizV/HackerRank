# An anagram are two strings who have the same letters in exactly the same frequency. This program calculates how many
# anagrams are in a given dictionary.
# The input is an integer n, which is the size of the dictionary. Then each line of input is a word of the dictionary.
# Then comes an integer m, which is the size of a string array. Then each line is an input of query.
# The goal is to compute how many words of the dictionary are anagrams of query[i].

def anagram(query, dictionary, n):
    for i in query:
        count = 0
        for j in range(n):
            if len(i) == len(dictionary[j]):
                sorted_string1 = sorted(i)
                string1 = "".join(sorted_string1)
                sorted_string2 = sorted(dictionary[j])
                string2 = "".join(sorted_string2)
                if string1 == string2:
                    count += 1
        print(count)

n = int(input())
dictionary = []
query = []
for i in range(n):
    dictionary.append(input())
m = int(input())
for i in range(m):
    query.append(input())
anagram(query, dictionary, n)