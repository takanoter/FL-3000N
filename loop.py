import os, sys
import time, logging
#from datetime import *
def run():
    os.system('rm -f master/log/master.log.wf.*')  //fork and BLOCK

if __name__ == '__main__':
    timeout = 600 #5 minitus
    while True:
        lastTimestamp = time.time()
        run()
        nowTimestamp = time.time()
        while nowTimestamp - lastTimestamp < timeout:
            time.sleep(10)
            nowTimestamp = time.time()
    #end of while True
