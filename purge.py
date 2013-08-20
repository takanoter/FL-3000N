#coding=utf-8
import sys, os, stat
import re
curPtr=0
#wordList=[[0 for col in range(2)] for row in range(2)]  
wordList=['MAX_NIC_BANDWIDTH', 'DEFAULT_MIN_BANDWIDTH', 'MICRO_SEC',
          'NOT_RECV_NOTIFY', 'TIMEOUT', 'MAX_TASK_SIZE', 'MAX_BUF_LEN',
          'RECENT_RATE_NUM', 'SLEEP_INTERVAL', 'RENEW_LEASE_INTERVAL',
          'SPEED_THRESHOLD', 'SEND_DIRECTION', 'RECV_DIRECITON',
          'SEND_AND_RECV', 'TK_JOB_ID', 'TK_SCHED_TYPE', 'TK_PORT',
          'TK_DIRECTION', 'TK_MIN_BANDWIDTH', 'TK_MAX_BANDWIDTH',
          'TK_PRIORITY', 'TK_MASTER_HOST', 'TK_MAX_NIC_BANDWIDTH',
          'TK_LOG_LEVEL', 'TK_LOG_PATH', 'TK_LOG_FILE', 'TK_LOG_TYPE'
         ]
specialWordList=['(', '=', ' ', '\[']

def genNewWord(rawWord):
    return "k" + "".join([w.capitalize() for w in rawWord.split("_")])

def modify(filename):
    #sed -i "s/skd/ddddddd/g" filename
    for word in wordList:
        for specialWord in specialWordList:
            oldWord=specialWord+word
            newWord=specialWord+genNewWord(word)
            query = 'sed  "s/%s/%s/g" %s' % (oldWord, newWord, filename)
            #query = 'sed -i "s/%s/%s/g" %s' % (oldWord, newWord, filename)
            #print query
            os.system(query);

def walk(path):
    for item in os.listdir(path):
        subpath = os.path.join(path, item)
        mode = os.stat(subpath)[stat.ST_MODE]
        if stat.S_ISDIR(mode):
            if item == ".svn":
                continue
            else:
                walk(subpath)
        else:
            cppFileRegex=r".*cpp"
            hFileRegex=r".*h"
            if re.search(cppFileRegex, item) or re.search(hFileRegex, item):
                #print 'hahaha', path,item, subpath
                modify(subpath)
            
if __name__ == "__main__":
    walk(".")
