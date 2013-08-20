import sys, os, struct, getopt
import logging, time
import re
#grep "DTS" master.log.wf | grep "create task failure" | less

def fileStat(date, fileName):
    #query = 'grep "create task" %s | grep %s | grep "DTS" | cut -d " " -f13 |cut -d":" -f2| cut -d"u" -f1 | sort -g | uniq -c'% (fileName, d
ate)
    query = 'grep "create task" %s | grep %s | grep "DTS" | cut -d " " -f2 | uniq -c'% (fileName, date)
    #query = 'grep "create task failure" %s | grep %s | grep "DTS" | cut -d " " -f2 | uniq -c'% (fileName, date)
    print fileName, date, query
    pipe = os.popen(query)
    for data in pipe.readlines():
        print data
    pipe.close()



if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "m:d:")
    for op, value in opts:
        if op=="-m":
            searchMonth=value
        elif op=="-d":
            searchDay=value
        else:
            sys.exit(0)

#    searchMonth='07'
#    searchDay='28'
    searchDate=searchMonth+searchDay
    searchStartTimestamp='2013'+searchDate+'000000'
    searchStopTimestamp='2013'+searchDate+'235959'
    files = os.listdir(os.curdir)
    files.sort()
    #logFileRegex=r"master.log.wf.\d*$"
    logFileRegex=r"master.log.\d*$"
    lastInBlock = True
    for file in files:
        if re.search(logFileRegex, file):
            fileDigital = file[11:]
            #fileDigital = file[14:]
            #print fileDigital, searchStartTimestamp, searchStopTimestamp
            if fileDigital < searchStartTimestamp : continue
            if fileDigital < searchStopTimestamp:
                fileStat(searchMonth+'-'+searchDay, file)
                lastInBlock = True
            elif fileDigital > searchStopTimestamp and lastInBlock:
                fileStat(searchMonth+'-'+searchDay, file)
                lastInBlock = False
            else:
                continue
