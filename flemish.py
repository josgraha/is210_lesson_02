#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains flemish statements."""


import inquisition

# Task 10: Using Replace
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')

# Task 11: Another Way to Replace
FLEMISH = FISHY[0:FISHY.index('Spanish')] + \
          'Flemish' + \
          FISHY[FISHY.index('Spanish') + len('Spanish'):len(FISHY)]
print FLEMISH
#"Nobody expects the Flemish Inquisition!\nOur chief weapon is haddock...haddock and fear..
#.fear and haddock....\nOur two weapons are fear and haddock...and ruthless efficiency....\
#nOur three weapons are fear, haddock, and ruthless efficiency... .\nand an almost fanatica
#l devotion to the Pope....\nOur four...no... amongst our weapons....\namongst our weaponry
# are such elements as fear, haddock....\nI'll come in again."