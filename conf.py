from data import database1
from data import database2

from data import requests1
from data import requests2
from data import requests3
from data import requests4
from data import requests6
from data import database3
from data import requests5

class conf:
    def __init__(self):
        self.database = None
        self.minDBlatency = 0
        self.maxDBlatency = 0
        self.requests = None
cnfg = {}


'''
    Users configuration starts here
'''

# Configuration One
c1 = conf()
c1.database = database1.attribute_db
c1.minDBlatency = 1
c1.maxDBlatency = 5
c1.requests = requests1.requests
cnfg[1]=c1

# Configuration Two
c2 = conf()
c2.database = database2.attribute_db
c2.minDBlatency = 1
c2.maxDBlatency = 5
c2.requests = requests2.requests
cnfg[2]=c2

# Configuration Three
c3 = conf()
c3.database = database2.attribute_db
c3.minDBlatency = 1
c3.maxDBlatency = 5
c3.requests = requests3.requests
cnfg[3]=c3

# Configuration Four
c4 = conf()
c4.database = database2.attribute_db
c4.minDBlatency = 1
c4.maxDBlatency = 5
c4.requests = requests4.requests
cnfg[4]=c4

# Configuration Six
c6 = conf()
c6.database = database2.attribute_db
c6.minDBlatency = 1
c6.maxDBlatency = 5
c6.requests = requests6.requests
cnfg[6]=c6
#config for resource conflicts
# Configuration Four
c5 = conf()
c5.database = database3.attribute_db
c5.minDBlatency = 1
c5.maxDBlatency = 5
c5.requests = requests5.requests
cnfg[5]=c5
