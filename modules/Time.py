from datetime import datetime

now = datetime.now()
hour = now.hour

def checkTime():
    if hour >= 19:
        return 'It\'s time to leave'
    else:
        return f'You have {19 - hour} hours work left'


print(checkTime())
