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

    if "PM" in x:
        Time = '{:02d}:{:02d}'.format(*divmod(finalMinute, 60))
        spliter = Time.split(":")
        MyTime = spliter[0]
        if int(MyTime) >= 12:
            return f"{int(MyTime) - 12}:{spliter[1]} AM (next day)" # formating the time for output
        else:
            return f"{str(MyTime).replace('0', '')}:{spliter[1]} PM" # formating the time for output

print(add_time("3:00 PM", "3:10"))

