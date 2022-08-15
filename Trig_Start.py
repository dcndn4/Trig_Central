# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 13:06:58 2022

@author: CS_Knit_tinK_SC
"""

#Trig Start

import math

# pyth theorem

# c2 = a2 + b2
# where c is hypotenuse

#%%

#c**2 = a**2 + b**2

# if c=5 and a = 3, what is b

# 5**2 = 3**2 + b**2

# b**2 = 25 - 9
#b**2 = 16
# b=4!

b=math.sqrt(25-9)
#%%

# c**2 = 6**2+8**2
c=math.sqrt(36+64)

d=13**2
e=169+144
#%%

#13**2=a**2+12**2
g=math.sqrt(169-144)
#%%

# c2+7**2+24**2
h=math.sqrt(49+(24**2))
#%%

i=math.sqrt(65.27**2-41.955**2)
#%%

j=math.sqrt(9-2.9544**2)
#%%

# converting angle degrees to minutes
# 1 minute = 1/60 degree

# degrees, minutes, seconds

# in 16.5 degrees
# 16.5 degrees = 16 degrees, 30 min

# in 22.333 degrees
i=60*.333
# .333 = 19.98 minutes
# 22 degrees 20 minutes

# in 2.22 x 10-3 degrees

j = 2.22/1000
# = .00222 degrees
k=60*.00222
l=60/13.32
# answer = 8 seconds

# in .202 degrees

m=60*.202
# 12.12 
# = 12 minutes
l=60/12
# answer = 12 minutes 7.2 sec
#%%
# convert angles from deg-sec-min to decimal degrees

# 12 degrees 15 minutes
# 12.25 (as 15 = 25% of 60)

# 34 degrees 50 minutes
n=50/60

# 34.833 (repeating)

# 4 seconds

o=4/3600
# .00111 or 1.11 x 10(-3rd)

# 5 deg 14 min 4.8 sec

p=14/60
q=4.8/360
r=.233333+.0013333

# 5.235
#%%

# sin - built in to math module of course, but to use for angle degrees, have to add (math.radians__) in place of number
# regular number as argument is number, not angle degrees

# sine is ratio of opposite side/hypotenuse


start=math.sin((math.radians(10)))
monday=math.sin((math.radians(40)))
#%%

# tan - same functionality
# tangent = ratio of opposite side/adjacent side

mond=math.tan((math.radians(25)))

#%%

# cos - same
# cosign = adjacent side / hypotenuse

mon=math.cos((math.radians(5)))

