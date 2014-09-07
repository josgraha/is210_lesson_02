#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend:s}! I have {0} news! I won the raffle with number {1:06d}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42
d = {'friend': FNAME}
EMAIL = NEWS.format(NTYPE, RNUM, **d)
print EMAIL
# Hi Pat! I have *amazing* news! I won the raffle with number 000042!