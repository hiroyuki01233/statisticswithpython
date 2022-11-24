import datetime

now = datetime.datetime.now()
ts = "2022-11-22 23:05:48"
f = "%Y-%m-%d %H:%M:%S"
theday = datetime.datetime.strptime(ts, f)
themonthday = theday.strftime("%Y-%m-%d")
print((now - theday).days == 0)