import csv
import operator

import twitter
from collections import Counter


users={
	'name':[None]*twitter.getNum(),
	'numOfFollowers':[None]*twitter.getNum(),
	'retweet':[None]*twitter.getNum(),
    'date':[None]*twitter.getNum(),
    'hour': [None]*twitter.getNum(),
    'twtperhour':[None]*twitter.getNum()
}
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
def getTime(s):

    return s[find_str(s, ':')+1:len(s)]

def getHour(s):
   return int(getTime(s)[0:2])
i=0
counter=0
fileName=twitter.getFile()
with open(fileName,encoding='utf-8') as file:

    reader= csv.reader(file, delimiter=' ')
    for line in reader:
        list=line

        print ('i is '+str(i))
        print (list)
        users['name'][i]=list[0]
        users['numOfFollowers'][i] = list[len(list)-2]
        users['retweet'][i] = list[len(list)-1]
        users['date'][i]=list[1]
        users['hour'][i]=getHour(users['date'][i])
        users['twtperhour'][i] = 0


        i+=1

print (users)


def bubbleSort(alist,list1,list2,list3,list4,list5):
    print(len(alist))
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            y=int(alist[i])
            z=int(alist[i+1])
            if y>z:
               temp2= list1[i]
               temp3=list2[i]
               temp4=list3[i]
               temp5=list4[i]
               temp6=list5[i]
               list1[i]=list1[i+1]
               list2[i]=list2[i+1]
               list3[i]=list3[i+1]
               list4[i]=list4[i+1]
               list5[i]=list5[i+1]

               list2[i+1]=temp3
               list1[i+1]=temp2
               list3[i+1]=temp4
               list4[i+1]=temp5
               list5[i+1]=temp6
               temp = y
               alist[i] = z
               alist[i+1] = temp

bubbleSort(users['numOfFollowers'],users['retweet'],users['name'],users['hour'],users['date'],users['twtperhour'])


with open('followers_sorted.txt', 'w') as text:

    for s in range(i):
        text.write(str(s+1)+' '+ users['name'][s]+ ' '+str(users['numOfFollowers'][s])+'\n')


bubbleSort(users['retweet'],users['numOfFollowers'],users['name'],users['hour'],users['date'],users['twtperhour'])

with open('retweet_sorted.txt', 'w') as text:

    for s in range(i):
        text.write(str(s+1)+ ' '+users['name'][s]+ ' '+str(users['retweet'][s])+'\n')


def findMin(list):

    min=list[0]
    index=0
    for number in range(0,len(list)):
        if(min>list[number]):
            min=list[number]
            index=number
    return min


def findMax (list):
    max = list[0]
    index = 0
    for number in range(0, len(list)):
        if (max < list[number]):
            max = list[number]
            index = number
    return max

def resetrate(list):
    for i in list:
        i=0

def nameCounter(list):
    return dict(Counter(list))

minhour=findMin(users['hour'])
maxhour=findMax (users['hour'])
print(minhour)
for minhour in range(minhour,maxhour+1):
        resetrate(users['twtperhour'])
        list = []
        list2=[]
        for i in range(0,len(users['hour'])):

            if (int(users['hour'][i])==int(minhour)):

                list.append(users['name'][i])
                list2.append(i)

        a=nameCounter(list)
        print(a)
        for z in list2:

            users['twtperhour'][z]=a[users['name'][z]]









bubbleSort(users['twtperhour'],users['numOfFollowers'],users['name'],users['hour'],users['date'],users['retweet'])

with open('tweetperhour_sorted.txt', 'w') as text:

    for s in range(0,len(users['twtperhour'])):
        text.write(str(s+1)+' '+ users['name'][s]+ ' '+str(users['twtperhour'][s])+'\n')





