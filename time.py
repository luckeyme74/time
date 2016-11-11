class Time(object):
    """represents the time of day in hours, minutes and seconds"""
t = Time()
t.hour = 11
t.minute = 59
t.second = 30

def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

print_time(t)
