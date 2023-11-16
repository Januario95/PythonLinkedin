#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 09:12:23  2022

@author: Januario Cipriano
"""


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService
        
    def __str__(self):
        return "<Person ({0} {1}, {2}, {3})>".format(
            self.fname, self.lname, self.level,
            self.seniority
        )
        
    def check_employee(self, other):
        if not isinstance(other, Employee):
            raise TypeError('Can only compare between employee classes')
        
    # TODO: implement comparision functions by em level
    def __ge__(self, other):
        self.check_employee(other)
        
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.leve
        
    
    def __gt__(self, other):
        self.check_employee(other)
        
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level
    
    def __lt__(self, other):
        self.check_employee(other)
        
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level
    
    def __le__(self, other):
        self.check_employee(other)
        
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level
    
    def __eq__(self, other):
        self.check_employee(other)
        return self.level == other.level


def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebeca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durben", 5, 12))
    
    # TODO: Who's more senior?
    # print(dept[0] > dept[2])
    # print(dept[4] < dept[3])
    
    # TODO: sort the items
    emps = sorted(dept, key=lambda n: n.fname)
    for emp in emps:
        print(emp) #.lname)
    
if __name__=='__main__':
    main()
    








































