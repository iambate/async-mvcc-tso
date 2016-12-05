import os
import sys

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(THIS_DIR + "/..")


from config import requests1
from config import database1

from config import requests2
from config import database2

from config import requests3
from config import database3

from config import requests4
from config import database4

from config import requests5
from config import database5

from config import requests6
from config import database6

from config import requests7
from config import database7

from config import requests21
from config import database21
class conf:
    def __init__(self):
        self.database = None
        self.minDBlatency = 0
        self.maxDBlatency = 0
        self.requests = None
cnfg = {}


c1 = conf()
c1.database = database1.attribute_db
c1.policy = "policy-example1.xml"
c1.minDBlatency = 1
c1.maxDBlatency = 5
c1.requests = requests1.requests
cnfg[1]=c1

c2 = conf()
c2.database = database2.attribute_db
c2.policy = "policy-example2.xml"
c2.minDBlatency = 1
c2.maxDBlatency = 5
c2.requests = requests2.requests
cnfg[2]=c2

c3 = conf()
c3.database = database3.attribute_db
c3.policy = "policy-example3.xml"
c3.minDBlatency = 1
c3.maxDBlatency = 5
c3.requests = requests3.requests
cnfg[3]=c3

c4 = conf()
c4.database = database4.attribute_db
c4.policy = "policy-example4.xml"
c4.minDBlatency = 1
c4.maxDBlatency = 5
c4.requests = requests4.requests
cnfg[4]=c4


# Configuration Five
c5 = conf()
c5.database = database5.attribute_db
c5.policy = "policy-example5.xml"
c5.minDBlatency = 1
c5.maxDBlatency = 5
c5.requests = requests5.requests
cnfg[5]=c5


c6 = conf()
c6.database = database6.attribute_db
c6.policy = "policy-example6.xml"
c6.minDBlatency = 1
c6.maxDBlatency = 5
c6.requests = requests6.requests
cnfg[6]=c6


c7 = conf()
c7.database = database7.attribute_db
c7.policy = "policy-example7.xml"
c7.minDBlatency = 1
c7.maxDBlatency = 5
c7.requests = requests7.requests
cnfg[7]=c7

#single request for tracing
c21 = conf()
c21.database = database21.attribute_db
c21.policy = "policy-example21.xml"
c21.minDBlatency = 1
c21.maxDBlatency = 5
c21.requests = requests21.requests
cnfg[21]=c21
