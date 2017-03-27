# -*- coding: utf-8 -*-
'''	
forgetting_curve.py
This program aims at generating a plan for memorizing
vocabularies according to the Forgetting Curve.

Copyright (c) 2015 Libao Jin
Licence: unknown
'''

import math
import itertools

__author__ = 'Libao Jin'
__date__ = 'July 03, 2015'

def listGroup(lists, numberOfNewListsPerDay, numberOfListGroups):
    '''
    to devide a list into groups of sublists
    '''
    listGroup = range(numberOfListGroups)
    listGroups = []
    for i in listGroup:
        listGroups.append(lists[numberOfNewListsPerDay*(i):numberOfNewListsPerDay*(i+1)])
    return listGroups

def acuSum(numbers):
    '''
    accummulate summation over a list of numbers.
    '''
    for i,e in enumerate(numbers):
        if i == 0:
            numbers[i] = e
        else:
            numbers[i] = e + numbers[i-1]
    return numbers

def mergeLists(lists):
    '''
        merge sublists of a list into one list.
    '''
    mergedList = itertools.chain(*lists)
    return mergedList

def genTasks(listGroups, forgetLaw, days):
    '''
    generate/make a table of arrangment of lists.
    '''
    Tasks = [[] for i in range(days)]
    for i,e in enumerate(listGroups):
        for j in forgetLaw:
            Tasks[i+j].append(e)
    return Tasks

def genBoundedTasks(listGroups, forgetLaw, limit):
    '''
    generate/make a table of arrangment of lists which is more scientific.
    '''
    Tasks = [[] for i in range(200)]
    k = 0
    for i,e in enumerate(listGroups):
        for j in forgetLaw:
            #print(len(Tasks[i+j+k]))
            #print(Tasks[i+j+k])
            while len(Tasks[i+j+k]) >= limit:
                k += 1
            Tasks[i+j+k].append(e)
    return Tasks

def memo_list():
    numberOfLists = 40
    numberOfNewListsPerDay = 10
    numberOfListGroups = math.ceil(numberOfLists / numberOfNewListsPerDay)
    forgetLawBasic = [0, 1, 2, 4, 7, 15]
    forgetLaw = acuSum(forgetLawBasic)
    days = numberOfListGroups + forgetLaw[-1]
    lists = list(range(1, numberOfLists+1, 1))
    listGroups = listGroup(lists, numberOfNewListsPerDay, numberOfListGroups)
    limitNumberOfListsPerDay = 2

    Tasks2 = genTasks(listGroups, forgetLaw, days)
    Tasks = genBoundedTasks(listGroups, forgetLaw, limitNumberOfListsPerDay)

    timetable = 'timetable.txt'
    f = open(timetable, 'w+', encoding = 'utf-8')

    print(len(Tasks))
    for i in Tasks:
        ml = list(itertools.chain(*i))
        print(ml)
        for j,e in enumerate(ml):
            if j < len(ml)-1:
                f.write(str(e))
                f.write(', ')
            else:
                f.write(str(e))
        f.write('\n')
    f.close()

if __name__ == '__main__':
    memo_list()


