import os
import re
import json

def getnewname(oldname):
    try:
        [uppath, filename] = os.path.split(oldname)
        [filename, exname] = os.path.splitext(filename)
        p = re.compile(r"([a-zA-Z]{3,4})(-|00|_|)([0-9]{3})((-|_|)[CcRr]){0,}")
        m = p.search(filename)
        if m == None:
            return oldname
        else:
            AVname = str.upper(m.group(1))
            AVindex = m.group(3)
            AVChineseSub = m.group(4)
            if(AVChineseSub):
                newname = AVname+'-'+AVindex+'-'+AVChineseSub+exname
            else:
                newname = AVname+'-'+AVindex+exname
            newname = os.path.join(uppath, newname)
            return newname
    except:
        print('AVre error')
        return oldname
        
def getallfile(path):
    def _getallfile(path,l):
        its = os.listdir(path)
        for i in its:
            if os.path.isfile(os.path.join(path,i)):
                l.append(os.path.join(path,i))
            else:
                _getallfile(os.path.join(path,i),l)
    file = []
    _getallfile(path,file)
    return file

def moveCname(namelog):
    def nameadd(name,add):
        upname, exname = os.path.splitext(name)
        name = upname+'-'+str(add)+exname
        return name
    newnamelist = [x[1] for x in namelog]
    cname = {}
    for index,newname in enumerate(newnamelist):
        if(newnamelist.count(newname) == 1):
            pass
        else:
            if newname in cname.keys():
                pass
            else:
                cname[newname] = []
                for i,n in enumerate(newnamelist):
                    if(newname == n):
                        cname[newname].append(i)
    for basefilename in cname.keys():
        for ifile in range(len(cname[basefilename])):
            namebeadded = nameadd(basefilename,ifile)
            newnamelist[cname[basefilename][ifile]] = namebeadded
    for index, newname in enumerate(newnamelist):
        namelog[index][1] = newname      
    return namelog   
  
def rename(logs):
    for index,log in enumerate(logs):
        try:
            os.renames(log[0],log[1])
        except:
            print('ERROR:',log)

def savejson(log):
    logjson = json.dumps(log)
    with open(os.path.join(os.getcwd(),'log.josn'),'w',encoding = 'utf-8') as f:
        f.write(logjson)
if __name__ == "__main__":
    path = os.getcwd()
    allfile = getallfile(os.getcwd())
    log = []
    for oldname in allfile:
        houzhui = os.path.splitext(oldname)[1]
        if(houzhui in [".mp4",".avi",".wmv",".rmvb"]):
            newname = getnewname(str(oldname))
            if(newname != oldname):
                log.append([oldname,newname])
    log = moveCname(log)
    rename(log)
    savejson(log)