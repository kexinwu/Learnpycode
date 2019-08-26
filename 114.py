# 排序不支持原生比较的对象 输不出结果？？
from operator import attrgetter
class User:
    def __init__(self,user_id):
        self.user_id = user_id
    
    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(23),User(3),User(99)]
    print(users)
    print(sorted(users,key=lambda u:u.user_id))
    print(sorted(users,key=attrgetter('user_id')))
