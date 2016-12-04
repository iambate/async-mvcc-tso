import os
import sys

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(THIS_DIR + "/..")

from config import database1

from config import requests1
from config import requests4
from config import requests6

from config import requests2
from config import database2
from config import requests21
from config import requests22
from config import requests23

from config import requests3
from config import database3
from config import requests32
from config import requests33

from config import requests5
from config import database5

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
c21.policy = "policy-example2.xml"
c21.minDBlatency = 1
c21.maxDBlatency = 5
c21.requests = requests21.requests
cnfg[21]=c21

# Configuration Two Two
c22 = conf()
c22.database = database2.attribute_db
c22.policy = "policy-example2.xml"
c22.minDBlatency = 1
c22.maxDBlatency = 5
c22.requests = requests22.requests
cnfg[22]=c22

# Configuration Two Three
c23 = conf()
c23.database = database2.attribute_db
c23.policy = "policy-example2.xml"
c23.minDBlatency = 1
c23.maxDBlatency = 5
c23.requests = requests23.requests
cnfg[23]=c23

# Configuration Three
c3 = conf()
c3.database = database2.attribute_db
c3.policy = "policy-example3.xml"
c3.minDBlatency = 1
c3.maxDBlatency = 5
c3.requests = requests3.requests
cnfg[3]=c3

# Configuration Three Two
c32 = conf()
c32.database = database3.attribute_db
c32.policy = "policy-example3.xml"
c32.minDBlatency = 1
c32.maxDBlatency = 5
c32.requests = requests32.requests
cnfg[32]=c32

# Configuration Three Three
c33 = conf()
c33.database = database3.attribute_db
c33.policy = "policy-example3.xml"
c33.minDBlatency = 1
c33.maxDBlatency = 5
c33.requests = requests33.requests
cnfg[33]=c33

# Configuration Five
c5 = conf()
c5.database = database5.attribute_db
c5.policy = "policy-example5.xml"
c5.minDBlatency = 1
c5.maxDBlatency = 5
c5.requests = requests5.requests
cnfg[5]=c5
