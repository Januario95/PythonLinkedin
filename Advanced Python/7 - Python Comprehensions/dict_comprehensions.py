#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:11:00  2022

@author: Januario Cipriano
"""


def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]
    
    # TODO: Use a comprehension to build a dictionary
    # tempDict = {t: (t*9/5)+32 for t in ctemps if t < 100}
    # print(tempDict)
    # print(tempDict[12])
    
    # TODO: Merge two dictionaries with a comprehension
    team1 = {'Jones1':24, 'Jameson': 18, 'Smith': 58,
             'Burns': 7}
    team2 = {'WWhite':12, 'Macke': 88, 'Perce': 4}
    
    newTeam = {k:v for team in (team1, team2) for k,v in team.items()}
    print(newTeam)
    
if __name__=='__main__':
    main()
    






























