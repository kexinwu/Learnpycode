#第三章 数字日期和时间 3.11-3.15内容
#问题:你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
import random
values =[1,2,4,6,8,5]
print(random.choice(values))
print(random.sample(values,3))
#打乱顺序
print(values)
random.shuffle(values)
print(values)
#生成随机整数
print(random.randint(1,9))
#生成随机浮点数
print(random.random())
#获取n位随机位整数
print(random.getrandbits(15))

#3.12 基本的日期与时间转换
#问题:你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。
from datetime import timedelta
a=timedelta(days=2,hours=6)
b=timedelta(hours=4.5)
c=a+b
print(c.days)
#没有print(c.hours)功能
print(c.seconds/3600)
print(c.total_seconds()/3600)

#如果你想表示指定的日期和时间，先创建一个 datetime 实例然后使用标准的数学 运算来操作它们。
from datetime import datetime
d = datetime (2012,12,21)
print(d+timedelta(days=10))

#3.13 计算最后一个周五的日期
#问题:你需要查找星期中某一天最后出现的日期，比如星期五。

from datetime import datetime ,timedelta
import sys
weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#上面的算法原理是这样的：先将开始日期和目标日期映射到星期数组的位置上 (星 期一索引为 0)，然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然 后用开始日期减去那个时间差即得到结果日期。 
def get_previous_byday(dayname,start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    s='day_num : {name}'
    print( s.format(name = day_num) )
   
    day_num_target = weekdays.index(dayname)
    s1='day_num_target:{name1}'
    print(s1.format(name1 = day_num_target))

    day_ago = (7+day_num-day_num_target)%7
    s2='day_ago : {name2}'
    print(s2.format(name2 = day_ago))

    if day_ago==0:
        day_ago=7
    target_date = start_date-timedelta(days=day_ago)
    return target_date

print(datetime.today())
print(get_previous_byday('Friday')) 

#3.14 计算当前月份的日期范围
#问题:你的代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方 法。

from datetime import datetime,date,timedelta
import calendar
def get_month_range(start_date=None):
    if start_date is None: start_date = date.today().replace(day=1) 
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month) 
    end_date = start_date + timedelta(days=days_in_month) 
    return (start_date, end_date)
a_day = timedelta(days=1) 
first_day, last_day = get_month_range() 

while first_day < last_day: 
     print(first_day) 
     first_day += a_day 

#3.15 字符串转换为日期
#问题:你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便 在上面执行非字符串操作。

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text,'%Y-%m-%d')
z = datetime.now()
print(z-y)

#3.16 结合时区的日期操作
#问题:你有一个安排在 2012 年 12 月 21 日早上 9:30 的电话会议，地点在芝加哥。而你 的朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？

from datetime import datetime
from pytz import timezone
d = datetime.now()
print(d)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

#pytz 已经不再建议使用了
# utc_d = loc_d.astimezone(pytz.utc) 
# print(utc_d)
# print(pytz.country_timezones['IN'])