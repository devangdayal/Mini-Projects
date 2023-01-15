def calcData(nbytes):
    suffix = ['Bps', 'KBps','MBps','GBps','TBps','PBps']

    i=0

    while(nbytes >=1024 and i<len(suffix)-1):
        nbytes /=1024
        i+=1
    
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')

    return '%s %s' % (f, suffix[i])
