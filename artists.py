#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


THE_GREAT_QUESTION = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')
STATEMENTS = THE_GREAT_QUESTION.split('. ')

print STATEMENTS
# ['Michaelangelo', 'Leonardo', 'Rafael', 'Donatello', 'Turtles? Creators of the great works? Both? You be the judge!']

# Task 5: Slicing a List
ARTISTS = STATEMENTS[0:4]
print ARTISTS
# ['Michaelangelo', 'Leonardo', 'Rafael', 'Donatello']

# Task 6: Calculating Length
NUM_ARTISTS = len(ARTISTS)
print NUM_ARTISTS
# 4

CHARACTERS = len(THE_GREAT_QUESTION)
print CHARACTERS
# 105

# Task 7: Testing Membership
HAS_CREATORS = 'Creators' in THE_GREAT_QUESTION
print HAS_CREATORS
# True

HAS_SPLINTER = 'Splinter' in ARTISTS
print HAS_SPLINTER
# False