# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:54:21 2024

@author: mahir
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime
df=pd.read_csv("C:\\Users\\mahir\\OneDrive\\Desktop\\Delhi climate data(2017).csv")
def day():
    day=int(input('Enter the day : '))
    month=int(input('Enter the month : '))
    year=2017
    day_of_year=datetime.datetime(year,month,day).timetuple().tm_yday
    print(df.loc[day_of_year-1])
def week():
    week=int(input('Enter the week : '))
    s=(week-1)*7
    e=(week*7)-1
    print(df.loc[s:e])
def c_day():
    d1=int(input('Enter the day(1-31) : '))
    m1=int(input('Enter the month : '))
    y1=2017
    date1=str(d1)+'-'+str(m1)+'-'+str(y1)
    doy1=datetime.datetime(y1,m1,d1).timetuple().tm_yday
    d2=int(input('Enter the day(1-31) : '))
    m2=int(input('Enter the month : '))
    y2=2017
    date2=str(d2)+'-'+str(m2)+'-'+str(y2)
    doy2=datetime.datetime(y2,m2,d2).timetuple().tm_yday
    f=input('1.meantemp\n2.humidity\n3.wind_speed\n4.meanpressure\nEg:meantemp\nEnter your factor choice : ')
    d=[date1,date2]
    df1=df.loc[doy1-1,f]
    c1=df1.tolist()
    df2=df.loc[doy2-1,f]
    c2=df2.tolist()
    l=[c1,c2]
    plt.bar(d,l,width=0.2)
    plt.xlabel('Date')
    plt.ylabel(f)
    plt.title('Climate Comparision')
    plt.show()
def week_avg():
    week=int(input('Enter the week : '))
    s=(week-1)*7
    e=(week*7)-1
    f=input('1.meantemp\n2.humidity\n3.wind_speed\n4.meanpressure\nEg:meantemp\nEnter your factor choice : ')
    df0=df.loc[s:e,f]
    l=df0.tolist()
    s=0
    for i in range(7):
        s=s+l[i]
    avg=s/7
    print('Average '+f+' is '+str(avg))
def c_week():
    f=input('1.meantemp\n2.humidity\n3.wind_speed\n4.meanpressure\nEg:meantemp\nEnter your factor choice : ')
    w1=int(input('Enter week1 : '))
    s=(w1-1)*7
    e=(w1*7)-1
    df0=df.loc[s:e,f]
    l=df0.tolist()
    s=0
    for i in range(7):
        s=s+l[i]
    a1=s/7
    w2=int(input('Enter week2 : '))
    s=(w2-1)*7
    e=(w2*7)-1
    df0=df.loc[s:e,f]
    l=df0.tolist()
    s=0
    for i in range(7):
        s=s+l[i]
    a2=s/7
    w1='week'+str(w1)
    w2='week'+str(w2)
    w=[w1,w2]
    l=[a1,a2]
    plt.bar(w,l,width=0.2)
    plt.xlabel('Week')
    plt.ylabel(f)
    plt.title('Climate Comparision')
    plt.show()
def week_g():
    f=input('1.meantemp\n2.humidity\n3.wind_speed\n4.meanpressure\nEg:meantemp\nEnter your factor choice : ')
    w1=int(input('Enter start week : '))
    w2=int(input('Enter end week : '))
    l1=[]
    l2=[]
    for i in range(w1,w2+1):
        s=(i-1)*7
        e=(i*7)-1
        df0=df.loc[s:e,f]
        l=df0.tolist()
        s=0
        for j in range(7):
            s=s+l[j]
        a1=s/7
        l1.append(a1)
        l2.append('w'+str(i))
    plt.bar(l2,l1,width=0.2)
    plt.xlabel('Week')
    plt.ylabel(f)
    plt.title('Climate Comparision')
    plt.show()
while True:
    c=int(input('1.Record of a day\n2.Record of a week\n3.Compare any two days\n4.Average of week\n5.Compare any two weeks\n6.Interval of weeks comparision\n7.Exit\nEg:1\nEnter your choice : '))
    if(c==1):
        day()
    elif(c==2):
        week()
    elif(c==3):
        c_day()
    elif(c==4):
        week_avg()
    elif(c==5):
        c_week()
    elif(c==6):
        week_g()
    elif(c==7):
        print('Thank you visit again')
        break
    else:
        print('Invalid Choice')