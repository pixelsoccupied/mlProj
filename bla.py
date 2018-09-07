import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import threading
import time


# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime(time.time()))


class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        print("Inside the __eq__method")
        return self.name == other.name

    def getkey(self):
        "k"

    def __repr__(self) -> str:
        return '{}'.format(self.name)
    def retursomething (self):
        return Person("Bal")



a = Person("John")
b = Person("John")



exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
#thread1.start()
#thread2.start()

print("Exiting Main Thread")
print(a)

tuple = ("Jack", 2, 4, 5)
print("size ", len(tuple))
print(tuple[2:5])

lst = [3, 1, 353]

print(lst, "hello")

dic = {"key": 4, "key2": 9}

print(dic.values())

x = 3
y = 3
if (a == b):
    print("It is 5")

for key, value in dic.items():
    print(key, value)

for i, kk in enumerate(lst):
    print(i, kk)

"""In Python 3 open() gives you a stream producing 
Python's unicode strings, and the underlying yajl doesn't know 
how to deal with those. So, the correct way of
 parsing JSON files is actually to open them in 'rb' mode."""



df = pd.read_json("health_inspection_chi_sample.json", lines=True) # type: pandas.core.frame.DataFrame

df2 = df[['inspection_date']]
print(type(df2))
df1 = df.loc[0:5, ['risk', 'inspection_date']]
print("tHE TYPE IS --> ",'\n', df1.to_string())


print("\nIndex method\n -->", df.index)
print("\nHead method\n -->", df.head())
print(df.columns.tolist())
#change index to something else
df.set_index('inspection_id')

print(df['results'].value_counts())


y = df['zip'].unique().tolist()
print(lst)
print('The type is', type(lst))
x = df['zip'].value_counts().tolist()

#plt.hist(y, x)
#plt.show()


print("Chage inspection datetime --> ")
print("\n")
print(type(df2))
df2 = df2.apply(pd.to_datetime())
df1 = df.loc[0:5, ['risk', 'inspection_date']]
print("tHE TYPE IS --> ",'\n', df1.to_string())

print ("Im just out here changing git stuff")


