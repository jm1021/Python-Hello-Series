from random import randrange

#Period 2
"""
t1A = "AndrewA" # 8
t1B = "AndrewB" # 7
t2A = "NoahA"   # 1
t2B = "NoahB"   # 2
t3A = "SophieA" # 3
t3B = "SophieB" # 4
t4A = "TanmayA" # 5
t4B = "TanmayB" # 6
"""

"""
#Period 4
t1A = "AbijayA" # 4
t1B = "AbijayB" # 3
t2A = "CharlieA"   # 2
t2B = "CharlieB"   # 1
t3A = "IniyaaA" # 8
t3B = "IniyaaB" # 7
t4A = "LolaA" # 6
t4B = "LolaB" # 5
"""

#Period 5
t1A = "AkA" # 5
t1B = "AkB" # 6
t2A = "ColinA"   # 3
t2B = "ColinB"   # 4
t3A = "ValerieA" # 2
t3B = "ValerieB" # 1
t4A = "ZacheryA" # 7
t4B = "ZacheryB" # 8

# Make an array
scrum = \
[t1A, t1B,
t2A, t2B, 
t3A, t3B, 
t4A, t4B]

# Random Select of scrum
i = randrange(8)
print(scrum[i])

# random Select of group
i = randrange(4)
group = scrum[i*2]
print(group[0:-1])

# random Selection of A or B of scrum
i = randrange(2)
scrumy = scrum[i]
print(scrumy[-1])