import os
import sys

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(THIS_DIR + "/..")

from config import database1
from config import database2

from config import requests1
from config import requests2
from config import requests3
from config import requests4
from config import requests6
from config import database3
from config import requests5

from config import requests21
from config import requests22
from config import requests23

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

# Configuration Two One
c21 = conf()
c21.database = database2.attribute_db
c21.minDBlatency = 1
c21.maxDBlatency = 5
c21.requests = requests21.requests
cnfg[21]=c21

# Configuration Two Two
c22 = conf()
c22.database = database2.attribute_db
c22.minDBlatency = 1
c22.maxDBlatency = 5
c22.requests = requests22.requests
cnfg[22]=c22

# Configuration Two Three
c23 = conf()
c23.database = database2.attribute_db
c23.minDBlatency = 1
c23.maxDBlatency = 5
c23.requests = requests23.requests
cnfg[23]=c23

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
