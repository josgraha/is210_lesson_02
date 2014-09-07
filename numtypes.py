#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Other numeric types."""

from decimal import *
from fractions import Fraction

FLOATVAR  = float(0.1)

DECIMALVAR = Decimal('0.1')

FRACTIONVAR = Fraction('1/10')

DF_EQUALITY = DECIMALVAR == FRACTIONVAR
print DF_EQUALITY
# False

ARE_INEQUAL = DECIMALVAR == FRACTIONVAR == FLOATVAR
print ARE_INEQUAL
# False