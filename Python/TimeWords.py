#!/bin/python3

import sys

def timeInWords(h, m):
    # Complete this function
    hour = {1:"one",2:"two",3:"three",4:"four",5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve"}
    minute = {0:"o'clock", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"quarter", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 21:"twenty one", 22:"twenty two", 23:"twenty three", 24:"twenty four", 25:"twenty five", 26:"twenty six", 27:"twenty seven", 28:"twenty eight", 29:"twenty nine", 30:"half"}

    if m == 0:
        return(hour[h] + " o' clock")
    elif m == 1:
        return(minute[m] + " minute past " + hour[h])
    elif m == 15:
        return("quarter past " + hour[h])
    elif m < 30:
        return(minute[m] + " minutes past " + hour[h])
    elif m == 30:
        return(minute[m] + " past " + hour[h])
    elif m != 59 and m != 45:
        return(minute[60-m] + " minutes to " + hour[(h+1)%12])
    elif m==45:
        return("quarter to " + hour[(h+1)%12])
    elif m==59:
        return("one minute to " + hour[(h+1)%12])


if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
