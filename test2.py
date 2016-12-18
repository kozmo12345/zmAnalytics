#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

origin = 280
msr = 6/7
ed = 0.025
m = 1

for i in range(1,(20*m)+1):
   origin = origin + (origin * msr * ed)
print(origin)