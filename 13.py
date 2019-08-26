#保留最后N个元素 ???
from collections import deque

# q = deque(maxlen = 3)
# q.append(1)
# q.append(1)
# q.append(1)
# print(q)

# q.append(3)
# print(q)

# q = deque()
# q.append(1)
# q.append(1)
# q.appendleft(4)
# print(q)

# q.pop()
# print(q)

# q.popleft()
# print(q)

def search(lines,pattern,history=2):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line :
            yield line,previous_lines
            print(line)
        previous_lines.append(line)

if __name__=='__main__':
    with open(r'D:/Mycode/Python3/Cookbook/somefile.txt') as f:
        for line, prevlines in search(f,'python',2):
            for pline in prevlines:
                print(pline,end='##')
            print(line,end='!!')
            print('_'*20)
