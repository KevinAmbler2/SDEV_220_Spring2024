import datetime

with open("today.txt", mode='w') as targetFile:
    targetFile.write(str(datetime.date.today()))

with open("today.txt", mode='r') as targetFile:
    today_string = targetFile.read()

    today = datetime.datetime.strptime(today_string, '%Y-%m-%d').date()
    print("Today is", today)