import os
import time
import sys

addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']

cur_time =   time.asctime(time.localtime())

print(host + "," + addr + "," + cur_time + ":" + method,file = sys.stderr)
