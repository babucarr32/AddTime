def add_time(x, y, *optional):
    first_time = x[:-3]
    second_time = y
    opt = optional

    firstTimeSplitter = first_time.split(":")
    secondTimeSplitter = second_time.split(":")

    firstTimeHour = firstTimeSplitter[0]
    firstTimeMinute = firstTimeSplitter[1]

    secondTimeHour = secondTimeSplitter[0]
    secondTimeMinute = secondTimeSplitter[1]

    totalHour = (int(firstTimeHour) + int(secondTimeHour)) * 60
    totalMinute = int(firstTimeMinute) + int(secondTimeMinute)

    finalMinute = totalHour + totalMinute
    
    return int(1440 / finalMinute), 1440 % finalMinute

print(add_time("10:10 PM", "3:30"))

