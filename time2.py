class Time(object):
    """represents time in hours, minutes, seconds"""
t1 = Time()
t1.hour = 10
t1.minute = 42
t1.second = 23

t2 = Time()
t2.hour = 10
t2.minute = 54
t2.second = 02


def is_after(t1, t2):
    if (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second):
        print "True"
    print "False"

is_after(t1, t2)


