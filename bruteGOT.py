import urllib,urllib2
import itertools
def enum_info(raw_list):
    
    (func_list,offset_list)=raw_list
    assert len(func_list)==len(offset_list)
    num=len(func_list)
    offset_Permut=list(itertools.permutations(offset_list,num))
    print 'Exist %d permutations' % len(offset_Permut)
    info_list=[]
    for offset_situation in offset_Permut:
        temp=''
        for index in xrange(num):
            temp+=func_list[index]+':'+offset_situation[index]+','
        info_list.append(temp[:-1])
        
    return info_list

    
def searchOnline(info):
    url='https://libc.blukat.me/'
    textmod ={'q':info}#'_IO_2_1_stdin_:610,__libc_start_main_ret:7ae'}
    textmod = urllib.urlencode(textmod)
    print(textmod)
    req = urllib2.Request(url = '%s%s%s' % (url,'?',textmod))
    res = urllib2.urlopen(req)
    res = res.read()
    if 'Matches' in res:
        return 1
    else:
        return 0
    
def bruteGOT(raw_list):
    info_list=enum_info(raw_list)
    for info in info_list:
        if searchOnline(info)==1:
            return info
    return False
        
def main():
    raw_list=(['printf','gets'],
               ['d80','800'] )
    
    result=bruteGOT(raw_list)
    if result is not False:
        print 'Found:',result
    else:
        print 'Not Found!'
if __name__ == "__main__":
    main()
